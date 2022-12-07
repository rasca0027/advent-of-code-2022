from collections import defaultdict


f = open("input.txt", "r")

data = f.readline().rstrip()

start = 0
end = 13
chars = defaultdict(int)
for i in data[:14]:
    chars[i] += 1
while end <= len(data) - 1:
    start += 1
    end += 1
    print(chars)
    # if new is not in current set, we found it
    if data[end] not in chars.keys():
        print(end + 1)
        break
    # if new is, pop the first one and add new
    chars[data[start]] -= 1
    chars[data[end]] += 1


f.close()
