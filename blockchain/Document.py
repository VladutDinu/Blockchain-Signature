from User import User
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature.pkcs1_15 import new
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
class Document:
    def __init__(self, document_link, user):
        self.user = user
        self.document_link = document_link
        self.document_hash = SHA256.new(self.document_link.encode())
        key = RSA.importKey(open('privkey.der').read())
        cipher = pkcs1_15.new(key)
        self.digitalSignature = cipher.sign(self.document_hash)

    def getDocumentLink(self):
        return self.document_link    

    def getDocumentHash(self):
        return self.document_hash    

    def getDigitalSignature(self):
        return self.digitalSignature  
        
    def getuser(self):
        return self.user  

    def __str__(self):
        return "'document_link': {}, 'document_hash': {}, 'digital_signature': {}".format(self.document_link, self.document_hash.hexdigest(), self.digitalSignature)
            
            
            
        