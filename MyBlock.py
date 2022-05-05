import hashlib

class MyBlock:
    """A block in the blockchain
    """    
    def __init__(self, index, timestamp, data, previous_hash=""):
        print("Creating a block with index:", index, \
            "timestamp:", timestamp, \
            "data:", data, \
            "previous_hash:", previous_hash)
        
        # a unique number that tracks the position of every block in the entire blockchain.
        self._index = index

        # keeps a record of the time of occurrence of each completed transaction.
        self._timestamp = timestamp
        
        # data about the completed transactions, such as the sender details, recipient’s details, and 
        # quantity transacted.
        self._data = data

        # points to the hash of the preceding block in the blockchain, something important in maintaining 
        # the blockchain’s integrity.
        self._prevHash = previous_hash

        self._nonce = 0

        self._hash = self.calHash()

    ############# GETTERS #############

    def setHash(self, hash):
        """
        set the hash of the block

        Args:
            hash (string): hash of the block
        """        
        self._hash = hash

    def setPrevHash(self, hash):
        """
        set the previous hash of the block

        Args:
            hash (string): previous hash of the block
        """        
        self._prevHash = hash

    ############# GETTERS #############

    def getHash(self):
        """
        get the hash of the block

        Returns:
            string: hash of the block
        """        
        return self._hash

    ############# PROCESSING FUNCTIONS #############
        
    def calHash(self):
        """
        calculate the hash of the block based on its properties

        Returns:
            string: hash of the block
        """        

        sha = hashlib.sha256()
        sha.update((str(self._index) + str(self._timestamp) + str(self._data) + str(self._prevHash) + str(self._nonce)).encode('utf-8'))
        return sha.hexdigest()

    def proofOfWork(self, difficulty):
        while (self._hash[0: difficulty] != "".join(["0"] * difficulty)):
            self._nonce += 1
            self.setHash(self.calHash())