import os
import fileinput
def donate(data,f_donar,f_amount):
    f_donar.append(input("enter the donar name :"))
    f_amount.append(int(input("amount to be donated :")))
    data.write(str(f_donar[len(f_amount)-1])+" : "+ str(f_amount[len(f_amount)-1])+"\n")
    print("Unique ID is :",(len(f_amount)-1))
    return(data,f_donar,f_amount)
def retrive(data,f_donar,f_amount):
    print("enter the Unque ID to retrive your transaction data:")
    b=int(input())
    if (b<len(f_amount)):
        print("NAME:",f_donar[b])
        print("AMOUNT:",f_amount[b])
    else:
        print("entered ID does not exist")
def add_data(data,f_donar,f_amount):
    print("enter the Unque ID to edit the transaction data:")
    b=int(input())
    if (b<len(f_amount)):
        print("Enter the amount to be added :")
        c=int(input())
        for line in fileinput.input(data):
            line=line.replace(str(f_donar[len(f_amount)-1])+" : "+ str(f_amount[len(f_amount)-1]),str(f_donar[len(f_amount)-1]+c)+" : "+ str(f_amount[len(f_amount)-1]))
        f_amount[b]=f_amount[b]+c
    else:
        print("entered ID does not exist")
def retrive_all(data,f_donar,f_amount):
    for i in data:
        print([i])
if( __name__ == "__main__"):
    os.chdir("C:\\Users\\Rohit Sagar Shinde\\Desktop")
    data=open("Data.txt",'a+')
    print("for acsses of admin enter 1 and for user enter 2 : ")
    f_amount=[]
    f_donar=[]
    key=int(input())
    if(key==1):
        passcode=123456789
        print("Enter the Passcode :")
        p=int(input())
        if(p==passcode):
            while(1):
                print("For adding a donation enter 1,for retriving a data enter 2, for adding the amount to data 3,for retriving all data 4 ,EXIT 5")
                comand=int(input())
                if(comand==1):
                    donate(data,f_donar,f_amount)
                elif(comand==2):
                    retrive(data,f_donar,f_amount)
                elif(comand==3):
                    add_data(data,f_donar,f_amount)
                elif(comand==4):
                    retrive_all(data,f_donar,f_amount)
                else:
                    break
        else:
            print("------Invalid password-----")
    elif(key==2):
        
        while(1):
            print("For adding a donation enter 1,for retriving a data enter 2, for adding the amount to data 3,EXIT 5")
            comand=int(input())
            if(comand==1):
                donate(data,f_donar,f_amount)
            elif(comand==2):
                retrive(data,f_donar,f_amount)
            elif(comand==3):
                add_data(data,f_donar,f_amount)
            else:
                break
