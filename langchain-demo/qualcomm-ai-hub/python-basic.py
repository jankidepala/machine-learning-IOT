# # print(f"I am {12-1} years old.")
# # print(f"The area of a square with side 5 cm is {44+9} cm squared.")
# # print(f"The house was a good size: 1200 square feet, or {1200 * 0.092903} meters squared!")

# dog_age = 49 / 7
# print(dog_age)
# print(f"""Otto's dog age is {dog_age}. So a dog that's about
# {dog_age} would be the same age as Otto. Any dog born about {dog_age}
# years ago would be in the same stage of life as Otto.""")

import os
from dotenv import load_dotenv
import openai
import langchain

my_key = os.getenv("OPENAI_API_KEY")


from helper_functions import *

print_llm_response("What is the capital of France?")