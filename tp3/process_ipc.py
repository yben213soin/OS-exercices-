

import multiprocessing
import os
import time

def child_worker(conn):
    """Function executed by the child process."""
    child_pid = os.getpid()
    print(f"[Child  - PID {child_pid}] Process started. Waiting for data from parent...")
    
    # 3. Child receives the data from the Pipe
    message = conn.recv()
    print(f"[Child  - PID {child_pid}] Received data from parent: '{message}'")
    
    # 4. Child transforms the data (Converts to uppercase and reverses it)
    transformed = message.upper()[::-1]
    print(f"[Child  - PID {child_pid}] Transforming data...")
    
    # 5. Child sends the transformed data back to the parent
    conn.send(transformed)
    print(f"[Child  - PID {child_pid}] Sent transformed data back to parent. Exiting.")

if __name__ == "__main__":
    parent_pid = os.getpid()
    print(f"[Parent - PID {parent_pid}] Parent process initialized.")
    
    # 1. Establish IPC Mechanism: Anonymous Duplex Pipe
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # Data to be sent
    secret_message = "Operating Systems 2026"
    
    # 2. Spawn Child Process
    child_process = multiprocessing.Process(target=child_worker, args=(child_conn,))
    
    print(f"[Parent - PID {parent_pid}] Spawning child process...")
    child_process.start()
    
    # Give a tiny fraction of a second to cleanly format console output logs
    time.sleep(0.1)
    
    print(f"[Parent - PID {parent_pid}] Sending data to child: '{secret_message}'")
    parent_conn.send(secret_message)
    
    print(f"[Parent - PID {parent_pid}] Waiting for response from child...")
    # 6. Parent blocks and waits to receive the modified data
    received_back = parent_conn.recv()
    
    print(f"[Parent - PID {parent_pid}] Success! Received from child: '{received_back}'")
    
    # And Finaly the code  synchronize and clean up processes
    child_process.join()
    print(f"[Parent - PID {parent_pid}] Child process joined. Program execution completed.")
