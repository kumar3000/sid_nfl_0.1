import random, time

# Wait between 2 and 10 seconds
print("START!")

# Record start time, wait for user press, then print result
t = time.time()
input()
print(f"Score: {time.time() - t:.2f}")   
