from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, AESCCM, ChaCha20Poly1305
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

def AES_CCM_Encrypt(plaintext, key):
    plaintext_bytes = plaintext.encode('utf-8')
    aesccm = AESCCM(key)
    nonce = os.urandom(13) #largest nonce possible chosen, for max randomness - larger message size not needed (tradeoff between nonce and internal blockcoutner/message size)
    aad = None
    ciphertext = aesccm.encrypt(nonce, plaintext_bytes, aad) 
    return ciphertext, nonce

def AES_CCM_Decrypt(key, ct, aad, nonce):
    aesccm = AESCCM(key)
    return aesccm.decrypt(nonce, ct, aad)

def ChaCha20Poly1305_Encrypt(plaintext, key):
    aad = None
    plaintext_bytes = plaintext.encode('utf-8')
    nonce = os.urandom(12)
    chacha = ChaCha20Poly1305(key)
    ciphertext = chacha.encrypt(nonce, plaintext_bytes, aad)
    return ciphertext, nonce

def ChaCha20Poly1305_Decrypt(key, ct, aad, nonce):
    chacha = ChaCha20Poly1305(key)
    return chacha.decrypt(nonce, ct, aad)
