wiqa_nopara_gpt3_prompt = 
"Provide the knowledge involved in the question and answer it. \n\n 

Q: suppose squirrels get sick happens, how will it affect squirrel population. Answer Choices: (a) more (b) less (c) no effect
A: A male and female rabbit mate. The female rabbit becomes pregnant. Baby rabbits form inside of the mother rabbit. The female rabbit gives birth to a litter. The newborn rabbits grow up to become adults. The adult rabbits find mates. So the answer is (b).

Q: suppose the battery is smaller happens, how will it affect pen goes to paper. Answer Choices: (a) more (b) less (c) no effect
A: Choose what you want to write your letter on. Think of what you want to say. Write some nice things! Place the letter into an envelope. Put a stamp on the top right corner of the face of the envelope. Write the address of the recipient on the envelope. Put the envelope in your mailbox. Raise the flag on your mailbox, indicating to the mailman that you have outgoing mail.

Q: suppose more seeds are bought happens, how will it affect more seeds germinate. Answer Choices: (a) more (b) less (c) no effect
A:

Q:
A:
"

wiqa_A_gpt3_prompt = 

wiqa_KA_gpt3_prompt = 
"
Q: suppose water is shielded from heat happens, how will it affect less molecules will be broken down. Answer Choices: (a) more (b) less (c) no effect
K: Water is exposed to heat energy, like sunlight. The water temperature is raised above 212 degrees fahrenheit. The heat breaks down the molecules in the water. These molecules escape from the water. The water becomes vapor. The vapor evaporates into the atmosphere.
A: Water is shielded from heat, then water is exposed to less heat energy, less molecules will be broken down. The answer is (a) more

Q: suppose heat is applied for long periods of time happens, how will it affect less molecules will be broken down. Answer Choices: (a) more (b) less (c) no effect
K: Water is exposed to heat energy, like sunlight. The water temperature is raised above 212 degrees fahrenheit. The heat breaks down the molecules in the water. These molecules escape from the water. The water becomes vapor. The vapor evaporates into the atmosphere.
A: Heat is applied for long periods of time, then more molecules will be broken down. The answer is (b) less

Q: suppose water is not protected from high heat happens, how will it affect more vapor will form. Answer Choices: (a) more (b) less (c) no effect
K: Water is exposed to heat energy, like sunlight. The water temperature is raised above 212 degrees fahrenheit. The heat breaks down the molecules in the water. These molecules escape from the water. The water becomes vapor. The vapor evaporates into the atmosphere.
A: Water is not protected from high heat, then water is exposed to more heat energy, more vapor will form. The answer is (a) more

Q: suppose human encroachments on virgin land happens, how will it affect more evaporation. Answer Choices: (a) more (b) less (c) no effect
K: Water is exposed to heat energy, like sunlight. The water temperature is raised above 212 degrees fahrenheit. The heat breaks down the molecules in the water. These molecules escape from the water. The water becomes vapor. The vapor evaporates into the atmosphere.
A: Human encroachments on virgin land have no effect to evaporation. he answer is (c) no effect 
"


wiqa_modify_A_gpt3_prompt = 
"
Q: suppose water is shielded from heat happens, how will it affect molecules will be broken down. Answer Choices: (a) more (b) less (c) no effect
A: If water is shielded from heat, then water is exposed to less heat energy, less molecules will be broken down. The answer is (b) less

Q: suppose heat is applied for long periods of time happens, how will it affect molecules will be broken down. Answer Choices: (a) more (b) less (c) no effect
A: If heat is applied for long periods of time, then more molecules will be broken down. The answer is (a) more

Q: suppose water is not protected from high heat happens, how will it affect vapor will form. Answer Choices: (a) more (b) less (c) no effect
A: If water is not protected from high heat, then water is exposed to more heat energy, more vapor will form. The answer is (a) more

Q: suppose human encroachments on virgin land happens, how will it affect evaporation. Answer Choices: (a) more (b) less (c) no effect
A: Human encroachments on virgin land, it has no effect on evaporation. The answer is (c) no effect 

Q: suppose oxygen leaves air sacs and goes into bloodstream happens, how will it affect the amount of oxygen being delivered to the blood stream. Answer Choices: (a) more (b) less (c) no effect
A: If oxygen leaves air sacs and goes into bloodstream, then carbon dioxide will be transferred to the air sacs, a greater amount of oxygen will be delivered to the blood stream. The answer is (a) more

Q: suppose a disease or illness of the lungs happens, how will it affect the amount of oxygen being delivered to the blood stream. Answer Choices: (a) more (b) less (c) no effect
A: If a disease or illness of the lungs happens, then oxygen does not leave the air sacs into the bloodstream, less carbon dioxide will be transferred to the air sacs, a smaller amount of oxygen will be delivered to the blood stream. The answer is (b) less

Q: suppose there is no oxygen in the area happens, how will it affect oxygen does not leave the air sacs into the bloodstream. Answer Choices: (a) more (b) less (c) no effect
A: There is no oxygen in the area, it has no effect on oxygen does not leave the air sacs into the bloodstream. The answer is (c) no effect

Q: suppose more sunny days happens, how will it affect sugar and oxygen produced. Answer Choices: (a) more (b) less (c) no effect
A:
"


Q: suppose [ water is shielded from heat ] happens, how will it affect [ molecules will be broken down ]. Answer Choices: (a) more (b) less (c) no effect
A: If water is shielded from heat, then water is exposed to less heat energy, less molecules will be broken down. The answer is (b) less

Q: suppose [ heat is applied for long periods of time ] happens, how will it affect [ molecules will be broken down ]. Answer Choices: (a) more (b) less (c) no effect
A: If heat is applied for long periods of time, then more molecules will be broken down. The answer is (a) more

Q: suppose [ water is not protected from high heat ] happens, how will it affect [ vapor will form ]. Answer Choices: (a) more (b) less (c) no effect
A: If water is not protected from high heat, then water is exposed to more heat energy, more vapor will form. The answer is (a) more

Q: suppose [ human encroachments on virgin land ] happens, how will it affect [ evaporation ]. Answer Choices: (a) more (b) less (c) no effect
A: Human encroachments on virgin land, it has no effect on evaporation. The answer is (c) no effect 

Q: suppose there is no oxygen in the area happens, how will it affect oxygen does not leave the air sacs into the bloodstream. Answer Choices: (a) more (b) less (c) no effect
A: [ There is no oxygen in the area ], it has no effect on [ oxygen does not leave the air sacs into the bloodstream ]. The answer is (c) no effect 