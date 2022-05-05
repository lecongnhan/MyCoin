import hashlib

class MyBlock:
    """A block in the blockchain
    """    
    def __init__(self, index, timestamp, data, transactions=[], previous_hash=""):
        """create a new block

        Args:
            index (int): index of the block
            timestamp (datetime.time): the timestamp when the block is created
            data (string): data of the block
            previous_hash (str, optional): The hash of the previous block in the chain. Defaults to "".
        """
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

        self._difficulty = None

        self._transactions = transactions

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

    def getIndex(self):
        """
        get the index of the block

        Returns:
            int: index of the block
        """        
        return self._index

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
        """increase the difficulty entailed in mining or adding new blocks to the blockchain.

        Args:
            difficulty (int): the difficulty of the chain
        """
        self._difficulty = difficulty
        while (self._hash[0: difficulty] != "".join(["0"] * difficulty)):
            self._nonce += 1
            self.setHash(self.calHash())