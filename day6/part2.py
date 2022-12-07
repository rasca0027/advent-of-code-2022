import time
f = open("input.txt", "r")

data = f.readline().rstrip()
start = time.time()

start = 0
end = 13

while end <= len(data) - 1:
    # check current set
    if len(set(data[start: end+1])) == 14:
        print("found", end + 1)
        break
    start += 1
    end += 1

end = time.time()
print(end - start)
f.close()
