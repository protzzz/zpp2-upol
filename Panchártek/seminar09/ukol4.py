def convert_number_to_bytes(number):
    bytes_array = []
    if number:
        while number:
            byte = number & 0xff    #255
            bytes_array.append(byte)
            number = number >> 8
    else:
        bytes_array.append(0)
    return bytes_array[::-1]

def convert_bytes_to_number(bytes):
    number = 0
    for byte in bytes:
        number = number << 8
        number = number | byte
    return number

bytes_array = convert_number_to_bytes(1063)
numbers_array = convert_bytes_to_number([36, 91])
print(bytes_array)
print(numbers_array)

