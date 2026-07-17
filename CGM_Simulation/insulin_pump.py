#Represents Insulin Pump (does not include algorithms to calculate amount of insulin etc.)

class InsulinPump:
    def _init_(self):
        self.private_key = ec.generate_private_key(ec.SECP256r1(), default_backend())
        self.public_key = private_key.public_key()

    def return_public_key(self):
        return self.public_key

    def key_exchange(self, cgm_public_key):
        self.shared_key = private_key.exchange(aid_public_key)
        #use HDKF to derive the key
        self.aes_key = HDKF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"cgm-aid-connection").derive(shared_key)
