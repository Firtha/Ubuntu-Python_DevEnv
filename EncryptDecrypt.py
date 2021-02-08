from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from os import listdir
from os.path import isfile, join
import os.path

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
privKeyPEM = keyPair.exportKey()

print(f"\n\nPrivate key:")
print(privKeyPEM.decode('ascii'))

print(f"Public key:")
print(pubKeyPEM.decode('ascii'))


onlyfiles = [f for f in listdir("files-to-encrypt") if isfile(join("files-to-encrypt", f))]

for f in onlyfiles:
    print("\n\nFile is: ", f)
    reader = open("files-to-encrypt/" + f, "rb")
    msg = reader.read()
    print("- Before encryption: ", msg)
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    print("- Encrypted: ", binascii.hexlify(encrypted))
    reader.close()

    if not os.path.exists("files-encrypted/"):
        os.mkdir("files-encrypted/")

    filename = f.split(".")
    writer = open("files-encrypted/" + filename[0] + "_crypted.txt", "wb")
    writer.write(encrypted)
    writer.close()

for f in onlyfiles:
    print("\n\nFile is: ", f)
    filename = f.split(".")
    reader = open("files-encrypted/" + filename[0] + "_crypted.txt", "rb")
    encrypted = reader.read()
    print("- Before decryption: ", binascii.hexlify(encrypted))
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('- Decrypted: ', decrypted)
    reader.close()
