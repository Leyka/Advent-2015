import sys

def main():

    with open('data.txt', 'r') as file:
        data = file.read()

        count = 0
        index = 0
        for char in data:
            index +=1
            if char == '(':
                count += 1
            elif char == ')':
                count -=1

            # part 2
            if (count < 0):
                print(index)
                sys.exit()
        # part 1 
        #print(str(count))

if __name__ == '__main__':
    main()
