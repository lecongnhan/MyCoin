from MyBlock import MyBlock
from MyChain import MyChain
import datetime


def main():
    chain = MyChain()
    timestamp = datetime.datetime.now()
    block = MyBlock(1, timestamp, "Block 1")
    chain.addNewBlock(block)
    print(chain.toJson())


if __name__ == "__main__":
    main()