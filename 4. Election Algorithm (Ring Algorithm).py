class Process:
    def __init__(self, pid):
        self.pid = pid

def ring_election(processes, start):
    msg = []
    i = start
    n = len(processes)

    print(f"Process {start} starts election")
    while True:
        msg.append(processes[i].pid)
        print("Passing →", msg)
        i = (i + 1) % n
        if i == start:
            break

    print("Coordinator =", max(msg))

pids = list(map(int, input("Enter process IDs: ").split(",")))
processes = [Process(pid) for pid in pids]

start = int(input("Enter initiator index: "))
ring_election(processes, start)



//input 
Enter process IDs: 3,9,4,7,2
Enter initiator index: 2
