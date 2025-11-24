class DNS:
    def __init__(self):
        self.records = {
            "google.com": "8.8.8.8",
            "openai.com": "4.4.4.4"
        }
        self.cache = {}

    def resolve(self, host):
        if host in self.cache:
            return self.cache[host]
        ip = self.records.get(host)
        if ip:
            self.cache[host] = ip
        return ip

dns = DNS()

for h in ["google.com", "openai.com", "facebook.com"]:
    ip = dns.resolve(h)
    print(h, "→", ip)
