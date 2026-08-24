import sys
sys.path.append("/22201193")

from Blockchain.Backend.Core.blockchain import Blockchain

if __name__ == "__main__":
    print("Initializing Blockchain...")
    blockchain = Blockchain()

    blockchain.add_next_block()
    blockchain.add_next_block()

    blockchain.print()