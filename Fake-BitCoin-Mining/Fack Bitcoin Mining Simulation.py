# Write By : A.S

#This Code Is Used To Mine BitCoin ( Just a prank )

from hashlib import sha256
import time
import random
from colorama import Fore, Style, init

# Initialize colorama
init()

# Maximum number of iterations for the nonce (increased for a longer runtime)
MAX_NONCE = 100000000000

# Define the hashing function
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

# Function to simulate Bitcoin mining with enhanced features
def mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    logs_generated = 0
    start_time = time.time()
    bitcoin_found = False
    block_reward = 6.25  # Bitcoin reward for mining a block

    # Countdown before mining starts
    print("Welcome to Bitcoin Mining Simulation!")
    print("Mining will start in:")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("Mining started!\n")

    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        # Log at random intervals
        if random.randint(1, 1000) == 1:
            logs_generated += 1
            elapsed_time = time.time() - start_time
            print(f"[{elapsed_time:.2f}s] Trying nonce: {nonce} => Hash: {new_hash}")

            # Check if 10,000 logs have been generated
            if logs_generated >= 10000 and not bitcoin_found:
                print(f"Logged {logs_generated} times. Continuing mining...")

        # Simulate finding a Bitcoin with a specific message and details
        if random.randint(1, 100000) == 1 or new_hash.startswith(prefix_str):
            bitcoin_value = random.randint(200, 300)
            print(Fore.GREEN + f"🎉 Successfully mined a Bitcoin block!" + Style.RESET_ALL)
            print(f"Block Hash: {new_hash}")
            print(f"Nonce used: {nonce}")
            elapsed_time = time.time() - start_time
            print(f"Time taken: {elapsed_time:.2f} seconds")
            print(f"Reward: {block_reward} BTC")
            print(f"Total logs generated: {logs_generated}")
            bitcoin_found = True
            input("Press Enter to continue mining: ")
            print("Continuing mining...")
            break  # Exit the loop once bitcoin is found

    # Display results after mining completes
    elapsed_time = time.time() - start_time
    if bitcoin_found:
        print(Fore.GREEN + f"🎉 Congratulations! You mined a Bitcoin block successfully!" + Style.RESET_ALL)
        print(f"Total mining time: {elapsed_time:.2f} seconds")
        print("Waiting 100 seconds before showing final message...")
        time.sleep(100)  # Wait for 100 seconds after mining completes
        print(Fore.GREEN + f"Final congratulatory message after 100 seconds." + Style.RESET_ALL)
    else:
        print("Mining unsuccessful. Try again.")

    return bitcoin_found

if __name__ == "__main__":
    transactions = [
        "Player1->Player2->200",
        "Player3->Player4->450"
    ]
    difficulty = 6  # Increased difficulty for a longer runtime

    # Start mining simulation
    mine_bitcoin(
        5,
        "\n".join(transactions),
        "0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7",
        difficulty,
    )
