import hashlib


def main():

    input = 'iwrupvqb'
    nb = 0
    found = False

    while not found:
        md5 = get_md5(input + str(nb))
        print(md5)
        if md5[:6] == '000000': # a: 5 zeros, b: 6 zeros
            found = True
        else:
            nb += 1

    print("Found! number is : " + str(nb))

def get_md5(input):
    m = hashlib.md5()
    m.update(input)
    return m.hexdigest()

if __name__ == '__main__':
    main()
