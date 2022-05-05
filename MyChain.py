from MyBlock import MyBlock
import datetime
import json


class MyChain:
    def __init__(self):
        self._difficulty = 2
        self._chain = [self._createGenesisBlock()]

    def _createGenesisBlock(self):
        # get current timestamp using datetime
        timestamp = datetime.datetime.now()
        return MyBlock(0, timestamp, "Genesis Block", "")

    def getLastestBlock(self):
        return self._chain[-1]

    def addNewBlock(self, newBlock):
        lastBlock = self.getLastestBlock()
        newBlock.setPrevHash(lastBlock.getHash())
        # newBlock.setHash(newBlock.calHash())
        newBlock.proofOfWork(self._difficulty)
        self._chain.append(newBlock)

    def checkChainValidity(self):
        """
        Check if the chain is valid

        Returns:
            bool: True if valid, False if not
        """
        for i in range(1, len(self._chain)):
            curBlock = self._chain[i]
            prevBlock = self._chain[i - 1]

            if currentBlock.getHash() != currentBlock.calHash():
                return False

            if currentBlock.getPrevHash() != previousBlock.getHash():
                return False

        return True

    def toJson(self):
        return json.dumps(self._chain, default=lambda o: o.__dict__ if hasattr(o, "__dict__") else str(o), sort_keys=True, indent=4)