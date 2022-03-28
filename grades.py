'''Joshua Alexis Aviles 6520150001
    Evaluation and Improvement of Software Development
    17/02/2022
    Teacher: Marco Antonio Muñoz Portillo

    This system calculates the average of n number of grades which
    prints the average and a message according to the UTCH grade standard

    Example: 
        Enter the number of grades:
        3
        _____________________________
        Enter the grades
        8
        8
        9
        _____________________________
        SA | Avarage: 8.333333333333334
    Example: 
        Enter the number of grades:
        4
        _____________________________
        Enter the grades
        10
        10
        9
        7
        Repobatory grade! NA: 7
        _____________________________
        DE | Avarage: 9
    '''
import statistics 
    
def avg(grades):
    mean = statistics.mean(grades)
    if mean >= 8 and mean < 8.5:
        print(f'SA | Avarage: {mean}')
    elif mean >= 8.5 and mean < 9.5:
        print(f'DE | Avarage: {mean}')
    elif mean >= 9.5:
        print(f'AU | Avarage: {mean}')
    else: 
        print(f'NA | Avarage: {mean}')

if __name__ == '__main__':
    try: 
        grades = []
        print('Enter the number of grades: ')
        n = int(input())
        print('_____________________________')
        print('Enter the grades')
    
        for _ in range(0,n):
            gr = int(input()) 
            if gr < 0 or gr > 10:
                grades = 0
                break
            else:
                if gr <= 7:
                    gr = 7
                    print(f'Reprobatory grade! NA: {gr}' ) 
                else:
                    pass
                grades[len(grades):] = [gr]
        print('_____________________________')
        avg(grades)

    except (ValueError, TypeError, IndexError):
        print("ERROR: Invalid data, try again")