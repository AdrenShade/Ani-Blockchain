import hashlib

class AniCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash= previous_block_hash
        self.transction_list = transaction_list

        self.block_data = "_".join(transaction_list) + "_" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
t1 = "Ram sends 1 AC to shyam"
t2 = "raj sends 5 AC to shyam"
t3 = "shyam sends 3.2 ac to raj"
t4 = "rahul sends 4 AC to shan"
t5 = "soni sends 5 AC to ankit"
t6 = "aman sends 9 ac to himanshu"

initial_block = AniCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = AniCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = AniCoinBlock(second_block.block_hash, [t4, t5])

print(third_block.block_data)
print(third_block.block_hash)

fourth_block = AniCoinBlock(third_block.block_hash, [t5, t6])

print(fourth_block.block_data)
print(fourth_block.block_hash)