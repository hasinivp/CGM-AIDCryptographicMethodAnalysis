from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

#guide: https://cryptography.io/en/latest/hazmat/primitives/aead/


#AES often uses one key that is established at the beginning when the CGM and AID are paired 

def AES_CBC_Encrypt(plaintext, session_key):
    cipher = AES.new(key=session_key, mode=AES.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(pad(plaintext.encode('utf-8')), cipher.block_size)
    return (ciphertext.hex())
       
def AES_GCM_Encrypt(plaintext, key):      
    plaintext_bytes = plaintext.encode('utf-8')
    aad = None
    #key = AESGCM.generate_key(128)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext_bytes, aad) #appended with 16 byte tag
    return ciphertext, nonce #returns tuple

def AES_GCM_Decrypt(key, ct, aad, nonce):
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, ct, aad)

        
        
