class RoundRobin:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def next_server(self):
        if not self.servers:
            return None
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

servers = input("Enter servers (comma-separated): ").split(",")
rr = RoundRobin(servers)

n = int(input("Enter number of requests: "))

for r in range(1, n+1):
    print(f"Request {r} served by → {rr.next_server()}")


//inout
Enter servers (comma separated): S1,S2,S3
Enter number of requests: 6


