
f = open('msg.enc', 'r')

ct = f.read()

byteString = bytes.fromhex(ct)

def decryption(cipher):
    pt = []

    for char in byteString:

        char = ((179 * (char - 18)) % 256)

        pt.append(char)

    return bytes(pt)

print(decryption(ct))





