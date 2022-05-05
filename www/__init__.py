from flask import Flask
import json

_chain = None
app = Flask(__name__)

def setChain(chain):
    global _chain
    _chain = chain

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/block/<hash>", methods=["GET"])
def getBlockByHash(hash):
    global _chain

    block = _chain.getBlock(hash)

    if block is None:
        return {}

    response = app.response_class(
        response=block.toJson(),
        mimetype='application/json'
    )
    return response

@app.route("/api/transaction/<transactionId>", methods=['GET'])
def getTransactionById(transactionId):
    global _chain

    transaction = _chain.getTransaction(transactionId)

    if transaction is None:
        return {}

    response = app.response_class(
        response=transaction.toJson(),
        mimetype='application/json'
    )
    return response