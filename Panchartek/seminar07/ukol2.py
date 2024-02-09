import re

# message = "mrwfvqbfiryivfiqborxqlfrmnqanmirpvpbfvierwrfarqnxbhivgibopubqr"
# message = "mrwfvqbfiryivfiqborxqlfrmnqanmirpvpbfvierwrfarqnxbhivgibopubqr12"
message = ""
# message = ["<", "sjd"]
symbols = "abcdefghijklmnopqrstuvwxyz"


def decode(message):
    for key in range(len(symbols)):
        translated = ""
        for symbol in message:
            if symbol in symbols:
                symbolIndex = symbols.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex += len(symbols)
                
                translated += symbols[translatedIndex]
            else:
                translated += symbol
        print("Key #%s: %s" % (key,translated))


if not message:
    print("Fill the message")
else:
    try:
        if re.search(r'\d', message):
            raise TypeError("message must be letters!!!")
        decode(message)
    except TypeError as e:
        print("TypeError: ", e)
    except Exception as e:
        print("The problem is", e)