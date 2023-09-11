import os
import openai
from dotenv import load_dotenv




#load_dotenv()
#openai.api_key = os.getenv("OPENAPI_KEY")

#OPENAPI_KEY="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"
openai.api_key = "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"

print(openai.api_key)

question = input("Your Question : ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": f"{ question }"},
    ]

)
result = ''
for choice in response.choices:
    result += choice.message.content
    
print(f"we ask chatGPT {question} - here is their responcse: ")
print(result)
