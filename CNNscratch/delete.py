import time
start = time.time()

list = []
for thing in range(10000000):
    list.append( thing )

print(len( list ))
print(time.time() - start)
