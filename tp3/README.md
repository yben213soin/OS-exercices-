#  Assignment 3: Process Creation & IPC

## Younes Bendani 
---

## Project Description
This application demonstrates low-level operating system operations: spawning a dedicated child process and establishing a secure Inter-Process Communication (IPC) channel. The parent process transmits a text string to the child, which intercepts it, processes a string transformation (inversion + uppercase), and pipes the result back to the parent.

---

## Technical Report: IPC Mechanism Justification

For this task, an **Anonymous Pipe (`multiprocessing.Pipe()`)** was selected as the Inter-Process Communication mechanism. 

### Why a Pipe is Appropriate for This Task:
1. **Unicast (1-to-1) Efficiency:** A pipe inherently sets up a direct, private communication channel between exactly two endpoints (the parent and the child). Unlike a shared `Queue`, which involves internal locks and thread management overhead to handle multiple producers/consumers, a `Pipe` is lightweight and ultra-fast for strictly paired transactions.
2. **Duplex Communication:** By default, Python's `Pipe()` creates a bidirectional link. This allows us to reuse the exact same communication channel to send data down to the child and pull the response back up, avoiding the need to allocate multiple objects.
3. **Synchronization and Blocking:** The `recv()` method on a pipe is naturally blocking. This prevents race conditions: the parent process automatically halts and waits at the kernel layer until the child finishes processing and pushes bytes back into the buffer.

### Process Creation Mechanics:
On POSIX compliant operating systems (like Linux), calling `child_process.start()` triggers a native `fork()` system call under the hood. The OS clones the parent address space. Because the `Pipe` file descriptors are inherited during the fork, both isolated memory spaces retain reference handles to communicate across the boundary.

---

##  i put document an exemple for the execution  

## And for the final how to Run the Program

Execute the script inside your terminal or cloud environment:
```bash
python3 process_ipc.py

