# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956422
# Date: 13.12.2022

#intialising the variables to 0
progress = 0 
trailer = 0
retriever = 0
exclude = 0
range_ = [0,20,40,60,80,100,120] #storing the range of values allowed in the program to a list


#function to input user data in student version
def input_data_student(input_name):
    while True:
        try:
            input_type = int(input('Please enter your credits at '+ str(input_name)+': '))
            if input_type not in range_:
                print('Out of range .')
                continue
            else :
                return input_type 
        except:
            print('Integer required ')
#function to input user data in staff version
def input_data_staff(input_name):
    while True:
        try:
            input_type = int(input('Enter your total '+ str(input_name)+' credits: '))
            if input_type not in range_:
                print('Out of range .')
                continue
            else :
                return input_type 
        except:
            print('Integer required ')
#function to print histogram
def histogram():
    print('________________________________________________________________________________')
    
    if progress > 0 :
        print('Progress' ,progress, ' : ' ,progress*'*')
    if trailer > 0 :
        print('Trailer' , trailer, ' : ' ,trailer*'*')
    if retriever > 0 :
        print('Retriever ' ,retriever, ' : ' ,retriever*'*' )
    if exclude > 0 :
        print('Excluded ' ,exclude, ' : ' ,exclude*'*')
    print(progress+trailer+retriever+exclude , 'outcomes in total ')

    print('________________________________________________________________________________')
#student version of the code
def student():
    Pass=input_data_student('pass')  
    defer=input_data_student('defer')
    fail=input_data_student('fail')

    if Pass + defer + fail != 120 :
        print('Total incorrect ')    
    else :
        if Pass == 120 :
            print('Progress \n')
        elif Pass == 100:
            print('Progress (module trailer) \n') 
        elif fail >= 80 :
            print('Exclude \n')
        else :
            print('Module retriever \n')
                
#staff version of the code
def staff():
    global progress
    global trailer
    global retriever
    global exclude
    
    while True:
        #calling the input data fuction for staff version
        Pass=input_data_staff('pass')
        defer=input_data_staff('defer')
        fail=input_data_staff('fail')

        if Pass + defer + fail != 120 :
            print('Total incorrect ')
        else :
            #categorizing output progressions accoding to input data
            if Pass == 120 :
                print('Progress \n')
                progress += 1
            elif Pass == 100:
                print('Progress (module trailer) \n')
                trailer +=1 
            elif fail >= 80 :
                print('Exclude \n')
                exclude += 1
            else :
                print('Module retriever \n')
                retriever += 1
                
        print('Would you like to enter another set of data? ')

        while True:
            choice= input('Enter "y" for yes or "q" to quit and view results:')
            print('')
            if choice.lower() == 'y' or choice.lower() == 'q':
                break
            else :
                print('The choice you entered is Invalid . Please check and re-enter ')
        
        if choice.lower() == 'y':
            continue
        elif choice.lower() == 'q' :
            histogram() #calling the histogram function
            break
        
#prompting the user for a option       
while True:
    menu=input("Please enter 'staff' if you're a staff member\nPlease enter 'student' if you're a student member\n>>>")
    if menu.lower() == 'staff':
        staff() #calling the staff function
        break
    elif menu.lower() == 'student':
        student() #calling the student function
        break
    else:
        print('Invalid option please re-enter!\n')
        continue
