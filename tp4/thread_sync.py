
import threading
import time

# Global shared variables
counter = 0
NUM_THREADS = 4
ITERATIONS = 1000000

# Mutex/Lock primitive for Part 2
counter_lock = threading.Lock()

def unsynchronized_worker():
    """Worker function that increments the counter without synchronization."""
    global counter
    for _ in range(ITERATIONS):
        # Non-atomic operation: Read -> Modify -> Write
        current_value = counter
        counter = current_value + 1

def synchronized_worker():
    """Worker function that uses a Mutex (Lock) to protect the counter."""
    global counter
    for _ in range(ITERATIONS):
        
        with counter_lock:
            current_value = counter
            counter = current_value + 1
       

def run_part1_unspaced():
    global counter
    counter = 0
    threads = []
    
    print("[Part 1] Starting 4 unsynchronized threads...")
    start_time = time.time()
    
    for i in range(NUM_THREADS):
        t = threading.Thread(target=unsynchronized_worker, name=f"Unsynced-T{i+1}")
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    end_time = time.time()
    expected = NUM_THREADS * ITERATIONS
    print(f"[Part 1] Expected Result : {expected:,}")
    print(f"[Part 1] Actual Result   : {counter:,}")
    print(f"[Part 1] Discrepancy    : {expected - counter:,} lost increments!")
    print(f"[Part 1] Time taken      : {end_time - start_time:.4f} seconds\n")

def run_part2_synced():
    global counter
    counter = 0
    threads = []
    
    print("[Part 2] Starting 4 synchronized threads (using Mutex/Lock)...")
    start_time = time.time()
    
    for i in range(NUM_THREADS):
        t = threading.Thread(target=synchronized_worker, name=f"Synced-T{i+1}")
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    end_time = time.time()
    expected = NUM_THREADS * ITERATIONS
    print(f"[Part 2] Expected Result : {expected:,}")
    print(f"[Part 2] Actual Result   : {counter:,}")
    print(f"[Part 2] Success Status  : {'MATCH' if counter == expected else 'FAILURE'}")
    print(f"[Part 2] Time taken      : {end_time - start_time:.4f} seconds\n")

if __name__ == "__main__":
    run_part1_unspaced()
    print("-" * 50)
    run_part2_synced()
    

