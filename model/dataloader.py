"""Wrapper for a conditional generation dataset present in 2 tab-separated columns:
source[TAB]target
"""
import sys
import logging
import pandas as pd
from tqdm import tqdm
from typing import Optional, Union
from collections import defaultdict

import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from dataclasses import dataclass
from transformers import AutoTokenizer
from transformers.tokenization_utils_base import PreTrainedTokenizerBase, PaddingStrategy

num_choice = 3
answer_label_list = [" The answer is less.", " The answer is more.", " The answer is no effect."]
label_dict = {"less": 0, "attenuator": 0, "more": 1, "intensifier": 1, "no_effect": 2, "no effect": 2}

def process_data(data_path, is_para=False):
    data = pd.read_json(data_path, orient="records", lines=True)
    questions, answer_labels, paragraphs, input_texts = [], [], [], []

    for i, row in tqdm(data.iterrows(), total=len(data), desc="Reading QA examples"):
        text_label = row["question"]["answer_label"].strip()
        answer_labels.append(label_dict[text_label])
        para = " ".join([p.strip() for p in row["question"]["para_steps"] if len(p) > 0])
        question = row["question"]["stem"].strip()
        questions.append(question)
        paragraphs.append(para)    
        if is_para:
            input_texts += [para + question + answer_label_list[j] for j in range(num_choice)]
        else:
            input_texts += [question + answer_label_list[j] for j in range(num_choice)]

    encoded_input = tokenizer(input_texts)

    input_ids = encoded_input["input_ids"]
    if "token_type_ids" in encoded_input:
        token_type_ids = encoded_input["token_type_ids"]
    else:
        token_type_ids = [[0] * len(s) for s in encoded_input["input_ids"]]  # only BERT uses it anyways, so just set it to 0
    
    # flatten token ids
    input_ids = [{"input_ids": line} for line in input_ids]
    return input_ids, answer_labels


class MultipleChoiceDataset(Dataset):
    def __init__(self, tokenizer, data_path: str, is_para=False) -> None:
        super().__init__()
        self.data = pd.read_json(data_path, orient="records", lines=True)
        self.tokenizer = tokenizer
        self.is_para = is_para
        self.read_qa()

    def read_qa(self):
        self.questions, self.answer_labels, self.paragraphs, self.input_texts = [], [], [], []

        for i, row in tqdm(self.data.iterrows(), total=len(self.data), desc="Reading QA examples"):
            text_label = row["question"]["answer_label"].strip()
            self.answer_labels.append(label_dict[text_label])
            para = " ".join([p.strip() for p in row["question"]["para_steps"] if len(p) > 0])
            question = row["question"]["stem"].strip()
            self.questions.append(question)
            self.paragraphs.append(para)    
            if self.is_para:
                self.input_texts += [para + question + answer_label_list[j] for j in range(num_choice)]
            else:
                self.input_texts += [question + answer_label_list[j] for j in range(num_choice)]

        encoded_input = self.tokenizer(self.input_texts)
        self.input_ids = encoded_input["input_ids"]

        # flatten token ids
        # self.input_ids = [{"input_ids": line} for line in input_ids]
        # return input_ids, answer_labels

    def __len__(self) -> int:
        return len(self.answer_labels)

    def __getitem__(self, i):
        return {"input_ids": self.input_ids[i*num_choice: (i+1)*num_choice], "label": self.answer_labels[i]}
        

@dataclass
class DataCollatorForMultipleChoice:
    """
    Data collator that will dynamically pad the inputs for multiple choice received.
    """

    tokenizer: PreTrainedTokenizerBase
    padding: Union[bool, str, PaddingStrategy] = True
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None

    def __call__(self, features):
        batch_size = len(features)
        labels = [feature["label"] for feature in features]
        flattened_token_ids = [[{"input_ids": feature["input_ids"][i]} for i in range(num_choice)] for feature in features]
        flattened_token_ids = sum(flattened_token_ids, [])

        batch = self.tokenizer.pad(
            flattened_token_ids,
            padding=self.padding,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors="pt",
        )
        
        # Un-flatten
        batch = {k: v.view(batch_size, num_choice, -1) for k, v in batch.items()}
        # Add back labels
        batch["labels"] = torch.tensor(labels, dtype=torch.int64)
        return batch

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
    dataset = MultipleChoiceDataset(tokenizer, 'Data/wiqa/test.jsonl')
    dataset.map()

    flattened_features, labels = process_data('Data/wiqa/test.jsonl')
    batch = DataCollatorForMultipleChoice(tokenizer)(flattened_features[:9], labels[:3])
    print(batch)
    print(batch["input_ids"].shape)