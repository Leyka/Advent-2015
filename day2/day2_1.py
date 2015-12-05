# day 2 - part 1
def main():

    with open('data.txt', 'r') as file:
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

                surface = calc_surface_box(l,w,h)
                surface += (sorted_nb[0] * sorted_nb[1])

                total += surface

        print("total: " + str(total))


def calc_surface_box(l,w,h):
    return ((2*l*w)+(2*w*h)+(2*h*l))

if __name__ == '__main__':
    main()
