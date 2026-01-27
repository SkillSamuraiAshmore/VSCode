alphabet = "ABCDEFGHIJKLMNOPQRXYZ"

message = input("Please enter a message to encrypt: ").upper()
output = ""

key = int(input("Please enter a key: "))

for char in message:
    if char in alphabet:
        position = alphabet.find(char)
        new_position = (position + key) % 26
        new_char = alphabet[new_position]
        output += new_char
    else:
        output += char
        
print(output)