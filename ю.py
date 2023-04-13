import time
timing = time.time()
while True:
    if time.time() - timing > 10.0:
        timing = time.time()
        print("10 seconds")