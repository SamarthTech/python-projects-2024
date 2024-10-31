# **Secure Transmission of Data Using Cryptography & LSB Steganography**

import base64
from Crypto import Random
from Crypto.Cipher import AES
import pandas as pd
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from PIL import Image
import stepic


# Key Generation
def gen_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend())

    public_key = private_key.public_key()
    return private_key, public_key

def save_pvkey(pk, filename):
    pem = pk.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)

def save_pukey(pk, filename):
    pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)

private_key, public_key = gen_key()

save_pvkey(private_key, 'private_key')
save_pukey(public_key, 'public_key')
print("private key and public key generated.")

# DNA chain based encoding - Crypto
DNA_data = { "words":["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W",
                   "X","Y","Z"," ",",",".",":","0","1","2","3","4","5","6","7","8","9"],
            "DNA_code": ["CGA","CCA","GTT","TTG","GGC","GGT","TTT","CGC","ATG","AGT","AAG","TGC","TCC","TCT","GGA","GTG",
                         "AAC","TCA","ACG","TTC","CTG","CCT","CCG","CTA","AAA","CTT","ACC","TCG","GAT","GCT","ACT","TAG",
                         "ATA","GCA","GAG","AGA","TTA","ACA","AGG","GCG"]
           }

DNA_df = pd.DataFrame.from_dict(DNA_data)

# Enter the data that you want to secure
message = input("Please enter your message: ")
DNA_crypto_message = ""
word = message.upper()


for i in word:
    DNA_crypto_message+= str(DNA_df.loc[ DNA_df['words'] == i , 'DNA_code' ].iloc[0])

print(DNA_crypto_message)


# AES-128 Crypto
#block size =16

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
class AESCipher:
    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')
    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )
cipher = AESCipher('LKHlhb899Y09olUi')
AES_encrypted_message = cipher.encrypt(DNA_crypto_message)

print(AES_encrypted_message)

# Digital Signature
def load_pvkey(filename):
    with open(filename, 'rb') as pem_in:
        pemlines = pem_in.read()

    private_key = load_pem_private_key(pemlines, None, default_backend())
    return private_key

message = AES_encrypted_message
private_key = load_pvkey("private_key")
signature = private_key.sign(message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                                  salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())
print(signature)

secret_msg = AES_encrypted_message + bytes("SIGNATURE", 'utf-8') + signature


# Input any image in which you want to hide your data
# *Steganography*
# Image Steganography is the technique of hiding data(including text, image, audio, video) inside an image in such a way that a human being generally won’t be able to distinguish between the manipulated image and the original image. This adds an extra layer of security to the data being transmitted.
im = Image.open('YOUR_IMAGE.jpg')
im1 = stepic.encode(im, secret_msg)
im1.save('encoded_image.png', 'PNG')

# Your data is secured within the given image.