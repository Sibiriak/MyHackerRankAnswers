def print_rangoli(size):
    # your code goes here
    down = []
    for i in range(size):        
        letters = [chr(x) for x in reversed(range(97+i, n+97))]
        string = '-'.join(letters+list(reversed(letters))[1:])
        down.append(string)
    up = list(reversed(down))
    maxlen=4*size-3
    for x in (up+down[1:]):
        print(x.center(maxlen, '-'))

        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
