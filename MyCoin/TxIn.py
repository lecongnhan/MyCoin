class TxIn:
    def __init__(self, txOutId, txOutIndex, signature):
        """
        creates a new TxIn
        
        Args:
            txOutId (string): id of the TxOut
            txOutIndex (int): index of the TxOut
            signature (string): signature of the TxIn
        """
        self._txOutId = txOutId
        self._txOutIndex = txOutIndex
        self._signature = signature

    def getTxOutId(self):
        """
        get the id of the TxOut
        
        Returns:
            string: id of the TxOut
        """
        return self._txOutId

    def getTxOutIndex(self):
        """
        get the index of the TxOut
        
        Returns:
            int: index of the TxOut
        """
        return self._txOutIndex

    def getSignature(self):
        """
        get the signature of the TxIn
        
        Returns:
            string: signature of the TxIn
        """
        return self._signature