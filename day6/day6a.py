def day6_a():

    # Grid containing all the lights
    lights = set()

    with open('data.txt', 'r') as f:
        data = f.read().splitlines()

        for row in data:
        #row = 'toggle 0,0 through 999,999'
            if row:
                columns = row.split(' ')
                toggle = columns[0] == 'toggle'

                if toggle:
                    action = columns[0]
                    from_ = columns[1]
                    to = columns[3]
                else:
                    action = columns[1]
                    from_ = columns[2]
                    to = columns[4]

                x1, y1, x2, y2 = get_coordinates(from_, to)

                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        if toggle:
                            if (x,y) in lights:
                                lights.remove((x,y))
                            else:
                                lights.add((x,y))
                        else:
                            if action == 'on': #turn on
                                lights.add((x,y))
                            elif action == 'off' and (x,y) in lights: #turn off
                                lights.remove((x,y))

    print("Numbers lights on: " + str(len(lights))) #543903


def get_coordinates(from_, to):
     x1, y1 = from_.split(',')
     x2, y2 = to.split(',')
     x1 = int(x1)
     x2 = int(x2)
     y1 = int(y1)
     y2 = int(y2)

     return (x1, y1, x2, y2)

if __name__ == '__main__':
    day6_a()
