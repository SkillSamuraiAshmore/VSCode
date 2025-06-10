from openai import OpenAI
import os
# pass the api key
# NEVER upload this to Github
client = OpenAI(
    api_key=os.environ.get('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')
)
# define prompt
messages = []
messages.append({'role': 'user', 'content': 'what color is the sky?'})
# make an api call
response = client.chat.completions.create(messages=messages, model="gpt-4.1", n=2, max_tokens = 50)
# print the response
print(response.choices[0].message.content)