from collections import defaultdict

f = open("input.txt", "r")

fs = defaultdict(int)
current_path = []
for line in f.readlines():
    if line[0] == "$":
        # command
        if line[2] == "c":  # cd
            directory = line.rstrip().split("cd ")[1]
            if directory == "..":
                # back
                current_path.pop()
            else:
                current_path.append(directory)
    else:
        # output
        if line[:3] != "dir":
            for i in range(len(current_path), 0, -1):
                path = "/".join(current_path[:i])
                fs[path] += int(line.rstrip().split(" ")[0])
current_free_space = 70000000 - fs["/"]
required = 30000000 - current_free_space

smallest = 70000000
for directory in fs:
    if fs[directory] >= required:
        smallest = min(smallest, fs[directory])

print(smallest)
