alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

input_text=input("Enter a message:").upper()
output_text = ''

key=int(input("Please enter a number:"))

for char in input_text:
    if char in alphabet:
        position = alphabet.find(char)
        new_position = (position + key) % 26
        new_char= alphabet[new_position]
        output_text += new_char
    else:
        output_text += char
print(output_text)