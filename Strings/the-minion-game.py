def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin += len(string)-i
        else:
            Stuart += len(string)-i

    if Kevin > Stuart:
        print("Kevin", Kevin)
    elif Kevin < Stuart:
        print("Stuart", Stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
