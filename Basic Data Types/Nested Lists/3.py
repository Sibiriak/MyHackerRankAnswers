if __name__ == '__main__':
    array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        array.append([name, score])
    scores = [x[1] for x in array]
    sorted_scores = sorted(list(set(scores)))
    target = sorted_scores[1]
    names = sorted([x[0] for x in array if x[1]==target])
    for name in names:
        print(name)
