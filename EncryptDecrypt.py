from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from os import listdir
from os.path import isfile, join
import os.path

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"\n\nPrivate key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))


onlyfiles = [f for f in listdir("files-to-encrypt") if isfile(join("files-to-encrypt", f))]

for f in onlyfiles:
    print("\n\nFile is: ", f)
    reader = open("files-to-encrypt/" + f, "rb")
    msg = reader.read()
    print("\nBefore encryption: ", msg)
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    print("\nEncrypted: ", binascii.hexlify(encrypted))
    reader.close()

    if not os.path.exists("files-encrypted/"):
        os.mkdir("files-encrypted/")
        print("Directory " , "files-encrypted/",  " Created ")
    else:    
        print("Directory " , "files-encrypted/",  " already exists")

    filename = f.split(".")
    writer = open("files-encrypted/" + filename[0] + "_crypted.txt", "wb")
    writer.write(encrypted)
    writer.close()

    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\nDecrypted: ', decrypted)

for f in onlyfiles:
    print("\n\nFile is: ", f)
    filename = f.split(".")
    reader = open("files-encrypted/" + filename[0] + "_crypted.txt", "rb")
    encrypted = reader.read()
    print("\nBefore decryption: ", binascii.hexlify(encrypted))
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('\nDecrypted: ', decrypted)
    reader.close()
