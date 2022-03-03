'''Joshua Alexis Aviles
    6520150001
    Evaluation and Improvement of Software Development
    10/02/2022
    Teacher: Marco Muñoz
    
    
    '''

import statistics

def na(n):
    if n <= 7:
        n = 7
        print(f'Repobatory grade! NA: {n}' )
    else:
        pass

def avg(gr):
    print('_____________________________')
    mean = statistics.mean(gr)
    print(mean)

    if mean >= 8 and mean < 8.5:
        print(f'SA | Avarage: {mean}')
    elif mean >= 8.5 and mean < 9.5:
        print(f'DE | Avarage: {mean}')
    elif mean >= 9.5:
        print(f'AU | Avarage: {mean}')
    else: 
        print(f'NA | Avarage: {mean}')

if __name__ == '__main__':
    gr = []
    print('Enter the number of grades: ')
    x = int(input())
    print('_____________________________')
    print('Enter the grades')

    for _ in range(0,x):
        n = int(input())
        na(n)
        gr[len(gr):] = [n]
    avg(gr)