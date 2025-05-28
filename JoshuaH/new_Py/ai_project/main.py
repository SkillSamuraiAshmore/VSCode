from openai import OpenAI

# pass the api key 
# never upload this to github
client = OpenAI(
    api_key = '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'
)

# define prompt 
messages = []
messages.append({'role': 'system', 'content' : 'you are a CTO mentoring deveoplers dont onloy provide answers also ask guiding questions and make sure to get the LOOOOOOOOOOOOW TAPER FADE'})
messages.append({'role': 'user', 'content': 'why is my website down?'})

# make an api 
response = client.chat.completions.create(messages=messages, model="gpt-4.1", n=2, max_tokens = 50)
# print the response
print(response)
# print(response.choices[0].message.content)