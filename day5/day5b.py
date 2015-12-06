def main():
    with open('data.txt', 'r') as f:
        data = f.read()
        rows = data.split('\n')

        count = 0

        for text in rows:
            if has_pair_twice(text) and has_sandwich_letters(text):
                count += 1

        print(count)

def has_pair_twice(text):
    """
        It contains a pair of any two letters that appears at least twice in the string without overlapping,
        like xyxy (xy) or aabcdefgaa (aa),
        but not like aaa (aa, but it overlaps).
    """
    i = 1
    while i < len(text):
        first_two_letters = text[i-1] + text[i]
        remaining = text[i+1:]
        if first_two_letters in remaining:
            return True
        i += 1
    return False

def has_sandwich_letters(text):
    """
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    i = 0

    while i < len(text):
        try:
            letter =  text[i]
            same_letter = text[i+2]
        except:
            return False

        if letter == same_letter:
            return True
        i += 1
    return False

# def is_nice(text):
#     return (has_pair_twice(text) and repeated_letters(text))

# def has_pair_twice(text):
#     """
#         It contains a pair of any two letters that appears at least twice in the string without overlapping,
#         like xyxy (xy) or aabcdefgaa (aa),
#         but not like aaa (aa, but it overlaps).
#     """
#
#     two_letters = re.findall('..?', text)
#
#     for letters in two_letters:
#



# def repeated_letters(text):

if __name__ == '__main__':
    main()
