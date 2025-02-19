def rot13(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

# Lista de nuestros textos cifrados
texts = ["Cnvag.yax", "Favccvat Gbby.yax", "Fgvpxl Abgrf.yax", "Tbbtyr Puebzr.yax", "Svyr Rkcybere.yax", "awenG.yax", "Cbvfba Vil 2.3.yax", "CebEng.yax", "Eriratr-ENG i0.yax", "Jvaqbjf Qrsraqre.yax", "Abgrcnq.yax"]

decoded_texts = [rot13(text) for text in texts]

for original, decoded in zip(texts, decoded_texts):
    print(f"Cifrado: {original} -> Descifrado: {decoded}")

