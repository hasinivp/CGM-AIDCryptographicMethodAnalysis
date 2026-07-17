from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from cryptography.hamzat.primitives.ciphers.aead import AESGCM

#guide: https://cryptography.io/en/latest/hazmat/primitives/aead/


#AES often uses one key that is established at the beginning when the CGM and AID are paired 
class Encryption:
    def AES_CBC_Encrypt(plaintext, session_key):
        cipher = AES.new(key=session_key, mode=AES.MODE_CBC)
        ciphertext = cipher.iv + cipher.encrypt(pad(plaintext.encode('utf-8')), cipher.block_size)
        return (ciphertext.hex())
        
    def AES_GCM_Encrypt(plaintext, key):
        #temporarily - key is generated each time during encryption - will be modified to use the key generated during asymmetric key exchange
        plaintext_bytes = plaintext.encode('utf-8')
        aad = None
        key = AESGCM.generate_key(128)
        aesgcm = AESCGM(key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, plaintext_bytes, aad) #appended with 16 byte tag
        return ciphertext

    def AES_GCM_Decrypt(ct, aad, nonce):
        {
            return aesgcm.decrypt(nonce, ct, aad)
        }
        
        
