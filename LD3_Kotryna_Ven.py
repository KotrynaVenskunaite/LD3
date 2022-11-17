import os.path
from os import path


name = "Desktop\part_of_LD3_Kotryna_Ven\Foresight.txt"

def Read():
    if os.path.isfile(name) == False:           #standart reading from file
        return 0                                #if file does not exist return 0
    else:
        with open (name) as f:
            if (os.path.getsize(name) == 0):
                f.close()
                return -1
            else:
                A = f.readlines()
                f.close()
                return A

def Delete(A):
    C=[]                    #array that tracks (adds numbers) on how many lines where changed
    line_int = -1
    did_change_happen = 0

    for line in A:
        line_int+=1
        capital_letter_count = 0

        for word in line.split():           #read every individual word
            if word[0].isupper() == True:
                capital_letter_count+=1
                last_capital = word
                
        if capital_letter_count > 3:
            A[line_int] =  A[line_int].replace (last_capital, '\b') #replace last capital word with backspace
            #print (A[line_int])                                    #it may look like a square in the file tho
            did_change_happen = 1
            C.append(line_int + 1)

    if did_change_happen == 1:
        print("changes where made in lines ", end = '')
        for x in C:
            print(x, ' ', end = '')

    return A

def Write(A):
    f = open("Edit.txt", "w")
    f.writelines(A)
    f.close()

F = Read()
cwd = os.getcwd()                                                   #default python pathing (where it is installed)
if F == 0:
    print (f"file does nor exist in directory, please put your file in {cwd}")
elif F == -1:
    print("File is empty")
else:
     F = Delete(F)
     Write(F)
     print (f"your file is located in {cwd}")
