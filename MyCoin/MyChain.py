from .MyBlock import MyBlock
from .Transaction import Transaction
from .TxIn import TxIn
from .TxOut import TxOut

import datetime
import json

COINBASE_AMOUNT = 50


class MyChain:
    def __init__(self):
        self._difficulty = 2
        self._chain = [self._createGenesisBlock()]
        self._unspentTxOuts = []

    def _createGenesisBlock(self):
        """
        create the first block of the chain

        Returns:
            MyBlock: the first block of the chain
        """
        # get current timestamp using datetime
        timestamp = datetime.datetime.now()
        return MyBlock(0, timestamp, "Genesis Block", [], "")

    def getLastestBlock(self):
        """
        get the last block of the chain

        Returns:
            MyBlock: the last block of the chain
        """
        return self._chain[-1]

    def addNewBlock(self, data, transactions=[]):
        """
        generate a new block and add it to the chain

        Args:
            data (string): data of the new block

        Returns:
            MyBlock: the new block
        """
        
        lastBlock = self.getLastestBlock()
        timestamp = datetime.datetime.now()

        newBlock = MyBlock(lastBlock.getIndex() + 1, timestamp, data, transactions, lastBlock.getHash())
        newBlock.setPrevHash(lastBlock.getHash())
        newBlock.setHash(newBlock.calHash())

        newBlock.proofOfWork(self._difficulty)
        self._chain.append(newBlock)

        # Updating unspent transaction outputs
        for tx in transactions:
            for txIn in tx.getTxIns():
                self._unspentTxOuts.remove(txIn)
            for txOut in newBlock.getTxOuts():
                self._unspentTxOuts.append(txOut)

        return newBlock

    def getBlock(self, hash):
        """
        get the block with the hash

        Args:
            hash (string): hash of the block

        Returns:
            MyBlock: the block with the hash
        """
        for block in self._chain:
            if block.getHash() == hash:
                return block
        return None

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

    def generatenextBlockWithTransaction(self, address, amount):
        pass

    def signTxIn(self, transaction, txInIndex, privateKey, unspentTxOuts):
        """
        sign a TxIn

        Args:
            transaction (MyTransaction): the transaction to sign
            txInIndex (int): index of the TxIn to sign
            privateKey (string): private key of the wallet
            unspentTxOuts (list(TxOut)): list of unspent TxOuts

        Returns:
            bool: True if signed, False if not
        """
        txIn = transaction.getTxIns()[txInIndex]
        dataToSign = transaction.getId()
        # refUnspentTxOut = this._findUnspentTxOut(txIn.getTxOutId(), txIn.getTxOutIndex())
        # refAddress = MyWallet.generatePublicKeyFromPrivateKey(privateKey)
        signature = MyWallet.sign(dataToSign, privateKey)
        
    def newUnspentTxOuts(self, newUnspentTxOuts):
        """
        set the unspent TxOuts

        Args:
            newUnspentTxOuts (list(TxOut)): list of unspent TxOuts
        """
        self._unspentTxOuts = newUnspentTxOuts

    def _findUnspentTxOut(self, txOutId, txOutIndex):
        """
        find the TxOut with the id and index

        Args:
            txOutId (string): id of the TxOut
            txOutIndex (int): index of the TxOut

        Returns:
            TxOut: the TxOut with the id and index
        """
        for txOut in self._unspentTxOuts:
            if txOut.getId() == txOutId and txOut.getIndex() == txOutIndex:
                return txOut
        return None

    def _findUnspentTxOutsForAmount(self, amount):
        """
        find the TxOuts that has the amount

        Args:
            amount (int): amount of the coin

        Returns:
            list: list of TxOuts
        """
        curAmount = 0
        txOuts = []

        for txOut in self._unspentTxOuts:
            txOuts.append(txOut)
            if curAmount >= amount:
                leftOver = curAmount - amount
                return txOuts, leftOver
        
        return None

    def _toUnsignedTxIn(self, UnspentTxOut):
        """
        convert a UnspentTxOut to a TxIn

        Args:
            UnspentTxOut (TxOut): the UnspentTxOut to convert

        Returns:
            TxIn: the TxIn
        """
        return TxIn(UnspentTxOut.getId(), UnspentTxOut.getIndex())

    def _createTxOuts(self, receiverAddress, senderAddress, amount, leftOver):
        """
        create TxOuts for a transaction

        Args:
            receiverAddress (string): address of the receiver
            senderAddress (string): address of the sender
            amount (int): amount of the coin
            leftOver (int): left over amount

        Returns:
            list: list of TxOuts
        """
        txOuts = []
        if amount > 0:
            txOuts.append(TxOut(receiverAddress, amount))
        if leftOver > 0:
            txOuts.append(TxOut(senderAddress, leftOver))
        return txOuts

    def toJson(self):
        """
        convert the chain to a json string

        Returns:
            string: json string of the chain
        """
        return json.dumps(self._chain, default=lambda o: o.__dict__ if hasattr(o, "__dict__") else str(o), sort_keys=True, indent=4)