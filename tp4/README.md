# Assignment 4: Threads & Synchronization

## Younes Bendani 

## Project Description
This assignment explores the challenges of multi-threaded programming, specifically focusing on shared memory access, identifying data corruption through Race Conditions, and implementing a Mutex/Lock mechanism to guarantee thread safety.



## Technical Report

### 1. What is a Race Condition? (Observations from Part 1)
Based on the observations from Part 1, a Race Condition occurs when multiple concurrent threads try to modify a shared global variable simultaneously without any coordination. 

The core issue stems from the fact that the high-level code operation `counter += 1` is not atomic. At the CPU and OS instruction level, it is executed as three distinct steps:
1. Read: Load the current value of the counter from main memory into a local thread register.
2. Modify: Increment the register value by 1.
3. Write : Copy the updated value back from the register to the shared memory location.

When multiple threads execute this cycle concurrently, the OS scheduler can interrupt a thread mid-cycle (e.g., after the Read step but before the Write step). A second thread then reads the old value, increments it, and writes it back. When the first thread resumes, it overwrites the progress of the second thread with its own calculated value, effectively causing "lost updates." This explains why our actual final count in Part 1 falls significantly short of the expected 4,000,000.

### 2. How the Mutex/Lock Solved the Problem (Part 2)
To solve this concurrency failure, a Mutex (Mutual Exclusion Lock) via `threading.Lock()` was introduced in Part 2. 

The lock acts as a digital gatekeeper enforcing mutual exclusion over the Critical Section (the code blocks reading/writing to `counter`). 
* Before a thread is allowed to access the counter, it must execute an `acquire()` operation. 
* If another thread already holds the lock, the requesting thread is safely put into a waiting/blocked state by the OS scheduler.
* Only when the owning thread completes its Read-Modify-Write sequence and executes a `release()` operation can the next thread take the lock.

This structural serialization guarantees that only one thread can execute the counter increment at any given split-second, eradicating interleaving errors and ensuring a mathematically perfect final result of 4,000,000.

---

##  i put document an exemple for the execution  

## How to Run the Program

Execute the script inside your terminal or cloud environment:
```bash
python3 thread_sync.py

