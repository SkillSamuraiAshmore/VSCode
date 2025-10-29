from openai import OpenAI

# pass the API key
client = OpenAI()
# define prompt
message = {role: 'user', 'content':, 'why is my website now?'}
messages = []
message.append(message)

# make and api
response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

# print the response
print(response)