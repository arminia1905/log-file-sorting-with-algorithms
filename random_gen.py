import random

f = open("random_100m.txt", "w")

for i in range (0, 100000000):
    f.write(str(random.randint(1, 1000000)) + "\n")