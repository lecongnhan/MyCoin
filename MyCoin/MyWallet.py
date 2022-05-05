import random


class MyWallet:
    @staticmethod
    def generateNewPrivateKey():
        return "0x" + "".join(random.choice("0123456789abcdef") for _ in range(32))

    @staticmethod
    def generatePublicKeyFromPrivateKey(privateKey):
        """
        generate the public key from the private key

        Args:
            privateKey (string): private key

        Returns:
            string: public key
        """
        privateKey = privateKey[2:]
        publicKey = ""
        for i in range(0, len(privateKey), 2):
            publicKey += str(int(privateKey[i: i + 2], 16) * 2)
        return "0x" + publicKey

    @staticmethod
    def createNewWallet():
        """
        create a new wallet

        Returns:
            MyWallet: the new wallet
        """
        privateKey = MyWallet.generateNewPrivateKey()
        return MyWallet(privateKey)

    @staticmethod
    def sign(data, privateKey):
        """
        sign the data with the private key

        Args:
            data (string): data to sign
            privateKey (string): private key of the wallet

        Returns:
            string: signature
        """
        privateKey = privateKey[2:]
        signature = ""
        for i in range(0, len(privateKey), 2):
            signature += str(int(privateKey[i: i + 2], 16) * int(data, 16))
        return "0x" + signature

    def __init__(self, privateKey):
        self._privateKey = privateKey
        self._publicKey = MyWallet.generatePublicKeyFromPrivateKey(privateKey)

    def getPrivateKey(self):
        return self._privateKey

    def getPublicKey(self):
        return self._publicKey

    def getBalance(self, unspentTxOuts):
        """
        get the balance of the wallet

        Args:
            unspentTxOuts (list(TxOut)): list of unspent TxOuts
                
        Returns:
            int: balance of the wallet
        """
        balance = 0
        for txOut in unspentTxOuts:
            if txOut.getAddress() == self._publicKey:
                balance += txOut.getAmount()
        return balance