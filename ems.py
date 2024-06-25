print("1.Addemp\n2.viewemp\n3.updateemp\n4.deleteemp\n5.exitemp")
emp=[[1,"aisu",21,25000,"aisu@gmail.com",2,1234512345],[2,"aisuu",21,2500,"aisuu@gmail.com",2,2244668811]]
while True:
    a=int(input("Enter your choice:"))
    if a==1:
    #  for i in range(a):
        emp_id=int(input("Enter id"))
        emp_name=str(input("Enter name"))
        emp_age=int(input("Enter age"))
        emp_salarry=int(input("Enter salarry"))
        emp_email=input("Enter email")
        emp_experiance=int(input("Enter experiance"))
        emp_phno=int(input("Enter phno"))
        emp.append([emp_id,emp_name,emp_age,emp_salarry,emp_email,emp_experiance,emp_phno])

    elif a==2:
        for i in emp:
            print('emp_id:',i[0])
            print('emp_name:',i[1])
            print('emp_age:',i[2])
            print('emp_salarry:',i[3])
            print('emp_email:',i[4])
            print('emp_experiance:',i[5])
            print('emp_phno:',i[6])

    elif a==3:
        oldid=int(input("Enter old id"))
        f=0
        for i in (emp):
            if oldid==i[0]:
                f=1
                emp_name=str(input("Enter name"))
                emp_age=int(input("Enter age"))
                emp_salarry=int(input("Enter salarry"))
                emp_email=input("Enter email")
                emp_experiance=int(input("Enter experiance"))
                emp_phno=int(input("Enter phno"))

                i[1]=emp_name
                i[2]=emp_age
                i[3]=emp_salarry
                i[4]=emp_email
                i[5]=emp_experiance
                i[6]=emp_phno
        if f==0:
            print("invalid id")
    elif a==4:
            d=int(input("Enter ID needed to be deleted: "))
            f=0
            for i in emp:
                if d==i[0]:  
                    f=1
                    emp.remove(i)   
                    break               

            if f==0:
                print("ID not recognised")
            else:
                print("Updated employee list:",emp)

    elif a==5:
            print("You are exited")
            break
            
    else:
        print("INVALID -----!")    