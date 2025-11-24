lock = False
pid = 0

while True:
    key = input("Press any key to create new process (q to quit): ")
    if key == "q":
        break

    print(f"Process {pid} requesting access...")

    if not lock:
        lock = True
        print(f"Process {pid} entered critical section")
        print(f"Process {pid} exited critical section")
        lock = False
    else:
        print("Critical section busy!")

    pid += 1

//input 
(Press enter multiple times)
