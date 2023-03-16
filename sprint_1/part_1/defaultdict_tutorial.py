from collections import defaultdict

if __name__ == '__main__':

    def def_value():
        return -1


    size_a, size_b = input().split()

    d = defaultdict(list)
    for i in range(int(size_a)):
        d['group_a'].append(input())
    for i in range(int(size_b)):
        d['group_b'].append(input())
    for word in d['group_b']:
        indices = []
        for i in range(len(d['group_a'])):
            if word == d['group_a'][i]:
                indices.append(str(i + 1))
        if len(indices) == 0:
            print(-1)
        else:
            print(' '.join(indices))
