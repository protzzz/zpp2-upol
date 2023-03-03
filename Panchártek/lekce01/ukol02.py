"""
Pomoií hrubé síly prolomte iaesarovu šifru: 
”mrwfvqbfiryivfiqborxqlfrmnqanmirpvpbfvierwrfarqnxbhivgibopubqr”
"""


message = "mrwfvqbfiryivfiqborxqlfrmnqanmirpvpbfvierwrfarqnxbhivgibopubqr"
#SYMBOLS = "ABCDEFGHIJKLМNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890 !?."
SYMBOLS = "abcdefghijklmnopqrstuvwxyz"

for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)
            
            translated += SYMBOLS[translatedIndex]
        else:
            translated += symbol
    print("Key #%s: %s" % (key,translated))

