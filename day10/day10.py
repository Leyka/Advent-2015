from itertools import groupby

'''
Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud
the previous sequence and using that reading as the next sequence.
For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

For example:
1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).

Your puzzle input is 1321131112.
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?
'''

start = '1321131112'

def main():
    print(get_length(start, 40)) # First part (40 times)
    print(get_length(start, 50)) # First two (50 times)

def get_length(input, times=1):
    for i in range(times):
        input = look_and_say(input)
    return len(input)

def look_and_say(input):
    output = ''
    for nb, same_nb in groupby(input):
        count = len(list(same_nb))
        output += str(count) + str(nb)
    return output

if __name__ == '__main__':
    main()
