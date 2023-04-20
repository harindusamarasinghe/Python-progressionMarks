# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956422
# Date: 13.12.2022

#I reffered to ast module from
#site link - https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/

#importing a module to Convert a string representation of list into list
import ast
#intialising the variables to 0
progress = 0
trailer  = 0
retriever = 0
exclude = 0

input_progression = [[],[],[],[]] #nested list to save input data
_range = [0,20,40,60,80,100,120] #storing the range of values allowed in the program to a list
#function to input user data
def input_data(input_name):
    while True:
        try:
            input_type = int(input('Please enter your credits at '+ str(input_name)+': '))
            if input_type not in _range:
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
#function to display output progression
def output_data(name,string,letter_type,myList):
    if name > 0 :
        for k in  range(len(myList[3])):
            if myList[3][k]== str(letter_type):
                print(str(string) , end=' ' )
                print(",".join([str(myList[i][k]) for i in range(3)]))
def main():
    while True:
        #acessing the global variables inside the main function
        global progress
        global trailer
        global retriever
        global exclude
        
        Pass=input_data('pass')
        input_progression[0].append(Pass)

        defer=input_data('defer')
        input_progression[1].append(defer)
        
        fail=input_data('fail')
        input_progression[2].append(fail)
     
        if Pass + defer + fail != 120 :
            print('Total incorrect \n')             
        else :
            if Pass == 120 :
                print('Progress \n')
                progress += 1
                input_progression[3].append('p')
            elif Pass == 100:
                print('Progress (module trailer) \n')
                trailer +=1
                input_progression[3].append('t')
            elif fail >= 80 :
                print('Exclude \n')
                exclude += 1
                input_progression[3].append('e')
            else :
                print('Module retriever \n')
                retriever += 1
                input_progression[3].append('r')

            print('Would you like to enter another set of data?')

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
        #opening the text file in write mode
        file_txt = open("output.txt",'w')
        #writing to the file using the nested list
        file_txt.write(''.join(str(input_progression))) 
        file_txt.close() #closing the file
        file_txt = open("output.txt",'r')
        #converting the list type text file into a list
        myList= ast.literal_eval(file_txt.read())
    
        #calling the output_data function
        output_data(progress,'Progress - ','p',myList)
        output_data(trailer,'Progress (module trailer) -' ,'t',myList)
        output_data(retriever,'Module retriever -','r',myList)
        output_data(exclude, 'Exclude -' , 'e',myList)
        break

main()
