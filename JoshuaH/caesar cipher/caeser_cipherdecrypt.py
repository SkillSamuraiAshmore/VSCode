alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

input_text = input("please enyter a message to decrypt: ").upper()
output_text = ''

key = int(input("please enter a key: "))

for char in input_text:
    if char in alphabet:
        position = alphabet.find(char)
        new_position = (position - key)
        new_char = alphabet[new_position]
    else:
        output_text += char
        
print(output_text)