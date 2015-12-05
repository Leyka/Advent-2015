class Coordinate:
    ''' Two-dimensional coordination (x,y) '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '<':
            self.x -= 1
        elif direction == '>':
            self.x += 1
        else:
            pass

def main():
    coord_list = {}

    santa = Coordinate(0, 0)
    robot = Coordinate(0, 0) # part 2

    # Save start address
    coord_list[(0, 0)] = 1

    part_2 = True # part 2

    santa_turn = True

    with open('data.txt', 'r') as file:
        directions = file.read()

        for direction in directions:

            if santa_turn:
                santa.move(direction)
                if (santa.x, santa.y) in coord_list:
                    coord_list[(santa.x, santa.y)] += 1
                else:
                    coord_list[(santa.x, santa.y)] = 1

                if part_2:
                    santa_turn = False
            else:
                robot.move(direction)
                if (robot.x, robot.y) in coord_list:
                    coord_list[(robot.x, robot.y)] += 1
                else:
                    coord_list[(robot.x, robot.y)] = 1

                santa_turn = True


    count_list = len(coord_list)
    print("Unique houses: " + str(count_list))

if __name__ == '__main__':
    main()
