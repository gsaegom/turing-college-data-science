from collections import Counter

if __name__ == '__main__':

    number_shoes = int(input())

    shoes = Counter(input().split(' '))

    earnings = 0
    number_customers = int(input())

    for i in range(number_customers):
        size, price = input().split()
        if shoes[size] < 0:
            earnings += int(price)
            shoes[size] -= 1

    print(earnings)
