import hashlib
import time

#  1. The Block Class 
class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Used for mining (Proof of Work)
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Creates a SHA-256 cryptographic hash of the block's contents
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Proof-of-Work: Find a hash that starts with 'difficulty' number of zeros
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block Mined Successfully! Hash: {self.hash}")

#  2. The Blockchain Ledger Class 
class Blockchain:
    def __init__(self):
        # Initialize the chain with the Genesis block
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # The higher the number, the harder/slower it is to mine

    def create_genesis_block(self):
        # The very first block in a blockchain has no previous hash
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # Link the new block to the previous block's hash
        new_block.previous_hash = self.get_latest_block().hash
        # Require the block to be mined before adding it to the chain
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Loop through the chain to verify cryptographic integrity
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if the block's hash is still valid
            if current_block.hash != current_block.calculate_hash():
                return False
            # Check if the block correctly points to the previous block
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

#  3. Testing the Architecture 
if __name__ == "__main__":
    print("Initializing Blockchain...")
    my_blockchain = Blockchain()

    print("\nMining block 1 (Transaction: $500 to Alice)...")
    my_blockchain.add_block(Block(1, time.time(), {"amount": 500, "recipient": "Alice"}))

    print("\nMining block 2 (Transaction: $250 to Bob)...")
    my_blockchain.add_block(Block(2, time.time(), {"amount": 250, "recipient": "Bob"}))

    print(f"\nIs the blockchain cryptographically valid? {my_blockchain.is_chain_valid()}")
    
    print("\n--- Complete Blockchain Ledger ---")
    for block in my_blockchain.chain:
        print(f"Index: {block.index} | Data: {block.data} | Hash: {block.hash[:15]}...")
