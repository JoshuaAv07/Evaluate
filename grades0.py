import statistics

def average(grade):
    avg = sum(grade) / len(grade)
    return f'Grades avarage: {avg}'

def validation(grade):
    cont = 0
    for i in grade:
        if i < 0 or i > 10 or i == "":
            grade[cont] = int(input(f'{grade} is not valid'))

if __name__ == '__main__':
    while True:
        try:
            grade = list(map(int(),input().rstrip().split()))
            average(validation(grade))
            break
        except IndexError:
            validation(grade)

