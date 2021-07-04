import jsonpickle
import hashlib
from datetime import datetime
class Block:
    def __init__(self, prevHash, transaction):
        self.prevHash = prevHash
        self.transaction = transaction
        self.timestamp = datetime.today().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        hasher = hashlib.sha256()
        hasher.update(jsonpickle.encode(str(self.transaction)).encode('utf-8'))

        self.blockHash = hasher.hexdigest()

    def getHash(self):
        return self.blockHash
    
    def __str__(self):
        return "'prev_hash': {}, 'block_hash': {}, 'timestamp': {}, 'transaction': {}".format(self.prevHash, self.blockHash, self.timestamp, str(self.transaction))
            
            
            
            
        