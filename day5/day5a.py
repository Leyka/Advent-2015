def main():

    with open('data.txt', 'r') as f:
        data = f.read()
        rows = data.split('\n')

        count = 0
        for text in rows:
            if text and is_nice(text):
                print("text is nice: " + text )
                count +=1

        print("Nice words: " + str(count))


def has_at_least_three_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char in vowels:
                count += 1
    return (count >= 3)

def has_one_letter_twice(text):

    previous_letter = None

    for char in text:

        if char == previous_letter:
            return True
        else:
            previous_letter = char

    return False

def has_bad_letters(text):
    return ('ab' in text or
            'cd' in text or
            'pq' in text or
            'xy' in text)


def is_nice(text):

    return(
        has_at_least_three_vowels(text) and
        has_one_letter_twice(text) and
        not has_bad_letters(text))


if __name__ == '__main__':
    main()
