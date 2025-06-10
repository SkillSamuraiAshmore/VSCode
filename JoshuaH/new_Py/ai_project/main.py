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