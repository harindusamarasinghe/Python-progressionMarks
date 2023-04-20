# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956422
# Date: 13.12.2022

print("1 : Part 1 - Main Version\n2 : Part 2 - List(extension)\n3 : Part3 - TextFile(extension)\n4 : Part4 - Dictionary(separate program)")
while True:
    try:
        choice = int(input('\nEnter a number of your choice: '))
        print('')
        if choice ==1:
            from part1 import staff, student
            break
        elif choice ==2:
            from part2 import main
            break
        elif choice ==3:
            from part3 import main
            break
        elif choice == 4:
            from part4 import main
            break
        else:
            print('Invalid input - Please try again.')
            continue
    except:
        print('Please enter a valid integer')

