if __name__ == '__main__':

    def return_grade(student):
        return student[0]


    super_list = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        person = [name, score]
        if score not in scores:
            scores.append(score)
        super_list.append(person)
    print(scores)
    scores.sort()
    print(scores)
    second_lowest = scores[1]
    super_list.sort(key=return_grade)
    for i in range(len(super_list)):
        if super_list[i][1] == second_lowest:
            print(super_list[i][0])
