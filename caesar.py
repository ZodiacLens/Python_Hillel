def caesar (text, shift = -7 ):
    result = ""
    for symbol in text:
        if symbol.isalpha():
            base = ord('А') if symbol.isupper() else ord('а')
            shifted_symbol = chr((ord(symbol) - base + shift) % 33 + base)
            result += shifted_symbol
        else:
            result += symbol
    return result

original_text = "П цхрлъ е лхтпфхр шумчщфхр щмфп п фм ъихдшв отз.\nЩйхр цхшхь, щйхр нмот — хфп ъшцхсзпйздщ умфе."
decrypted_text = caesar(original_text)
print(decrypted_text)