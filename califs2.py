import statistics

if __name__ == '__main__':
    try: 
        gr = []
        print('Enter the number of grades: ')
        x = int(input())
        print('_____________________________')
        print('Enter the grades')
    
        for _ in range(0,x):
            n = int(input()) 
            if n < 0 or n > 10:
                break
            elif n <= 7:
                n = 7
                print(f'Repobatory grade! NA: {n}' ) 
            else:
                pass
            gr[len(gr):] = [n]

        print('_____________________________')
        mean = statistics.mean(gr)
        if mean >= 8 and mean < 8.5:
            print(f'SA | Avarage: {mean}')
        elif mean >= 8.5 and mean < 9.5:
            print(f'DE | Avarage: {mean}')
        elif mean >= 9.5:
            print(f'AU | Avarage: {mean}')
        else: 
            print(f'NA | Avarage: {mean}')

    except (ValueError, TypeError, IndexError):
        print("ERROR: Invalid data, try again")