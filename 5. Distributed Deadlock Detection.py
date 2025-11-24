resources = {
    "R1": "P1",
    "R2": "P1"
}

print("P1 acquired R1 and R2")
print("P2 waiting for R1")

if list(resources.values()).count("P1") == len(resources):
    print("Deadlock detected! P1 holds all resources.")
