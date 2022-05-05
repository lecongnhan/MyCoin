from MyBlock import MyBlock
from MyChain import MyChain
import datetime


def main():
    chain = MyChain()
    
    for i in range(0, 10):
        chain.addNewBlock("Block #" + str(i))

    print(chain.toJson())


if __name__ == "__main__":
    main()