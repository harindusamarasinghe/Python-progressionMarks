# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956422
# Date: 13.12.2022

#intialising the variables to 0
progress = 0
trailer  = 0
retriever = 0
exclude = 0
UOW = 0

stu_id = dict()
database = dict()
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
def output_data(name,string,letter_type):
     if name > 0 :
            for k in  range(len(input_progression[3])):
                if input_progression[3][k]== str(letter_type):
                    print(str(string) , end=' ' )
                    print(",".join([str(input_progression[i][k]) for i in range(3)]))
                    print("")   
def main():
    while True:
        #acessing the global variables inside the main function
        global progress
        global trailer
        global retriever
        global exclude
        global UOW
        
        while True :
            try:
                ID = input('Enter the Student ID : w')
                if len(ID)==7:
                    int(ID)
                    break
                else:
                    print('Please enter a 7 digit number as the ID')
            except:
                print('Invalid student ID try entering again!')
                continue
            
        stu_id[UOW]=ID
            
        Pass=input_data('pass')
        defer=input_data('defer')
        fail=input_data('fail')
            
        if Pass + defer + fail != 120 :
            print('Total incorrect \n')                    
        else :
            if Pass == 120 :
                print('Progress\n')
                progress += 1
                input_progression = dict ()
                input_progression['pass']=Pass
                input_progression['defer']=defer
                input_progression['fail']=fail
                output_progression = dict()
                output_progression['Progress'] = input_progression
                database[stu_id[UOW]]=output_progression 
            elif Pass == 100:
                print('Progress (module trailer)\n')
                trailer += 1
                input_progression = dict ()
                input_progression['pass']=Pass
                input_progression['defer']=defer
                input_progression['fail']=fail
                output_progression = dict()
                output_progression['Progress (module trailer)'] = input_progression
                database[stu_id[UOW]]=output_progression 
            elif fail >= 80 :
                print('Exclude\n')
                exclude += 1
                input_progression = dict ()
                input_progression['pass']=Pass
                input_progression['defer']=defer
                input_progression['fail']=fail
                output_progression = dict()
                output_progression['Exclude'] = input_progression
                database[stu_id[UOW]]=output_progression      
            else :
                print('Module retriever\n')
                retriever += 1
                input_progression = dict ()
                input_progression['pass']=Pass
                input_progression['defer']=defer
                input_progression['fail']=fail
                output_progression = dict()
                output_progression['Module retriever'] = input_progression
                database[stu_id[UOW]]=output_progression 
                    
            print('Would you like to enter another set of data?')
            UOW += 1
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
                histogram()
            for index_key in database.keys():
                output_string = 'w'+str(index_key) + " : "+ list(database[index_key].keys())[0] +" - " + str(database[index_key][list(database[index_key].keys())[0]]["pass"])+','+str(database[index_key][list(database[index_key].keys())[0]]["defer"])+','+str(database[index_key][list(database[index_key].keys())[0]]["fail"])
                print(output_string)
        break           
main()

