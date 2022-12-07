f = open("input.txt", "r")

data = f.readline().rstrip()

start = 0
end = 3

while end <= len(data) - 1:
    # check current set
    if len(set(data[start: end+1])) == 4:
        print("found", end + 1)
        break
    start += 1
    end += 1

f.close()
