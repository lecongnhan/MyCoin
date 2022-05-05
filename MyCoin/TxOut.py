class TxOut:
    def __init__(self, txOutId, txOutIndex, address, amount):
        """
        creates a new UnspendTxOut
        
        Args:
            txOutId (string): id of the TxOut
            txOutIndex (int): index of the TxOut
            address (string): address of the TxOut
            amount (int): amount of the TxOut
        """
        self._txOutId = txOutId
        self._txOutIndex = txOutIndex
        self._address = address
        self._amount = amount