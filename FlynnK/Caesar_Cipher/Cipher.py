alphabet = "ABCDEFGHIJKLMNOPQRXYZ"

message = input("Please enter a message to decrypt: ").upper()
output = ""

key = int(input("Please enter the key: "))

for char in message:
    if char in alphabet:
        position = alphabet.find(char)
        new_position = (position - key) % 26
        new_char = alphabet[new_position]
        output += new_char
    else:
        output += char
        
print(output)