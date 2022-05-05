import hashlib

class Transaction:
    def __init__(self, txIns=[], txOuts=[]):
        """
        creates a new transaction
            
        Args:
            txIns (list(TxIn)): list of transaction inputs
            txOut (list(TxOut)): list of transaction outputs
        """
        self._txIns = txIns
        self._txOuts = txOuts
        self._id = self._getTransactionId()

    def _getTransactionId(self):
        """
        get the transaction id
            
        Returns:
            string: transaction id
        """
        txInContent = ""
        for txIn in self._txIns:
            txInContent += str(txIn.getTxOutId()) + str(txIn.getTxOutIndex())

        txOutContent = ""
        for txOut in self._txOuts:
            txOutContent += str(txOut.getAmount()) + str(txOut.getAddress())

        return str(hashlib.sha256(str(txInContent + txOutContent).encode('utf-8')).hexdigest())

    def getId(self):
        """
        get the transaction id
            
        Returns:
            string: transaction id
        """
        return self._id

    def getTxIns(self):
        """
        get the transaction inputs

        Returns:
            list(TxIn): list of transaction inputs
        """
        return self._txIns

    def getTxOuts(self):
        """
        get the transaction outputs

        Returns:
            list(TxOut): list of transaction outputs
        """
        return self._txOuts