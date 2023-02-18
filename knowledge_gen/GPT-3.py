import os
import openai

openai.api_key = "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"
# os.getenv("OPENAI_API_KEY")
  # "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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Q: suppose water is shielded from heat happens, how will it affect molecules will be broken down. Answer Choices: (a) more (b) less (c) no effect \nA: If water is shielded from heat, then water is exposed to less heat energy, less molecules will be broken down. The answer is (b) less \n\nQ: suppose heat is applied for long periods of time happens, how will it affect molecules will be broken down. Answer Choices: (a) more (b) less (c) no effect \nA: If heat is applied for long periods of time, then more molecules will be broken down. The answer is (a) more \n\nQ: suppose water is not protected from high heat happens, how will it affect vapor will form. Answer Choices: (a) more (b) less (c) no effect \nA: If water is not protected from high heat, then water is exposed to more heat energy, more vapor will form. The answer is (a) more \n\nQ: suppose human encroachments on virgin land happens, how will it affect evaporation. Answer Choices: (a) more (b) less (c) no effect \nA: Human encroachments on virgin land, it has no effect on evaporation. The answer is (c) no effect  \n\nQ: suppose oxygen leaves air sacs and goes into bloodstream happens, how will it affect the amount of oxygen being delivered to the blood stream. Answer Choices: (a) more (b) less (c) no effect \nA: If oxygen leaves air sacs and goes into bloodstream, then carbon dioxide will be transferred to the air sacs, a greater amount of oxygen will be delivered to the blood stream. The answer is (a) more \n\nQ: suppose a disease or illness of the lungs happens, how will it affect the amount of oxygen being delivered to the blood stream. Answer Choices: (a) more (b) less (c) no effect \nA: If a disease or illness of the lungs happens, then oxygen does not leave the air sacs into the bloodstream, less carbon dioxide will be transferred to the air sacs, a smaller amount of oxygen will be delivered to the blood stream. The answer is (b) less \n\nQ: suppose there is no oxygen in the area happens, how will it affect oxygen does not leave the air sacs into the bloodstream. Answer Choices: (a) more (b) less (c) no effect \nA: There is no oxygen in the area, it has no effect on oxygen does not leave the air sacs into the bloodstream. The answer is (c) no effect \n\nQ: suppose more sunny days happens, how will it affect less sugar and oxygen produced. Answer Choices: (a) more (b) less (c) no effect \nA:",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

print(response)