from pyexpat.errors import messages
from openai import OpenAI

# pass the API key
client = OpenAI()
# define prompt
messages = {"role": 'user', "content":'why is my website now?'}
messages.append({"role": 'system', "content":'why is my website now?'})
messages.append({"role": 'user', "content":'why is my website now?'})

# make and api
response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

# print the response
print(response.choices[0].mess)
