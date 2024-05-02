def special_cipher(text, rotation):
    caesar_cipher = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + rotation
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            caesar_cipher += chr(shifted)
        else:
            caesar_cipher += char

    encoded = ''
    count = 1
    for i in range(1, len(caesar_cipher)):
        if caesar_cipher[i] == caesar_cipher[i - 1]:
            count += 1
        else:
            encoded += caesar_cipher[i - 1] + str(count)
            count = 1
    encoded += caesar_cipher[-1] + str(count)

    return encoded

input_text = "AABCCC"
rotation_number = 4
output = special_cipher(input_text, rotation_number)
print("Output:", output)
