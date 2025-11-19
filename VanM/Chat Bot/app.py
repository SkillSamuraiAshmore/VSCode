from pyexpat.errors import messages
from openai import OpenAI
import os

# pass the API key
client = OpenAI(
    api_key=os.environ.get('')
)

# define prompt

messages = []
messages.append({"role": 'system', "content":'what color is the sky?'})
messages.append({"role": 'user', "content":'why is my website now?'})

# make and api
response = client.chat.completions.create(messages=messages, model="gpt-4.1", n=2, max_tokens=100, temperature=0)

# print the response
print(response.choices[0].message.content)
