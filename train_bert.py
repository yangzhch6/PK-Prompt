import torch
import pandas as pd
from transformers import AutoModelForMultipleChoice, TrainingArguments, Trainer, AutoTokenizer

from model.dataloader import *
from model.metrics import *

access_token = "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"

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset_name = "wiqa"
dataset_path = "data/wiqa/test.jsonl"
with_para = True

model_checkpoint = "/home/Yangzhicheng/data/models/bert-base-uncased"
model_name = model_checkpoint.split("/")[-1]
model = AutoModelForMultipleChoice.from_pretrained(model_checkpoint).to(device=device)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, do_lower_case=True)

dataset = {}
dataset["train"] = MultipleChoiceDataset(tokenizer, 'data/wiqa/train.jsonl', with_para=with_para)
dataset["dev"] = MultipleChoiceDataset(tokenizer, 'data/wiqa/dev.jsonl', with_para=with_para)
dataset["test"] = MultipleChoiceDataset(tokenizer, 'data/wiqa/test.jsonl', with_para=with_para)

learning_rate = 2e-5
batch_size = 8
num_epochs = 20

args = TrainingArguments(
    f"checkpoints/{model_name}-finetuned-{dataset_name}-lr{learning_rate}-bs{batch_size}_para{with_para}",
    evaluation_strategy = "epoch",
    save_strategy = "epoch",
    learning_rate=learning_rate,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=num_epochs,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy"
)

trainer = Trainer(
    model,
    args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["dev"],
    tokenizer=tokenizer,
    data_collator=DataCollatorForMultipleChoice(tokenizer),
    compute_metrics=compute_metrics,
)

trainer.train()
predictions = trainer.predict(dataset["test"])
print(predictions.metrics)