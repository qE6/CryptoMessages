import argparse # args parser
import os

# RSA requirements 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import new as Random
from base64 import b64encode, b64decode

# RSA using
class RSA_Functional: 
    @staticmethod
    def generate_key(kfile=str, len=int):
        rng = Random().read
        keys = RSA.generate(len, rng)

        with open(kfile + '.private', 'wb') as f:
            f.write(keys.exportKey())
        with open(kfile + '.public', 'wb') as f:
            f.write(keys.publickey().exportKey())

    @staticmethod
    def decipher_message(msg=str, kfile=str):
        ciphertext = b64decode(msg.encode())
        with open(kfile, 'r') as f:
            private_key = RSA.import_key(f.read()) # read private key
        rsa_obj = PKCS1_v1_5.new(private_key)
        plaintext = rsa_obj.decrypt(ciphertext, 16)
        print(plaintext.decode("utf-8"))

    @staticmethod
    def decipher_file(file=str, kfile=str):
        with open(file, 'rb') as f: # read file with cipher text
            ciphertext = b64decode(f.read())
        with open(kfile, 'r') as f:
            private_key = RSA.import_key(f.read()) # read private key
        rsa_obj = PKCS1_v1_5.new(private_key) # rsa object
        plaintext = rsa_obj.decrypt(ciphertext, 16)
        with open(file + '.decipher', 'wb') as f:
            f.write(plaintext)
        print('File saved as {0}.decipher'.format(file))

    @staticmethod
    def cipher_message(msg=str, kfile=str):
        with open(kfile, 'r') as f:
            public_key = RSA.import_key(f.read()) # read public key
        rsa_obj = PKCS1_v1_5.new(public_key) # rsa object
        cipher_text = rsa_obj.encrypt(msg.encode()) # cipher with rsa
        cipher_text = b64encode(cipher_text) # encode 
        print(cipher_text.decode("utf-8")) # pring b64 encoded message

    @staticmethod
    def cipher_file(file=str, kfile=str):
        with open(kfile, 'r') as f:
            public_key = RSA.import_key(f.read())
        with open(file, 'rb') as f:
            fc = f.read()
        rsa_obj = PKCS1_v1_5.new(public_key)
        cipher_text = rsa_obj.encrypt(fc) # using 'rb' for reading. No encoding needed
        cipher_text = b64encode(cipher_text)
        print(cipher_text.decode("utf-8"))



def main():
    # argparse init
    parser = argparse.ArgumentParser(description='CryptoMessages')
    parser.add_argument('-b', type=int, help='Generate keys. Key len (ex: "-b 4096")', required=False) # key generation
    parser.add_argument('-k', type=str, help='Key file. Required for decipher/cipher/key generation', required=True) # key file. required=true
    parser.add_argument('-em', type=str, help='Text message to cipher', required=False) # message to cipher
    parser.add_argument('-ef', type=str, help='File to cipher', required=False) # file to cipher
    parser.add_argument('-dm', type=str, help='Text message to decipher', required=False) # message to cipher
    parser.add_argument('-df', type=str, help='File to decipher', required=False) # file to decipher
    ns = parser.parse_args()

    if os.path.exists(ns.k) == False:
        print("Key file not found!")
        exit(0)

    if ns.b:
        # generate key
        if ns.b in [1024,2048,4096]:
            RSA_Functional.generate_key(ns.k, ns.b)
            print("Keys successfully generated.")
            exit(0)

        print("Please use -b <1024|2048|4096>")
        exit(0)

    if ns.em:
        # cipher msg
        RSA_Functional.cipher_message(ns.em, ns.k)
        exit(0)

    if ns.ef:
        # cipher file
        if os.path.exists(ns.ef) == False:
            print("File to cipher not found!")
            exit(0)
        RSA_Functional.cipher_file(ns.ef, ns.k)
        exit(0)

    if ns.dm:
        # decipher message
        RSA_Functional.decipher_message(ns.dm, ns.k)
        exit(0)

    if ns.df:
        # decipher file
        if os.path.exists(ns.df) == False:
            print("File to decipher not found!")
            exit(0)
        RSA_Functional.decipher_file(ns.df, ns.k)
        exit(0)

    print("No functions selected")
    exit(0)


if __name__ == "__main__":
    main()