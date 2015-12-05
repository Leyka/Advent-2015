# day 2 - part 2
def main():

    with open('data2.txt', 'r') as file:
        ops = file.read().split('\n')

        total = 0

        for op in ops:
            op_array = str(op).split('x')

            if len(op_array) == 3:
                l = int(op_array[0])
                w = int(op_array[1])
                h = int(op_array[2])

                numbers = [l,w,h]
                sorted_nb = sorted(numbers)

                total += calc(sorted_nb[0], sorted_nb[1], sorted_nb[2])

        print("total: " + str(total))

def calc(nb1,nb2,nb3):
    return (2*nb1+2*nb2)+(nb1*nb2*nb3)

if __name__ == '__main__':
    main()
