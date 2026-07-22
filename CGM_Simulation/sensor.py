#Reads a message from the messages.json file to be encrypted and sent to the receiver/AID system
#Currently uses basic pre-made message simulations, and will return a new message from this database every time the function is called - eventually, this will be updated to more realistic data that is generated after each call (likely from an existing open-source simulation of glucose readings)

import json
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import encryption
import os

class Sensor:
    def __init__(self, json_filepath):
        with open(json_filepath, "r") as file:
            self.items = json.load(file)
            self.index = 0
        self.private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
        self.public_key = self.private_key.public_key()
        #serialization of public key to PEM format
        #public_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo) 
            
    def get_next_item(self):
        item = self.items[self.index]
        self.index += 1
        return item
    
    def return_public_key(self):
        return self.public_key

    def key_exchange(self, aid_public_key, key_length):
        self.shared_key = self.private_key.exchange(ec.ECDH(), aid_public_key)
        #use HDKF to derive the key
        self.aes_key = HKDF(algorithm=hashes.SHA256(), length=key_length, salt=None, info=b"cgm-aid-connection").derive(self.shared_key) 

    def aes_gcm_encryption(self):
        self.reading = self.get_next_item()
        self.plaintext = json.dumps(self.reading, indent=4)
        return encryption.AES_GCM_Encrypt(self.plaintext, self.aes_key)

    def aes_ccm_encryption(self):
        self.reading = self.get_next_item()
        self.plaintext = json.dumps(self.reading, indent=4)
        return encryption.AES_CCM_Encrypt(self.plaintext, self.aes_key)
    
    def chacha_encryption(self):
        self.reading = self.get_next_item()
        self.plaintext = json.dumps(self.reading, indent=4)
        return encryption.ChaCha20Poly1305_Encrypt(self.plaintext, self.aes_key)
