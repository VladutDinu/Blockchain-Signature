from itertools import chain
from Block import Block
from Transaction import Transaction
from User import User
from Document import Document
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from datetime import datetime
from time import sleep
class Chain:
    chain = []
    def __init__(self, genesisBlock):
        # genesis block
        self.chain.append(genesisBlock)

    def getLastBlock(self):
        return self.chain[-1]
    
    def addBlock(self, transaction):
        new_documentHash = SHA256.new(str(transaction.getDocument().getDocumentLink()).encode())
        #print('user = ' +str(transaction.getUser()))
        #print('document = ' +str(transaction.getDocument()))
        #print('new_documentHash = '+str(new_documentHash.hexdigest()))
        key = RSA.import_key(open('pubkey.der').read())
        if not pkcs1_15.new(key).verify(new_documentHash, transaction.getDocument().getDigitalSignature()):
            print('match')
            self.chain.append(Block(self.getLastBlock().getHash(), Transaction(datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%fZ'), transaction.getUser(), transaction.getDocument(), ['s1', 's2', 's3'])))
        else:
            print("no match")
    
    def __str__(self):
        chain_data = ''

        for block in self.chain:
            chain_data+= str(block)+'\n\n'

        return chain_data

if __name__ == '__main__':
    
    genesisU = User(1, 'Genesis', 'Genesis')
    u = User(1, '1stAfterGenesis', '1stAfterGenesis')
    #print('User public key = ' + str(u.get_publicKey()))
    genesisD = Document('https://www.google.com/Genesisdocument', genesisU)
    d = Document('https://www.google.com/document', u)
    #print('Document= ' + str(d))
    genesisT = Transaction(datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%fZ'), genesisU, genesisD, ['Genesis1', 'Genesis2'])
    t = Transaction(datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%fZ'), u, d, ['1stAfterGenesis1', '1stAfterGenesis2'])
    #print('Transaction= ' + str(t))
    genesisB = Block('', genesisT)
    c = Chain(genesisB)
    print(type(c.getLastBlock()))
    b = Block(c.getLastBlock().getHash(), genesisT)
    
    #print('Block=' + str(b))
    sleep(1)
    c.addBlock(t)
    print(c)
