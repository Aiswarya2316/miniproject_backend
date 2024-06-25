print("1.Registration\n2.login")
bank=[[1,"aisu",21,"aisu@gmail.com",2,'123',0],[2,"aisuu",21,"aisuu@gmail.com",2,'224',0]]
while True:
    a=int(input("Enter your choice:"))
    if a==1:
        emp_name=str(input("Enter name"))
        emp_age=int(input("Enter age"))
        emp_location=input("Enter location")
        emp_email=input("Enter email")
        emp_phno=int(input("Enter phno"))
        emp_password=str(input("Enter password"))
        bank.append([emp_name,emp_age,emp_location,emp_email,emp_phno,emp_password,0])
        print("1.Registration\n2.login")

    elif a==2:
        emp_email=input("Enter email")
        emp_password=str(input("Enter password"))
        f=0
        for i in bank:  
            if i[3]==emp_email and i[5]==emp_password:  
                f=1
                print("sucessfully login")

                while True:
                    print("1.Balance\n2.Deposit\n3.Withdraw\n4.Logout")
                    a=int(input("Enter the choice"))
                    if a==1:
                        print("balance is:",i[6])

                    elif a==2:
                        deposit=int(input("Enter your amount:",))
                        i[6]+=deposit

                    elif a==3:
                        withdraw=int(input("Enter your amount:",))
                        if i[6]>=withdraw:
                            i[6]-=withdraw 

                        else:
                            print("invalid amount:")    

                    elif a==4:
                        print("you had leave the page")
                        break

                    else:
                        print("invalid----!")       



                
            

        