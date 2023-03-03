"""
Pomocí hrubé síly prolomte Caesarovu šifru: 
”mrwfvqbfcryivfiqborxqlfrmnqanmirpvpbfvcerwrfarqnxbhcvgibopubqr”
"""

message = "mrwfvqbfcryivfiqborxqlfrmnqanmirpvpbfvcerwrfarqnxbhcvgibopubqr"
#SYMBOLS = "ABCDEFGHIJKLМNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890 !?."
SYMBOLS = "ABCDEFGHIJKLМNOPQRSTUVWXYZ"

for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print("Key #%s: %s" % (key,translated))
