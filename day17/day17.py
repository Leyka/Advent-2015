from itertools import combinations

CAPACITY = 150
eggnogs = [int(line.strip()) for line in open("input.txt", 'r')]

def a():
    count = 0
    for i in range(len(eggnogs)):
        for c in combinations(eggnogs, i):
            if sum(c) == CAPACITY:
                count +=1
    print(str(count))

def b():
    count = 0
    min_combinations = 999

    for i in range(len(eggnogs)):
        for c in combinations(eggnogs, i):
            if sum(c) == CAPACITY and len(c) < min_combinations:
                min_combinations = len(c)

    for c in combinations(eggnogs, min_combinations):
        if sum(c) == CAPACITY:
            count += 1

    print(str(count))

if __name__ == '__main__':
    a()
    b()
