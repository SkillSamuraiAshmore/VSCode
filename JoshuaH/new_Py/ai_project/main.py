import openai
from openai import OpenAI

# pass the api key 
# never upload this to github
client = OpenAI(
    #TODO: i think it's saying error 429 because we are sharing this key online, later the tutorial hides this key so it should be fine later at the end of the tutorial
    api_key = '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'
)

# define prompt 
messages = []
messages.append({'role': 'system', 'content' : 'you are a CTO mentoring deveoplers dont onloy provide answers also ask guiding questions and make sure to get the LOOOOOOOOOOOOW TAPER FADE'})
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