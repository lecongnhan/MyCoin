from MyCoin.MyBlock import MyBlock
from MyCoin.MyChain import MyChain
import www
import datetime


def main():
    chain = MyChain()
    
    for i in range(0, 10):
        chain.addNewBlock("Block #" + str(i))
    print(chain.toJson())
    
    www.setChain(chain)
    www.app.run()


if __name__ == "__main__":
    main()