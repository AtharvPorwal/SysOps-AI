import time

# Simulate some work and capture output
time.sleep(2)
with open("t1.txt", "w") as f:
    f.write("Output from Terminal 1: Command executed successfully\n")
