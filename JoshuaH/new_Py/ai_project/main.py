import openai
from openai import OpenAI
import os

# pass the api key 
# never upload this to github
client = OpenAI(
    #TODO: i think it's saying error 429 because we are sharing this key online, later the tutorial hides this key so it should be fine later at the end of the tutorial
    api_key = os.environ.get('OPENAI_API_KEY')
)
# define prompt 
messages = []
messages.append({'role': 'user', 'content': 'why is my website down?'})

try:
    
    # make an api 
    response = client.chat.completions.create(messages=messages, model="gpt-4.1", n=2, max_tokens = 50)

    # print the response
    print(response.choices[0].message.content)

# authentication issues
except openai.AuthenticationError:
    print('no valid token / authentication error')
  
except openai.BadRequestError:
    print('invalid request, read the manual!')