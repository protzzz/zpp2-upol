def convert(letter):
    mask = 0b00100000

    if ord(letter) & mask:
        return chr(ord(letter) ^ mask)
    else:
        return chr(ord(letter) | mask)

print(convert('a'))