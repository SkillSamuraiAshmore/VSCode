import openai 

# pass the api key 
# never upload this to github
openai.api_key = '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'

# define prompt 
message = {'role' : 'user', 'content' : 'why is my website down?'}
messages = []
message.append(message)

# make an api 
response = openai.ChatCompletion.create(model)
# print the response