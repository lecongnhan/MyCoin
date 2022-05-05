import json

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

    def getAmount(self):
        """
        get the amount of the TxOut
        
        Returns:
            int: amount of the TxOut
        """
        return self._amount

    def getAddress(self):
        """
        get the address of the TxOut
        
        Returns:
            string: address of the TxOut
        """
        return self._address

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

    def toJson(self):
        """
        convert the txOut to a json object

        Returns:
            dict: json object of the block
        """
        return json.dumps(self, default=lambda o: o.__dict__ if hasattr(o, "__dict__") else str(o), sort_keys=True, indent=4)