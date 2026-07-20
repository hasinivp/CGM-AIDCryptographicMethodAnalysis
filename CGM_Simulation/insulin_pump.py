#Represents Insulin Pump (does not include algorithms to calculate amount of insulin etc.)
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import encryption

class InsulinPump:
    def __init__(self):
        self.private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
        self.public_key = self.private_key.public_key()

    def return_public_key(self):
        return self.public_key

    def key_exchange(self, aid_public_key):
        self.shared_key = self.private_key.exchange(ec.ECDH(), aid_public_key)
        #use HDKF to derive the key
        self.aes_key = HKDF(algorithm=hashes.SHA256(), length=16, salt=None, info=b"cgm-aid-connection").derive(self.shared_key)
        
    def decrypt_aes(self, ciphertext, nonce):
        self.plaintext_bytes = encryption.AES_GCM_Decrypt(self.aes_key, ciphertext, None, nonce)
        self.plaintext = self.plaintext_bytes.decode('utf-8')
        return self.plaintext
    #eventually should convert to another long-term patient database with readings, etc.
