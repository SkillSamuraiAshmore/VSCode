import openai
from openai import OpenAI
import wikipedia 

# pass the api key 
# never upload this to github
client = OpenAI(
    api_key = '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'
)

# get user input
title = input('title of the page: ')

# get the wikipedia content
page = wikipedia.page(title=title, auto_suggest=False)

# define prompt
prompt = 'Write a summary of the following article: ' + page.content

prompt = 'Write a summary of the following article: ' + page.content[:10000]

# define prompt 
prompt = 'create a 5 bullet point summary of:'
messages = []
messages.append({'role': 'user', 'content': prompt})

try:
    
    # make an api 
    response = client.chat.completions.create(messages=messages, model="gpt-4.1")

    # print the response
    print(response.choices[0].message.content)

# authentication issues
except openai.AuthenticationError:
    print('no valid token / authentication error')
  
except openai.BadRequestError as e:
    print('invalid request, read the manual!')
    print(e)