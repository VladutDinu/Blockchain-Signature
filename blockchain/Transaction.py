import jsonpickle
from datetime import datetime
class Transaction:
    #signing document transaction
    
    def __init__(self, id, user, document, users_signatures):
        self.id = id
        self.user = user
        self.document = document
        self.signatures = []
        for signature in users_signatures:
            self.signatures.append(signature)
    def getDocument(self):
        return self.document

    def getSignatures(self):
        return self.signatures

    def getUser(self):
        return self.user

    def __str__(self):
        return "'id' : {}, 'user' : {}, 'document' : {}, 'signatures' : {}".format(self.id, str(self.user), str(self.document), self.signatures)