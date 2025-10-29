from openai import OpenAI

# pass the API key
client = OpenAI(
    api_key = 'sk-proj-g-Spmz5U1Igo6R2IK7yARQu5hxVFnz6PLJceQkgrWb-sg624wAcscs4fPOhBJ4EzWveZmBAOa0T3BlbkFJQSoqAvaJdpyeVILIKqM'
)
# define prompt
message = {role: 'user', 'content':, 'why is my website now?'}
messages = []
message.append(message)

# make and api
response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

# print the response
print(response)