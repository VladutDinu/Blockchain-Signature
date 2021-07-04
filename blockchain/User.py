from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256
class User:
    def __init__(self, id, complete_name, personal_IDNumber):
        self.id = id
        self.complete_name = complete_name
        self.personal_IDNumber = personal_IDNumber
        keyPair =RSA.generate(1024)
        self.pubKey = keyPair.publickey()
        self.privKeyPEM = keyPair.exportKey()
        self.publicKeyPEM = keyPair.publickey().exportKey().decode('ascii')
        with open('pubkey.der', 'w') as file:
            file.write(self.publicKeyPEM)
        self.signatureKeyPEM= keyPair.exportKey().decode('ascii')
        with open('privkey.der', 'w') as file:
            file.write(self.signatureKeyPEM)


    def get_publicKey(self):
       return self.pubKey

    def get_signatureKey(self):
       return self.privKeyPEM

    def __str__(self):
        #return "'id': {}, 'complete_name': {}, 'public_key': {},  'signature_key': {}".format(self.id, self.complete_name, self.publicKeyPEM, self.signatureKeyPEM)
        return "'id': {}, 'complete_name': {}".format(self.id, self.complete_name)
            