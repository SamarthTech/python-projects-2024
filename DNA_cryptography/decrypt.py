# **Decryption End of the DNA crypto**

from hashlib import sha256
import base64
from Crypto import Random
from Crypto.Cipher import AES
import pandas as pd
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from PIL import Image
import stepic


# upload your image you want to decrypt
im = Image.open('encoded_image.png')
stegoImage = stepic.decode(im)

ind_sep = stegoImage.find('SIGNATURE')
message = bytes(stegoImage[:ind_sep],'utf-8')
signature = bytes(stegoImage[ind_sep+9:], 'latin1')

def load_pukey(filename):
    with open(filename, 'rb') as pem_in:
        pemlines = pem_in.read()
    public_key = load_pem_public_key(pemlines, default_backend())
    return public_key

public_key = load_pukey("public_key")
try:
    public_key.verify(signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                                  salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())
    print(message)
except InvalidSignature:
    print('Invalid!')


# AES decryption
BS = 16
unpad = lambda s : s[0:-ord(s[-1:])]

class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode('utf8')

cipher = AESCipher('LKHlhb899Y09olUi')
AES_decrypted = cipher.decrypt(message)

print(AES_decrypted)


DNA_data = { "words":["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W",
                   "X","Y","Z"," ",",",".",":","0","1","2","3","4","5","6","7","8","9"],
            "DNA_code": ["CGA","CCA","GTT","TTG","GGC","GGT","TTT","CGC","ATG","AGT","AAG","TGC","TCC","TCT","GGA","GTG",
                         "AAC","TCA","ACG","TTC","CTG","CCT","CCG","CTA","AAA","CTT","ACC","TCG","GAT","GCT","ACT","TAG",
                         "ATA","GCA","GAG","AGA","TTA","ACA","AGG","GCG"]
           }

DNA_df = pd.DataFrame.from_dict(DNA_data)

l = [AES_decrypted[i:i+3] for i in range(0, len(AES_decrypted), 3)]


original_message = ""
for i in l:
    original_message+= str(DNA_df.loc[ DNA_df['DNA_code'] == i , 'words' ].iloc[0])
print("The secret message is: ",original_message.lower())

# your orginal data is decrypted safely