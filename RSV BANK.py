#GIVE PASSWORD FOR SQL ONE
from datetime import date
import random
import mysql.connector as m
import time
import adda 
import pickle
def main_page():
    global mpc
    a=" "
    print('\n')
    print(a*48+"RSV Group of Banks")
    print('\n')
    samson=int(input('''1--> EMPLOYEE
2--> CUSTOMER
3--> ADMIN:'''))
    if samson==2:
        print("Dear customer welcome to Our RSV Bank. We are glad to serve you here at our Bank.")
        time.sleep(2)
        print("Our bank has many features like 'LOANS AT THE LOWEST INTEREST EVER', 'TRANSACTION MADE EASY', 'FAST AND QUICK REPLIES FOR QUERIES' etc...")
        time.sleep(2)
        print('\n')
        print("So dear customer are you new to our bank or do you have an account in our bank??")
        time.sleep(2)
        print("""Enter 1 --> if you DON'T HAVE AN ACCOUNT in our bank
          2 --> if you ALREADY HAVE AN ACCOUNT in our bank """)
        time.sleep(2)
        print('\n')
        x=0
        while x==0:
            mpc=input("Enter your choice (1 or 2) :")
            if mpc=='1' or mpc=='2':
                x=1
            else:
                print("Dear customer please enter a valid choice....")
        if mpc=='1':
            print("Dear customer do you wish to create an account in our bank or do you want to just surf through it??")
            print("""Enter 1 --> if you want to CREATE AN ACCOUNT
2 --> if you just want to SURF THROUGH THE BANK""")
            choice=input("Enter your choice (1 or 2) :")
            if choice=='1':
                new_user()
            if choice=='2':
                info()
        if mpc=='2':
            already_user()
    if samson==1:
        print("Welcome employee,hope you have a good day")
        time.sleep(2)
        print()
        employee()
    if samson==3:
        admin()
def new_user():
    d100={}
    d1={}
    d1['bal']=0
    d1['deposit']=[]
    d1['withdraw']=[]
    d1['fundtransfer']=[]
    time.sleep(2)
    print('\n')
    print("Dear customer now let's create an account for you in our bank")
    print("STEP 1 :For Account creation, please provide us with the following details.")
    time.sleep(1)
    print("The details should be provided with utmost care else your account may not be created....")
    time.sleep(2)
    print("So kindly be Alert while giving your details. Enter Nil if not.")
    time.sleep(2)
    i=0
    while i==0:
        print('\n')
        name=input("Enter your Full Name :")
        if name.isspace() or len(name)==0 or name.isdigit():
            print("Dear customer please enter a proper name.......")
        else:
            i=1
            d1["name"]=name
    while i==1:
        father_name=input("Enter your Father's name :")
        if father_name.isspace() or len(father_name)==0 or father_name.isdigit():
            print("Dear customer please enter a proper name.......")
        else:
            i=2
            d1["father_name"]=father_name
    while i==2:
        mother_name=input("Enter your Mother's name :")
        if mother_name.isspace() or len(mother_name)==0 or mother_name.isdigit():
            print("Dear customer please enter a proper name.......")
        else:
            i=3
            d1["mother_name"]=mother_name
    while i==3:
        guardian_name=input("Enter your Guardian name/Relative name (Enter 'Nil' if father's name or mother's name has been already entered) :")
        if guardian_name.isspace() or len(guardian_name)==0 or guardian_name.isdigit():
            print("Dear customer please enter a proper name.......")
        else:
            i=4
            d1["guardian_name"]=guardian_name
    while i==4:
        gender=input("Enter your Gender (Male/Female/Others) :")
        if gender.upper()=="MALE" or gender.upper()=="FEMALE" or gender.upper()=="OTHERS":
            i=5
            d1["gender"]=gender
        else:
            print("Please enter a valid option Dear Customer....")
    while i==5:
        date_of_birth=input("Enter your Date Of Birth (YYYY-MM-DD format) :")
        if date_of_birth.isspace() or date_of_birth.isalpha() or len(date_of_birth)!=10:
            print("Please enter a valid Date Of Birth...")
        elif date_of_birth[4]=='-'and date_of_birth[7]=='-':
            a=date_of_birth.split("-")
            b=str(date.today()).split("-")
            if a[0].isdigit() and a[1].isdigit() and a[2].isdigit():
                if len(a[0])==4 and len(a[1])==2 and len(a[2])==2:
                    if (int(b[0])-int(a[0]))>=5 and (int(b[0])-int(a[0]))<=100 and int(b[0])>int(a[0]):
                        if a[1]=='02' and int(a[2])<=29 and int(a[0])%4==0:
                            i=6
                            d1["date_of_birth"]=date_of_birth
                        elif a[1]=='02' and int(a[2])<=28:
                            i=6
                            d1["date_of_birth"]=date_of_birth
                        elif(a[1]=='01'or a[1]=='03'or a[1]=='05'or a[1]=='07'or a[1]=='08'or a[1]=='10'or a[1]=='12') and int(a[2])<=31:
                            i=6
                            d1["date_of_birth"]=date_of_birth
                        elif(a[1]=='04'or a[1]=='06'or a[1]=='09'or a[1]=='11')and int(a[2])<=30:
                            i=6
                            d1["date_of_birth"]=date_of_birth
                        else:
                            print("Please enter a valid date of birth in the pattern as given above....")
                    if b[1]==a[1] and b[2]==a[2] and (int(b[0])-int(a[0]))>=5 and (int(b[0])-int(a[0]))<=100:
                        print("OMG!! Happy Birthday Dear customer")
                        time.sleep(2)
                        print("You turned",int(b[0])-int(a[0]),"today. Congratulations!!")
                        i=6
                        d1["date_of_birth"]=date_of_birth
                    if b[1]==a[1] and b[2]==a[2] and (int(b[0])-int(a[0]))<5:
                        print("OMG!! Happy Birthday Dear customer")
                        time.sleep(2)
                        print("You turned",int(b[0])-int(a[0]),"today. Congratulations!!")
                        time.sleep(2)
                        print("But, we are sorry to inform you that you are not eligible to create an account in this bank...:(")
                        time.sleep(2)
                        print("Thank you for using RSV bank!!")
                        print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                    if (int(b[0])-int(a[0]))>=5 and (int(b[0])-int(a[0]))<=100:
                        i=6
                        d1["date_of_birth"]=date_of_birth
                    if (int(b[0])-int(a[0]))>100 or int(b[0])<int(a[0]):
                        print("HAHA customer very funny please enter a valid Date Of Birth....")
                else:
                    print("Please enter a valid date of birth in the pattern as given above....")
            else:
                print("Please enter a valid date of birth in the pattern as given above....")
        else:
            print("Please enter a valid date of birth in the pattern as given above....")
    bruh=int(b[0])-int(a[0])
    while i==6:
        age=input("Enter your age :")
        if age.isdigit():
            if int(b[1])>int(a[1]):
                if bruh==int(age):
                    i=7
                    d1["age"]=age
                else:
                    print("Please enter a valid age as instructed.......")
            elif int(b[1])==int(a[1]):
                if int(b[2])>=int(a[2]):
                    if bruh==int(age):
                        i=7
                        d1["age"]=age
                    else:
                        print("Please enter a valid age as instructed.......")
                else:
                    if bruh-1==int(age):
                        i=7
                        d1["age"]=age
                    else:
                        print("Please enter a valid age as instructed.......")
            else:
                if bruh-1==int(age):
                    i=7
                    d1["age"]=age
                else:
                    print("Please enter a valid age as instructed.......")
        else:
            print("Please enter a valid age as instructed.......")
    while i==7:
        occupation=input("Enter your Occupation :")
        if occupation.isspace() or len(occupation)==0 or occupation.isdigit():
            print("Dear customer please enter a proper occupation.......")
        else:
            i=8
            d1["occupation"]=occupation
    while i==8:
        qualification=input("Enter your Qualification :")
        if qualification.isspace() or len(qualification)==0 or qualification.isdigit():
            print("Dear customer please enter a proper qualification.......")
        else:
            i=9
            d1["qualification"]=qualification
    while i==9:
        annual_salary=input("Enter your Annual income (in digits) :")
        if annual_salary.isspace() or annual_salary.isalpha() or len(annual_salary)==0:
            print("Dear customer please enter a proper annual salary.......")
        else:
            if annual_salary.isdigit():
                i=10
                d1["annual_salary"]=annual_salary
            else:
                print("Dear customer please enter a proper annual salary without any speacial characters.......")
                
    while i==10:
        office_address=input("Enter your Office Address :")
        if office_address.isspace() or office_address.isdigit() or len(office_address)==0:
            print("Dear customer please enter a proper address.......")
        else:
            i=11
            d1["office_address"]=office_address
    while i==11:
        residential_address=input("Enter your Residential Address :")
        if residential_address.isspace() or residential_address.isdigit() or len(residential_address)==0:
            print("Dear customer please enter a proper address.......")
        else:
            i=12
            d1["residential_address"]=residential_address
    while i==12:
        city=input("Enter the name of your City :")
        if city.isspace() or city.isdigit() or len(city)==0 or len(city)<3:
            print("Dear customer please enter a proper city name.......")
        else:
            i=13
            d1["city"]=city
    while i==13:
        state=input("Enter your State :")
        if state.isspace() or state.isdigit() or len(state)==0 or len(state)<3:
            print("Dear customer please enter a proper state name.......")
        else:
            i=14
            d1["state"]=state
    while i==14:
        pincode=input("Enter your Pincode (in digits) :")
        if pincode.isspace() or pincode.isalpha() or len(pincode)==0:
            print("Dear customer please enter a proper pincode.......")
        else:
            if pincode.isdigit() and len(str(pincode))==6:
                i=15
                d1["pincode"]=pincode
            else:
                print("Dear customer please enter a proper pincode without any speacial characters.......")
    while i==15:
        phone_no=input("Enter your Phone Number (in digits) :")
        if phone_no.isspace() or phone_no.isalpha() or len(phone_no)==0:
            print("Dear customer please enter a proper phone number.......")
        else:
            if phone_no.isdigit() and len(str(phone_no))==10:
                i=16
                d1["phone_no"]=phone_no
            else:
                print("Dear customer please enter a proper phone number without any special characters.......")
    while i==16:
        spouse=input("Enter your spouse name :")
        if spouse.isspace() or spouse.isdigit() or len(spouse)==0:
            print("Dear customer please enter a proper name.......")
        else:
            if spouse.isalnum():
                i=17
                d1["spouse"]=spouse
            else:
                print("Dear customer please enter a proper name without any speacial characters.......")
    print('\n')
    print("Now lets move on to the next phase...:)")
    print("STEP 2: Verification Process.Please enter the following Details carefully as they are used for Verification")
    time.sleep(2)
    print('\n')
    aadhar_no=input("Enter your Aadhar card number :")
    pancard_no=input("Enter your Pancard number :")
    if len(aadhar_no)==12 and aadhar_no.isdigit() and len(pancard_no)==10 and pancard_no.isalnum():
        print('\n')
        print("verified")
        d1["aadhar_no"]=aadhar_no
        d1["pancard_no"]=pancard_no
        f1=open("account_no.txt","a+")
        b=f1.readlines()
        if len(b)==0:
                acc_no=random.randint(10000000,999999999999)
                f1.write(str(acc_no)+"\n")
                f2=open(str(acc_no)+".dat","ab+")
                print('\n')
                print("Wow we have successfully created an account for you",name.upper())
                time.sleep(2)
                print(name.upper(),"your account number is :",acc_no)
        else:
                while(1):
                    acc_no=random.randint(10000000,999999999999)
                    for i in b:
                        if i!=acc_no:
                            pass
                    f1.write(str(acc_no)+"\n")
                    f2=open(str(acc_no)+".dat","ab+")
                    print('\n')
                    print("Wow have successfully created an account for you",name.upper())
                    time.sleep(2)
                    print(name.upper(),"your account number is :",acc_no)        
        d1["account_number"]=str(acc_no)
        f1.close()
        print('\n')
        print("We have successfully completed two phases. Now let us move on to the 3rd phase...:)")
        print("STEP 3:Creation of Password. Follow these rules to have a strong password and to secure your account.")
        time.sleep(3)
        print("\n")
        print("1.Password must have minimum of 8 characters.")
        time.sleep(2)
        print("2.Password should not be a pattern or easy info like names, date of birth etc. (Example 12345678,Roshan etc).")
        time.sleep(2)
        print("3.Password must have special characters like @,# etc.")
        time.sleep(2)
        print("4.Password must have alteast one upper character.")
        time.sleep(2)
        print("5.Password should not have blank spaces.")
        time.sleep(2)
        print("\n")
        print("We guess you are ready with a strong password",name.upper())
        password=input("Enter your password :")
        while(1):
            c=d=e=f=0
            if len(password)>=8:
                c=1
            for i in password:
                if i.isupper():
                    d=1
                if i.isspace():
                    e=1
            for i in password:
                if i.isalnum():
                    pass
                else:
                    f=1
            if e==1:
                print("Rules have been violated")
                password=input("Enter your password :")
            elif c==d==f==1:
                print("Password is Strong")
                break
            else:
                print("Rules have been violated")
                password=input("Enter your password :")
        password_1=input("Re-enter your password :")
        m=0
        while(m<4):
            if password==password_1:
                print("STEP 3 is completed")
                print("Great!! Your password has been created created successfully",name.upper())
                time.sleep(2)
                print("Thank you for using RSV bank!!")
                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                print('\n')
                d1["password"]=password
                d100["new_user"]=d1
                pickle.dump(d100,f2)
                f2.close()
                print('Dear customer Do you want to exit our server or move back to the main page')
                roshan=int(input("1-to exit,2-main page :"))
                if roshan==1:
                    break
                else:
                    main_page()
            if m==4:
                print("Dear customer you have crossed the number of attempts in re-entering the password")
                time.sleep(2)
                print("Your account creation failed...........:(")
                time.sleep(2)
                print("Thank you for using RSV bank!!")
                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                print('\n')
                f2.close()
                print('Dear customer Do you want to exit our server or move back to the main page')
                roshan=int(input("1-to exit,2-main page :"))
                if roshan==1:
                    break
                else:
                    main_page()
            else:
                print("Wrongly Given")
                m+=1
                password_1=input("Re-enter your password :")
    else:
        print("Dear customer the details you have entered are invalid.")
        time.sleep(2)
        print("Your aadhar number and pancard number have not been verified")
        print('\n')
        time.sleep(2)
        print("We are sorry to inform you that your account creation failed.")
        time.sleep(2)
        print('\n')
        print("Thank you for using RSV bank!!")
        time.sleep(2)
        print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
        print('\n')
        print('Dear customer Do you want to exit our server or move back to the main page')
        roshan=int(input("1-to exit,2-main page :"))
        if roshan==1:
            pass
        else:
            main_page()

def already_user():
    l=[]
    global acc_no
    print('\n')
    print("Welcome back dear customer......:)")
    acc_no=int(input("Enter your Account Number :"))
    f1=open("account_no.txt","r")
    a=f1.readlines()
    for i in a:
        d=i.split("\n")
        d.pop()
        for i in d:
            l.append(i)
    n=0
    y=0
    while(n<4):
        if str(acc_no) in l:
            print("Dear customer account number entered has been verified....")
            break
        if n==3:
            print("Dear customer account number has been entered wrong thrice.....")
            print("Hence access is denied........:(")
            print("Thank you for using RSV bank!!")
            print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
            y=1
            print('\n')
            print('Dear customer Do you want to exit our server or move back to the main page')
            roshan=int(input("1-to exit,2-main page :"))
            if roshan==1:
                break
            else:
                main_page()
                break
        else:
            print("Dear customer the account number entered is wrong")
            n+=1
            acc_no=input("Please re-enter your Account Number :")            
    if y!=1:
        f2=open(str(acc_no)+".dat","rb")
        d3=pickle.load(f2)
        d2=d3["new_user"]
        password=input("Now please enter your password :")
        p=0
        z=0
        r=0
        while(p<4):
            if d2["password"]==password:
                print("The password entered is correct")
                h=1
                r=1
            elif p==3:
                print("Dear customer you have entered invalid password multiple times....")
                print("Hence access is denied........:(")
                print("Thank you for using RSV bank!!")
                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                print('\n')
                print('Dear customer Do you want to exit our server or move back to the main page')
                sv=0
                while sv==0:
                    roshan=input("1 - To EXIT, 2 - To move back to Main Page")
                    if roshan=='1' or roshan=='2':
                        sv=1
                    else:
                        print('Dear customer please enter a valid choice.......')
                if roshan==1:
                    pass
                else:
                    main_page()
            elif d2["password"]!=password:
                print("Invalid password")
                pz=0
                while pz==0:
                    forgot=input("Forgot password? (Please enter (yes/no)) :")
                    if forgot.upper()=='YES' or forgot.upper()=='NO':
                        pz=1
                    else:
                        print("Dear customer please enter a valid option")
                if forgot=="yes":
                    print("Dear customer now please answer the following questions if the details match....you can change your password...:)")
                    aadhar_no=int(input("Enter your aadhar number :"))
                    pancard_no=int(input("Enter your pancard number :"))
                    if type(aadhar_no)!=int and type(pancard_no)!= int:
                        print('\n')
                        print("The details entered are invalid...")
                        print("Hence access is denied........:(")
                        print("Thank you for using RSV bank!!")
                        print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                        print('\n')
                        print('Dear customer Do you want to exit our server or move back to the main page')
                        roshan=int(input("1-to exit,2-main page :"))
                        if roshan==1:
                            break
                        else:
                            main_page()
                            break
                    if d2["aadhar_no"]==str(aadhar_no) and d2["pancard_no"]==str(pancard_no):
                        print("Great, the details have matched",name.upper())
                        print("Dear customer as you know the rules of creating a password are :")
                        time.sleep(2)
                        print("\n")
                        print("1.Password must have minimum of 8 characters.")
                        time.sleep(2)
                        print("2.Password should not be a pattern or easy info like names, date of birth etc. (Example 12345678,Roshan etc).")
                        time.sleep(2)
                        print("3.Password must have special characters like @,# etc.")
                        time.sleep(2)
                        print("4.Password must have alteast one upper character.")
                        time.sleep(2)
                        print("5.Password should not have blank spaces.")
                        time.sleep(2)
                        print("\n")
                        password=input("Enter your new password :")
                        while(1):
                            t=d=e=f=0
                            if len(password)>=8:
                                t=1
                            for i in password:
                                if i.isupper():
                                    d=1
                                if i.isspace():
                                    e=1
                            for i in password:
                                if i.isalnum():
                                    pass
                                else:
                                    f=1
                            if e==1:
                                print("Rules have been violated, not a strong password")
                                password=input("Please try again entering a new password :")
                            elif t==d==f==1:
                                print("Password is Strong")
                                break
                            else:
                                print("Rules have been violated, not a strong password")
                                password=input("Enter your password :")
                        password_1=input("Re-enter your new password :")
                        m=0
                        while(m<4):
                            if password==password_1:
                                print("Your password has been updated succesfully",name.upper())
                                f3=open(str(acc_no)+".dat","wb")
                                d2["password"]=password_1
                                pickle.dump(d2,f3)
                                r=3
                                break
                            if m==3:
                                print('\n')
                                print("You have re-entered your new password multiple times")
                                print("Hence access is denied........:(")
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                r=1
                                break
                            else:
                                print("The new password re-entered is wrong...")
                                m+=1
                                password_1=input("Please re-enter your password :")
                    else:
                        print("Dear customer the details you have entered are invalid")
                        print("Change of password unsuccessfull.....:(")
                        print("Hence access is denied........:(")
                        print("Thank you for using RSV bank!!")
                        print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                        r=1
                else:
                    r=2
            if r==2:
                password=input("Enter your password :")
                p+=1
            if r==1:
                break
            if r==3:
                f3.close()
                break
    f1.close()
    f2.close()
    if h==1 and r==1:
        print("Dear customer please choose from the below options....")
        ros=int(input("1-loans,2-funds,3-edit_profile"))
        if ros==1:
            print()
            print()
            def loans(acc_no1):
                global acc_no
                acc_no=acc_no1
                def agro_loan():
                    d1={}
                    d99={}
                    def agri_loan(a):
                        if int(total_income)<250000:
                            loan_given=1000000
                        else:
                            loan_given=5*int(total_income)
                        print('\n')
                        print(name.upper(),"we provide upto",loan_given,"rupees.")
                        time.sleep(2)
                        print("Please provide an appropriate amount within the given limit or else your loan will not be sanctioned :")
                        time.sleep(2)
                        k1=0
                        while k1==0:
                            loanamt=input("Please enter the loan required (in digits, without any special character) :")
                            if loanamt.isdigit() and len(loanamt)!=0:
                                k1=1
                            else:
                                print('Dear customer please enter a valid input...')
                        if int(loanamt)<loan_given:
                            print('\n')
                            time_period=int(input("Enter the term of the loan :"))
                            if int(total_income)<250000:
                                if time_period<=15:
                                    actualprice=int(loanamt)*((1+(a/(12*100)))**time_period)
                                    emi=(actualprice/(12*time_period))
                                    print('\n')
                                    print("Dear customer we are happy to inform you that your agricultural loan of ",loanamt,"has been sanctioned....:)")
                                    time.sleep(3)
                                    print("Your EMI amount is :",emi)
                                    d99["agro_loan"]=d1
                                    f1=open(str(acc_no)+".dat","rb")
                                    sur=pickle.load(f1)
                                    sur.update(d99)
                                    f1.close()
                                    f99=open(str(acc_no)+".dat","wb")
                                    pickle.dump(sur,f99)
                                    f99.close()
                                else:
                                    print('\n')
                                    print("Dear customer the term of loan you have entered is invalid")
                                    time.sleep(1)
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                            else:
                                if time_period<=10:
                                    actualprice=int(loanamt)*((1+(a/(12*100)))**time_period)
                                    emi=(actualprice/(12*time_period))
                                    print('\n')
                                    print("""Dear customer please attach details like id proof, address proof, land ownership deed, collateral, assets info to our mail id (rsvbank@gmail.com)""")
                                    print("Dear customer we are happy to inform you that your agricultural loan of",loanamt,"has been sanctioned")
                                    time.sleep(3)
                                    print("Your EMI amount is :",emi)
                                    d99["agro_loan"]=d1
                                    f1=open(str(acc_no)+".dat","rb")
                                    sur=pickle.load(f1)
                                    sur.update(d99)
                                    f1.close()
                                    f99=open(str(acc_no)+".dat","wb")
                                    pickle.dump(sur,f99)
                                    f99.close()
                                else:
                                    print('\n')
                                    print("Dear customer the term of loan you have entered is invalid")
                                    time.sleep(1)
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                        else:
                            print("We are sorry to inform you that your loan cannot be sanctioned.")
                            time.sleep(1)
                            print("Thank you for using RSV bank!!")
                            print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                            return 1
                    def loan():
                        print('\n')
                        print(name.upper(),"All the details that you have entered till now have been checked and verified")
                        time.sleep(2)
                        print('\n')
                        print("Dear customer now let's move on to the last phase.....")
                        print()
                        print("STEP 3: Purpose and Type of Loan Facility.")
                        print("Following are some schemes given, please choose a scheme based on your requirement.")
                        time.sleep(3)
                        if int(total_income)<=250000:
                            print("\n")
                            print("1. Kisan Credit Card (KCC)/Crop Loans")
                            time.sleep(2)
                            print("Features of this scheme are:")
                            time.sleep(2)
                            print("--> Personal accident insurance cover (to the farmers) valid for 5 years.")
                            time.sleep(2)
                            print("--> The documentation and the details required are a duly-filled application form, ID proof, address proof,declaration of the crops raised.")
                            time.sleep(4)
                            print("--> No collateral is required")
                            time.sleep(2)
                            print("--> The tenure(term) ranges from 3 to 15 years.")
                            time.sleep(2)
                            print("\n")
                            print("2. Agricultural Term Loan")
                            time.sleep(2)
                            print("Features of this scheme are :")
                            time.sleep(2)
                            print("--> Loans upto Rs. 1 lakh without any collateral. The loan ranges from a few thousands to lakhs of rupees.")
                            time.sleep(3)
                            print("--> The tenure(term) ranges from 3 to 15 years.")
                            time.sleep(2)
                            print('1 for Kisan Credit Card (KCC)/Crop Loans')
                            print('2.for Agricultural Term Loan')
                            k2=0
                            while k2==0:
                                choice=input("Please enter the scheme that you want to choose (1 or 2) :")
                                if choice=='1' or choice=='2':
                                    k2=1
                                else:
                                    print('Dear customer please enter a valid option')
                            if choice=="1":
                                print("Dear customer the rate of interest in this scheme is 5 percent compounded monthly")
                                agri_loan(5)
                            elif choice=="2":
                                print("Dear customer the rate of interest in this scheme is 6 percent compounded monthly")
                                agri_loan(6)
                        elif 250000<int(total_income)<=1000000:
                            print("\n")
                            print("1. Agricultural Term Loan")
                            time.sleep(2)
                            print("Features of this scheme are :")
                            time.sleep(2)
                            print("--> Loans upto Rs. 1 lakh without any collateral. The loan ranges from a few thousands to lakhs of rupees.")
                            time.sleep(3)
                            print("--> The tenure(term) ranges from 3 to 15 years.")
                            time.sleep(2)
                            print("\n")
                            print("2. Farm Mechanisation Loan")
                            time.sleep(2)
                            print("Features of this sceme are :")
                            time.sleep(2)
                            print("--> Loans only to farmers who own at least 3 acres of perennially irrigated land.")
                            k2=0
                            while k2==0:
                                choice=input("Please enter the scheme that you want to choose (1 or 2) :")
                                if choice=='1' or choice=='2':
                                    k2=1
                                else:
                                    print('Dear customer please enter a valid option')
                            if choice=="1":
                                print("Dear customer the rate of interest in this scheme is 6 percent compounded monthly")
                                agri_loan(6)
                            elif choice=="2":
                                if int(acres)>=3:
                                    print("Dear customer the rate of interest for these loans is 10 percent compounded monthly")
                                    agri_loan(10)
                                else:
                                    print("Dear customer the land requirement is not satisfied...:(")
                                    time.sleep(1)
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                        elif int(total_income)>1000000:
                            print("\n")
                            print("1. Agricultural Term Loan ")
                            time.sleep(2)
                            print("Features of this scheme are :")
                            time.sleep(2)
                            print("--> Loans upto Rs. 1 lakh without any collateral. The loan ranges from a few thousands to lakhs of rupees.")
                            time.sleep(3)
                            print("--> The tenure(term) ranges from 3 to 15 years.")
                            time.sleep(2)
                            print("\n")
                            print("2. Farm Mechanisation Loan")
                            time.sleep(2)
                            print("Features of this sceme are :")
                            time.sleep(2)
                            print("-->Loans only to farmers who own at least 6 acres of perennially irrigated land.")
                            k2=0
                            while k2==0:
                                choice=input("Please enter the scheme that you want to choose (1 or 2) :")
                                if choice=='1' or choice=='2':
                                    k2=1
                                else:
                                    print('Dear customer please enter a valid option')
                            if choice=="1":
                                print("Dear customer the rate of interest in this scheme is 7 percent compounded monthly")
                                agri_loan(7)
                        elif choice=="2":
                                if int(acres)>=6:
                                    print("Dear customer the rate of interest for these loans is 10.5 percent compounded monthly")
                                    agri_loan(10.5)
                                else:
                                    print("Dear customer the land requirement is not satisfied...:(")
                                    time.sleep(1)
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                    def agri_loan_details():
                        global acres
                        global total_income
                        global name
                        m=0
                        print(ven*50,"RSV AGRICULTURE LOANS")
                        print()
                        print('\n')
                        print("Dear customer welcome to 'RSV AGRICULTURAL LOANS'. A supporting pillar to farmers providing us with our basic necessity...:)")
                        print()
                        time.sleep(1)
                        print("We are very glad to help you. Follow the introductions given below and fill the following details...")
                        time.sleep(2)
                        print('\n')
                        print("STEP 1: Please provide us with the following details. The Details given with utmost care, as wrong or false details may prevent your loan beng sanctioned.")
                        time.sleep(4)
                        i=0
                        while i==0:
                            print('\n')
                            name=input("Enter your Full Name :")
                            if name.isspace() or len(name)==0 or name.isdigit():
                                print("Dear customer please enter a proper name.......")
                            else:
                                i=1
                                d1["name"]=name
                        while i==1:
                            father_name=input("Enter your Father's name :")
                            if father_name.isspace() or len(father_name)==0 or father_name.isdigit():
                                print("Dear customer please enter a proper name.......")
                            else:
                                i=2
                                d1["father_name"]=father_name
                        while i==2:
                            gender=input("Enter your Gender (Male/Female/Others) :")
                            if gender.upper()=="MALE" or gender.upper()=="FEMALE" or gender.upper()=="OTHERS":
                                i=4
                                d1["gender"]=gender
                            else:
                                print("Please enter a valid option Dear Customer....")
                        while i==4:
                            age=input("Enter your age :")
                            if age.isdigit():
                                if int(age)<18 or int(age)>70:
                                    print('\n')
                                    print("Dear customer we are sorry to inform that we cannot provide you this loan as your age is less than 18 or greater than 70...:(")
                                    time.sleep(2)
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                                else:
                                    m=1
                                    i=5
                                    d1["age"]=age
                                    print(name.upper(),"now please provide us with a few more details....")
                                    time.sleep(2)
                            else:
                                print("Please enter a valid age as instructed.......")
                        while i==5:
                                residential_address=input("Enter your Residential Address :")
                                if residential_address.isspace() or residential_address.isdigit() or len(residential_address)==0:
                                    print("Dear customer please enter a proper address.......")
                                else:
                                    i=6
                                    d1["residential_address"]=residential_address
                        while i==6:
                            permanent_address=input("Enter your Permanent Address :")
                            if permanent_address.isspace() or permanent_address.isdigit() or len(permanent_address)==0:
                                print("Dear customer please enter a proper address.......")
                            else:
                                i=7
                                d1["permanent_address"]=permanent_address
                        while i==7:
                            village=input("Enter the name of your village :")
                            if village.isspace() or village.isdigit() or len(village)==0 or len(village)<3:
                                print("Dear customer please enter a proper village name.......")
                            else:
                                i=8
                                d1["village"]=village
                        while i==8:
                            town=input("Enter the name of your town :")
                            if town.isspace() or town.isdigit() or len(town)==0 or len(town)<3:
                                print("Dear customer please enter a proper town name.......")
                            else:
                                i=9
                                d1["town"]=town
                        while i==9:
                            mandal=input("Enter the name of your mandal/taluk :")
                            if mandal.isspace() or mandal.isdigit() or len(mandal)==0 or len(mandal)<3:
                                print("Dear customer please enter a proper mandal/taluk name.......")
                            else:
                                i=10
                                d1["mandal/taluk"]=mandal
                        while i==10:
                            district=input("Enter the name of your district :")
                            if district.isspace() or district.isdigit() or len(district)==0 or len(district)<3:
                                print("Dear customer please enter a proper district name.......")
                            else:
                                i=11
                                d1["district"]=district
                        while i==11:
                            state=input("Enter the name of your state :")
                            if state.isspace() or state.isdigit() or len(state)==0 or len(state)<3:
                                print("Dear customer please enter a proper state name.......")
                            else:
                                i=12
                                d1["state"]=state
                        while i==12:
                            pincode=input("Enter your Pincode (in digits) :")
                            if pincode.isspace() or pincode.isalpha() or len(pincode)==0:
                                print("Dear customer please enter a proper pincode.......")
                            else:
                                if pincode.isdigit() and len(str(pincode))==6:
                                    i=13
                                    d1["pincode"]=pincode
                                else:
                                    print("Dear customer please enter a proper pincode without any speacial characters.......")
                        while i==13:
                            phone_no1=input("Enter your phone/telephone number (in digits) :")
                            if phone_no1.isspace() or phone_no1.isalpha() or len(phone_no1)==0:
                                print("Dear customer please enter a proper phone number.......")
                            else:
                                if phone_no1.isdigit() and len(str(phone_no1))==10:
                                    i=14
                                    d1["phone_no1"]=phone_no1
                                else:
                                    print("Dear customer please enter a proper phone number without any special characters.......")
                        while i==14:
                            phone_no2=input("Enter your alternate phone/telephone number (in digits) :")
                            if phone_no2.isspace() or phone_no2.isalpha() or len(phone_no2)==0:
                                print("Dear customer please enter a proper phone number.......")
                            else:
                                if phone_no2.isdigit() and len(str(phone_no2))==10:
                                    i=16
                                    d1["phone_no2"]=phone_no2
                                else:
                                    print("Dear customer please enter a proper phone number without any special characters.......")
                        while i==16:
                            agricultural_income=input("Enter your annual income through agriculture :")
                            if agricultural_income.isspace() or agricultural_income.isalpha() or len(agricultural_income)==0:
                                print("Dear customer please enter a proper agricultural income.......")
                            else:
                                if agricultural_income.isdigit():
                                    i=17
                                    d1["agricultural_income"]=agricultural_income
                                else:
                                    print("Dear customer please enter a proper agricultural income without any speacial characters.......")
                        while i==17:
                            non_agri_income=input("Do you have any other occupation (other than agriculture)? (yes/no) : ")
                            x=0
                            while x==0:
                                if non_agri_income.upper()=='YES' or non_agri_income.upper()=='NO':
                                    x=1
                                else:
                                    print('Please enter a valid choice')
                            if non_agri_income.upper()=="YES":
                                j=0
                                while j==0:
                                    occupation1=input("Enter your other occupation (other than agriculture) :")
                                    if occupation1.isspace() or len(occupation1)==0 or occupation1.isdigit() or occupation1.upper=='FARMING':
                                        print("Dear customer please enter a proper occupation.......")
                                    else:
                                        j=1
                                        d1["occupation1"]=occupation1
                                while j==1:
                                    other_income=input("Enter your annual income through this occupation :")
                                    if other_income.isspace() or other_income.isalpha() or len(other_income)==0:
                                        print("Dear customer please enter a proper income.......")
                                    else:
                                        if other_income.isdigit():
                                            j=2
                                            i=18
                                            d1["other_income"]=other_income
                                            total_income=int(agricultural_income)+int(other_income)
                                            d1["total_income"]=total_income
                                        else:
                                            print("Dear customer please enter a proper income without any speacial characters.......")    
                            else:
                                i=18
                                other_income=0
                                d1["other_income"]=other_income
                                total_income=int(agricultural_income)+int(other_income)
                                d1["total_income"]=total_income
                        while i==18:
                            acres=input("Dear customer please enter the number of acres of irrigation land you own :")
                            if acres.isdigit():
                                d1["acres"]=acres
                                i=19
                            elif '.' in acres and acres.count('.')==1:
                                a=acres.split('.')
                                for i in a:
                                    if i.isdigit():
                                        pass
                                    else:
                                        print('Dear customer please enter a valid number of acres of irrigation land you own..')
                                else:
                                    i=19
                            else:
                                print('Dear customer please enter a valid number of acres of irrigation land you own..')
                        if m==1:
                            print('\n')
                            print("Dear customer now let's move on to the next phase.....:)")
                            print()
                            time.sleep(1)
                            print("STEP 2: Verification process. Now please provide us with the following details so that we can verify and sanction your loan...")
                            time.sleep(2)
                            print()
                            print("Now you can either provide us with your 'pancard number' or your 'votor's ID'..")
                            print("1 --> for Pancard number")
                            print("2 --> for Voter ID")
                            time.sleep(2)
                            print('\n')
                            ch=0
                            while ch==0:
                                choice=input("Enter your choice (1 or 2) :")
                                if choice=='1' or choice=='2':
                                    ch=1
                                else:
                                    print('Please enter a proper value')
                            print('\n')
                            if choice=='1':
                                b=0
                                pancard_no=input("Enter your Pancard number :")
                                if len(pancard_no)==10 and pancard_no.isalnum():
                                    print('\n')
                                    print("Dear customer the Pancard number you have entered has been verified....")
                                    b=1
                                    d1["pancard_no"]=pancard_no
                                if b==1:
                                    loan()
                                else:
                                    print('\n')
                                    print("Dear customer the Pancard number you have entered is invalid")
                                    print()
                                    time.sleep(1)
                                    print("We are sorry to inform you that your loan cannot be sanctioned.")
                                    print()
                                    time.sleep(1)
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                            elif choice=='2':
                                c=0
                                voters_id=input("Enter your Voter ID :")
                                if len(voters_id)==10:
                                    if voters_id.isalnum():
                                        print('\n')
                                        print("Dear customer the Voter ID you have entered has been verified..")
                                        d1["voters_id"]=voters_id
                                        c=1
                                    if c==1:
                                        loan()

                                    else:
                                        print('\n')
                                        print("Dear customer the Voter ID you have entered is invalid")
                                        print()
                                        time.sleep(1)
                                        print("Thank you for using RSV bank!!")
                                        print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                        return 1
                                else:
                                    print('\n')
                                    print("Dear customer the Voter ID you have entered is invalid")
                                    print()
                                    time.sleep(1)
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                            else:
                                print('\n')
                                print("Dear customer the  Aadhar number you have entered is invalid.")
                                print()
                                time.sleep(1)
                                print("We are sorry to inform you that your loan cannot be sanctioned.")
                                print()
                                time.sleep(1)
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                    agri_loan_details()
                def car_loan():
                    d99={}
                    d1={}
                    m=0
                    print()
                    print()
                    print(ven*40,"RSV CAR LOANS")
                    print()
                    print()
                    print("Dear customer welcome to 'RSV CAR LOANS'. Have your dream car in your garage!!")
                    time.sleep(1)
                    print()
                    print("We are very glad to help you. Follow the introductions given below and fill the following details...")
                    time.sleep(2)
                    print('/n')
                    print("STEP 1: Please provide us with the following details. The details given with utmost care, as wrong or false details may prevent your loan beng sanctioned.")
                    time.sleep(4)
                    i=0
                    while i==0:
                        print('\n')
                        name=input("Enter your Full Name :")
                        if name.isspace() or len(name)==0 or name.isdigit():
                            print("Dear customer please enter a proper name.......")
                        else:
                            i=1
                            d1["name"]=name
                    while i==1:
                        father_name=input("Enter your Father's name :")
                        if father_name.isspace() or len(father_name)==0 or father_name.isdigit():
                            print("Dear customer please enter a proper name.......")
                        else:
                            i=2
                            d1["father_name"]=father_name
                    while i==2:
                        gender=input("Enter your Gender (Male/Female/Others) :")
                        if gender.upper()=="MALE" or gender.upper()=="FEMALE" or gender.upper()=="OTHERS":
                            i=4
                            d1["gender"]=gender
                        else:
                            print("Please enter a valid option Dear Customer....")
                    while i==4:
                        age=input("Enter your age :")
                        if age.isdigit():
                            if int(age)<18 or int(age)>70:
                                print('\n')
                                print("Dear customer we are sorry to inform that we cannot provide you this loan as your age is less than 18 or greater than 70...:(")
                                time.sleep(2)
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                a123=int(input("1-to exit,2-to mainpage"))
                                if a123==2:
                                    main_page()
                                else:
                                    break
                            else:
                                m=1
                                i=5
                                d1["age"]=age
                                print(name.upper(),"now please provide us with a few more details....")
                                time.sleep(2)
                        else:
                            print("Please enter a valid age as instructed.......")
                    while i==5:
                        residential_address=input("Enter your Residential Address :")
                        if residential_address.isspace() or residential_address.isdigit() or len(residential_address)==0:
                            print("Dear customer please enter a proper address.......")
                        else:
                            i=6
                            d1["residential_address"]=residential_address
                    while i==6:
                        permanent_address=input("Enter your Permanent Address :")
                        if permanent_address.isspace() or permanent_address.isdigit() or len(permanent_address)==0:
                            print("Dear customer please enter a proper address.......")
                        else:
                            i=7
                            d1["permanent_address"]=permanent_address
                    while i==7:
                        district=input("Enter the name of your district :")
                        if district.isspace() or district.isdigit() or len(district)==0 or len(district)<3:
                            print("Dear customer please enter a proper district name.......")
                        else:
                            i=8
                            d1["district"]=district
                    while i==8:
                        state=input("Enter the name of your state :")
                        if state.isspace() or state.isdigit() or len(state)==0 or len(state)<3:
                            print("Dear customer please enter a proper state name.......")
                        else:
                            i=9
                            d1["state"]=state
                    while i==9:
                        pincode=input("Enter your Pincode (in digits) :")
                        if pincode.isspace() or pincode.isalpha() or len(pincode)==0:
                            print("Dear customer please enter a proper pincode.......")
                        else:
                            if pincode.isdigit() and len(str(pincode))==6:
                                i=10
                                d1["pincode"]=pincode
                            else:
                                print("Dear customer please enter a proper pincode without any speacial characters.......")
                    while i==10:
                        phone_no1=input("Enter your phone/telephone number (in digits) :")
                        if phone_no1.isspace() or phone_no1.isalpha() or len(phone_no1)==0:
                            print("Dear customer please enter a proper phone number.......")
                        else:
                            if phone_no1.isdigit() and len(str(phone_no1))==10:
                                i=11
                                d1["phone_no1"]=phone_no1
                            else:
                                print("Dear customer please enter a proper phone number without any special characters.......")
                    while i==11:
                        phone_no2=input("Enter your alternate phone/telephone number (in digits) :")
                        if phone_no2.isspace() or phone_no2.isalpha() or len(phone_no2)==0:
                            print("Dear customer please enter a proper phone number.......")
                        else:
                            if phone_no2.isdigit() and len(str(phone_no2))==10:
                                i=13
                                d1["phone_no2"]=phone_no2
                            else:
                                print("Dear customer please enter a proper phone number without any special characters.......")
                    while i==13:
                        income=input("Enter your Annual income (in digits) :")
                        if income.isspace() or income.isalpha() or len(income)==0:
                            print("Dear customer please enter a proper annual salary.......")
                        else:
                            if income.isdigit():
                                i=14
                                d1["annual_salary"]=income
                            else:
                                print("Dear customer please enter a proper annual salary without any speacial characters.......")
                    if m==1:
                        print('\n')
                        print("Dear customer now let's move on to the next phase.....:)")
                        time.sleep(1)
                        print()
                        print("STEP 2: Verification process. Now please provide us with the following details so that we can verify and sanction your loan...")
                        time.sleep(2)
                        print()
                        print("Now you need to provide us with your 'pancard number'")
                        time.sleep(2)
                        print('\n')
                        pancard_no=input("Enter your Pancard number :")
                        if len(pancard_no)==10 and pancard_no.isalnum():
                            print('\n')
                            print("Dear customer the Pancard number you have entered has been verified....")
                        else:
                            print('\n')
                            print("Dear customer the  Pancard number you have entered is invalid.")
                            time.sleep(1)
                            print("We are sorry to inform you that your loan cannot be sanctioned.")
                            time.sleep(1)
                            print()
                            print("Thank you for using RSV bank!!")
                            print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                            return 1
                        print('\n')
                        print("Dear customer now let's move on to the last phase....")
                        time.sleep(1)
                        print()
                        print("Step 3 : More information about the loan")
                        while i==14:
                            term=input("Please enter the term of loan (10 years maximum (in digits)) :")
                            if term.isspace() or term.isalpha() or len(term)==0:
                                print("Dear customer please enter a proper term of loan.....")
                            else:
                                if term.isdigit():
                                    i=15
                                    d1['term']=term
                                else:
                                    print("Dear customer please enter a proper term without any speacial characters.......")
                        if int(term)>10:
                            print('\n')
                            print("Dear costomer the term of loan is high")
                            time.sleep(1)
                            print()
                            print("We are sorry to inform you that your loan cannot be sanctioned")
                            time.sleep(1)
                            print()
                            print("Thank you for using RSV bank!!")
                            print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                            return 1
                        else:
                            loan=(int(income)*int(term))*0.5
                            i1=0
                            while i1==0:
                                print('\n')
                                car=input("Please enter the model of the car :")
                                if car.isspace() or len(car)==0 or car.isdigit():
                                    print("Dear customer please enter a proper name.......")
                                else:
                                    i1=1
                                    d1["car"]=car 
                            print("WOW!!",car.upper(),"?? That is a marvelous choice",name.upper())
                            while i1==1:
                                car_price=input("Please enter the price of your car (in digits) :")
                                if car_price.isspace() or car_price.isalpha() or len(car_price)==0:
                                    print("Dear customer please enter a proper price of the car.....")
                                else:
                                    if car_price.isdigit():
                                        i1=2
                                        d1['car_price']=car_price 
                                    else:
                                        print("Dear customer please enter a proper price of the car without any speacial characters.......")
                            approx=int(car_price)*(0.8)
                            print('\n')
                            print("So",name.upper(),", according to the details you entered.....")
                            time.sleep(1)
                            print("The loan amount that can be maximum provided is :", approx)
                            time.sleep(1)
                            print("Dear customer now its time to enter the loan amount you require")
                            time.sleep(1)
                            print("\n")
                            print("!!NOTE!!   --->   WE only provide loan upto 80 percent of your car's price....")
                            print("\n")
                            time.sleep(4)
                            while i1==2:
                                amount=input("Please enter the loan amount required (in digits) :")
                                if amount.isspace() or amount.isalpha() or len(amount)==0:
                                    print("Dear customer please enter a proper loan amount required.....")
                                else:
                                    if amount.isdigit():
                                        i1=3
                                        d1['amount']=amount
                                    else:
                                        print("Dear customer please enter a proper loan amount required without any speacial characters.......")
                            if int(amount)>approx:
                                print('\n')
                                print("Dear costomer Loan conditions violated......:(")
                                time.sleep(1)
                                print()
                                print("We are sorry to inform you that your loan cannot be sanctioned")
                                time.sleep(1)
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                print('\n')
                                print("Dear customer now its time to talk about the interest rate.......")
                                time.sleep(1)
                                print()
                                print("The rate of interest for car loans is 10 percent compounded monthly....")
                                time.sleep(2)
                                print(name.upper(),"Do you wish to take this loan??")
                                time.sleep(4)
                                while i1==3:
                                    choice=input("Enter yes or no:")
                                    if choice.upper()=='YES' or choice.upper()=='NO':
                                        i1=4
                                    else:
                                        print('Dear customer please enter a valid choice....')
                                if choice.upper()=="YES":
                                    print('\n')
                                    print("Wow that's a wise choice,",name.upper())
                                    time.sleep(1)
                                    print("We are happy to serve you......:)")
                                    amount1=int(amount)*((1+10/(100*12))**int(term))
                                    emi=amount1/(int(term)*12)
                                    print('\n')
                                    print("Dear costomer we are happy to inform you that your car loan of Rs.",amount,"for the term of ",term,"has been sanctioned :)")
                                    time.sleep(2)
                                    print(name.upper(),"your EMI will be :",emi)
                                    time.sleep(1)
                                    d99["car_loan"]=d1
                                    f1=open(str(acc_no)+".dat","rb")
                                    sur=pickle.load(f1)
                                    sur.update(d99)
                                    f1.close()
                                    f99=open(str(acc_no)+".dat","wb")
                                    pickle.dump(sur,f99)
                                    f99.close()
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                                else:
                                    print('\n')
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                            
                def educational_loan():
                    d1={}
                    print()
                    print()
                    print(ven*50,"RSV EDUCATIONAL LOANS")
                    print()
                    print()
                    print("Dear customer welcome to 'RSV EDUCATIONAL LOANS'. Don't let your economic background stop you from studing your desired course. Take loans from our bank at the lowest interest ever!!")
                    print("\n")
                    print(" A person who won’t read has no advantage over one who can’t read. –--> Mark Twain")
                    print("\n")
                    time.sleep(5)
                    print("We are very glad to help you. Follow the introductions given below and fill the following details...")
                    time.sleep(2)
                    print('\n')
                    print("STEP 1: Please provide us with the following details. The Details given with utmost care, as wrong or false details may prevent your loan beng sanctioned.")
                    time.sleep(4)
                    i=0
                    while i==0:
                        print('\n')
                        name=input("Enter your Full Name :")
                        if name.isspace() or len(name)==0 or name.isdigit():
                            print("Dear customer please enter a proper name.......")
                        else:
                            i=1
                            d1["name"]=name
                    while i==1:
                        father_name=input("Enter your Father's name :")
                        if father_name.isspace() or len(father_name)==0 or father_name.isdigit():
                            print("Dear customer please enter a proper name.......")
                        else:
                            i=2
                            d1["father_name"]=father_name
                    while i==2:
                        gender=input("Enter your Gender (Male/Female/Others) :")
                        if gender.upper()=="MALE" or gender.upper()=="FEMALE" or gender.upper()=="OTHERS":
                            i=3
                            d1["gender"]=gender
                        else:
                            print("Please enter a valid option Dear Customer....")
                    while i==3:
                        age=input("Enter your age :")
                        if age.isdigit():
                            if int(age)>30:
                                print('\n')
                                print("Dear customer we are sorry to inform that we cannot provide you this loan as your age is less than 18 or greater than 70...:(")
                                time.sleep(2)
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                i=5
                                d1["age"]=age
                                print("Now please provide us with a few more details....")
                                time.sleep(2)
                        else:
                            print("Please enter a valid age as instructed.......")
                    else:
                        print('\n')
                        print("please choose 1 - If student is applying for educational loan or 2 - If parent/guardian is applying for educational loan")
                        time.sleep(2)
                        j=0
                        while j==0:
                            choice=input("Dear customer now please enter your choice (1 or 2) :")
                            if choice=='1' or choice=='2':
                                j=1
                            else:
                                print('Dear customer please enter a valid choice.....')
                        if choice=="1":
                            print('\n')
                            print("Wow we really appreciate your effort to study!!....")
                            time.sleep(1)
                            print("The interest on educational loan is 6 percent compounded monthly.")
                            print()
                            time.sleep(1)
                            print("And the good news is that you can start repaying your loan (EMI) after the completion of your course....:).")
                            time.sleep(3)
                            edu(6,d1)
                        if choice=="2":
                            print("Dear customer the interest on educational loan is 7 percent compounded monthly.") 
                            time.sleep(2)
                            edu(7,d1)                  
                def edu(z,d1):
                    d99={}
                    j1=0
                    while j1==0:
                        a=input("Dear customer would you like to apply for the loan 'yes' or 'no' :")
                        if a.upper()=='YES' or a.upper()=='NO':
                            j1=1
                        else:
                            print('Dear customer please enter a valid choice.....')
                    if a.upper()=="NO":
                        print('\n')
                        print("Thank you for using RSV bank!!")
                        print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                        return 1
                    else:
                        print('\n')
                        print("That's a great choice")
                        time.sleep(1)
                        print("Dear customer for which graduation are you taking the loan?")
                        time.sleep(1)
                        while j1==1:
                            b=input("Enter UG - if Under graduation or PG - if Post graduation :")
                            if b.upper()=='UG' or b.upper()=='PG':
                                j1=2
                            else:
                                print("Dear customer please enter a valid choice.....")
                        if b.upper()=='UG':
                            d={"engineering":1000000,"medicine":3000000,"art and science":500000,"law":700000,"b.com":500000,"polytechnique":400000,"bba":100000,"others":300000}
                            for i in d:
                                print('\n')
                                print("For",i,"the maximum loan amount that can be sanctioned is :",d[i],"\n")
                            while True:
                                ch=input("Please enter the course that you are opting from the above choices we displayed (enter the choices exactly as given) :")
                                l=[]
                                for i in d:
                                    l.append(i.upper())
                                if ch.upper() not in l:
                                    print("Dear customer please enter a valid course name....")
                                else:
                                    break
                            print('\n')
                            print("Dear customer now let's move on to the next phase.....")
                            print()
                            print('STEP 2 : Information about the college')
                            j2=0
                            while j2==0:
                                college_name=input("Dear customer please enter name of the college/university :")
                                if college_name.isspace() or len(college_name)==0 or college_name.isdigit():
                                    print('Dear customer please enter a valid college name....')
                                else:
                                    j2=1
                                    d1['college_name']=college_name
                            while j2==1:
                                college_code=input("Now please enter the college counselling code :")
                                if college_code.isspace() or college_code.isalpha() or len(college_code)==0:
                                    print("Dear customer please enter a proper college counselling code.....")
                                else:
                                    if college_code.isdigit():
                                        j2=2
                                        d1['college_code']=college_code 
                                    else:
                                        print("Dear customer please enter a proper college counselling code without any speacial characters.......")
                            print('\n')
                            print("So you are opting for ",ch.upper(),"in",college_name,"college/university..")
                            time.sleep(2)
                            print("Now let's move on to the following essentials...")
                            time.sleep(1)
                            while j2==2:
                                co=input("Please enter the branch that you are opting from your major :")
                                if co.isspace() or len(co)==0 or co.isdigit():
                                    print('Dear customer please enter a valid branch that you are opting....')
                                else:
                                    j2=3
                                    d1['branch']=co
                            while j2==3:
                                totalcost=input("Please enter the total fee you have to pay for the course :")
                                if totalcost.isspace() or totalcost.isalpha() or len(totalcost)==0:
                                    print("Dear customer please enter a valid total cost of your course.....")
                                else:
                                    if totalcost.isdigit():
                                        j2=4
                                        d1['total_cost']=totalcost 
                                    else:
                                        print("Dear customer please enter a valid total cost of your course without any speacial characters.......")
                            totalcost=int(totalcost)
                            print("\n")
                            print("Dear customer now let's move on to the last phase....")
                            time.sleep(1)
                            print('STEP 3 : More information about the loan')
                            print()
                            time.sleep(1)
                            print("Please note that loan amount will be sanctioned only when the loan amount is less than or equal to the cost of the course you are opting for.")
                            time.sleep(3)
                            print()
                            print("Any violation of the above condition or any malpractise may cause your loan not to be sanctioned....")
                            j3=0
                            while j3==0:
                                loanamount=input("Please enter the loan you require (in digits) :")
                                if loanamount.isspace() or loanamount.isalpha() or len(loanamount)==0:
                                    print("Dear customer please enter a proper loan amount required.....")
                                else:
                                    if loanamount.isdigit():
                                        j3=1
                                        d1['loan_amount']=loanamount 
                                    else:
                                        print("Dear customer please enter a proper loan amount required without any speacial characters.......")
                            if int(loanamount)<=int(totalcost) and int(loanamount)<=d[ch]:
                                while j3==1:
                                    term=input("Please enter the term of loan (10 years maximum (in digits)) :")
                                    if term.isspace() or term.isalpha() or len(term)==0:
                                        print("Dear customer please enter a proper term of loan.....")
                                    else:
                                        if term.isdigit():
                                            j3=2
                                            d1['term']=term
                                        else:
                                            print("Dear customer please enter a proper term without any speacial characters.......")
                                actualprice=int(loanamount)*(1+(z/(12*100)))**int(term)
                                emi=(actualprice/(12*int(term)))
                                print('\n')
                                print("Dear customer we are happy to inform you that your educational loan of",loanamount,"has been sanctioned..:)")
                                time.sleep(3)
                                print("Your EMI amount is :",emi)
                                time.sleep(1)
                                d99["edu_loan"]=d1
                                f1=open(str(acc_no)+".dat","rb")
                                sur=pickle.load(f1)
                                sur.update(d99)
                                f1.close()
                                f99=open(str(acc_no)+".dat","wb")
                                pickle.dump(sur,f99)
                                f99.close()
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                print('\n')
                                print("Dear customer your loan cannot be sanctioned due to invalid input")
                                time.sleep(2)
                                print()
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                        if b.upper()=='PG':
                            d={"engineering":2000000,"medicine":6000000,"arts and science":1000000,"m.com":1000000,"mba":2000000,"others":1000000}
                            for i in d:
                                print('\n')
                                print("For",i,"the maximum loan amount that can be sanctioned is :",d[i],"\n")
                            while True:
                                ch=input("Please enter the course that you are opting from the above choices we displayed (enter the choices exactly as given):")
                                l=[]
                                for i in d:
                                    l.append(i.upper())
                                if ch.upper() not in l:
                                    print("Dear customer please enter a valid course name....")
                                else:
                                    break
                            print('\n')
                            print("Dear customer now let's move on to the next phase.....")
                            print()
                            print('STEP 2 : Information about the college')
                            j2=0
                            while j2==0:
                                college_name=input("Dear customer please enter name of the college/university :")
                                if college_name.isspace() or len(college_name)==0 or college_name.isdigit():
                                    print('Dear customer please enter a valid college name....')
                                else:
                                    j2=1
                                    d1['college_name']=college_name
                            while j2==1:
                                college_code=int(input("Now please enter the college counselling code :"))
                                if college_code.isspace() or college_code.isalpha() or len(college_code)==0:
                                    print("Dear customer please enter a proper college counselling code.....")
                                else:
                                    if college_code.isdigit():
                                        j2=2
                                        d1['college_code']=college_code 
                                    else:
                                        print("Dear customer please enter a proper college counselling code without any speacial characters.......")
                            print('\n')
                            print("So",name.upper(),"you are opting for ",ch.upper(),"in",college_name,"college/university..")
                            time.sleep(2)
                            print("Now let's move on to the following essentials...")
                            time.sleep(1)
                            while j2==2:
                                co=input("Please enter the branch that you are opting from your major :")
                                if co.isspace() or len(co)==0 or co.isdigit():
                                    print('Dear customer please enter a valid branch that you are opting....')
                                else:
                                    j2=3
                                    d1['branch']=co
                            while j2==3:
                                totalcost=input("Please enter the total fee you have to pay for the course :")
                                if totalcost.isspace() or totalcost.isalpha() or len(totalcost)==0:
                                    print("Dear customer please enter a valid total cost of your course.....")
                                else:
                                    if totalcost.isdigit():
                                        j2=4
                                        d1['total_cost']=totalcost 
                                    else:
                                        print("Dear customer please enter a valid total cost of your course without any speacial characters.......")
                            totalcost=int(totalcost)
                            print("\n")
                            print("Dear customer now let's move on to the last phase....")
                            time.sleep(1)
                            print('STEP 3 : More information about the loan')
                            print()
                            time.sleep(1)
                            print("Please note that loan amount will be sanctioned only when the loan amount is less than or equal to the cost of the course you are opting for.")
                            time.sleep(3)
                            print("Any violation of the above condition or any malpractise may cause your loan not to be sanctioned....")
                            j3=0
                            while j3==0:
                                loanamount=input("Please enter the loan you require (in digits) :")
                                if loanamount.isspace() or loanamount.isalpha() or len(loanamount)==0:
                                    print("Dear customer please enter a proper loan amount required.....")
                                else:
                                    if loanamount.isdigit():
                                        j3=1
                                        d1['loan_amount']=loanamount 
                                    else:
                                        print("Dear customer please enter a proper loan amount required without any speacial characters.......")
                            if loanamount<=totalcost and loanamount<=d[ch]:
                                while j3==1:
                                    term=input("Please enter the term of loan (10 years maximum (in digits)) :")
                                    if term.isspace() or term.isalpha() or len(term)==0:
                                        print("Dear customer please enter a proper term of loan.....")
                                    else:
                                        if term.isdigit():
                                            j3=2
                                            d1['term']=term
                                        else:
                                            print("Dear customer please enter a proper term without any speacial characters.......")
                                actualprice=int(loanamount)*(1+(z/(12*100)))**int(term)
                                emi=(actualprice/(12*int(term)))
                                print('\n')
                                print("Dear customer we are happy to inform you that your educational loan of",loanamount,"has been sanctioned..:)")
                                time.sleep(3)
                                print("Your EMI amount is :",emi)
                                time.sleep(1)
                                d99["edu_loan"]=d1
                                f1=open(str(acc_no)+".dat","rb")
                                sur=pickle.load(f1)
                                sur.update(d99)
                                f1.close()
                                f99=open(str(acc_no)+".dat","wb")
                                pickle.dump(sur,f99)
                                f99.close()
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                print('\n')
                                print("Dear customer your loan cannot be sanctioned due to invalid input")
                                time.sleep(2)
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                def house_loan():
                    d1={}
                    d99={}
                    print()
                    print()
                    print(ven*50,"RSV HOUSE LOANS")
                    print()
                    print()
                    def house(a):
                        houseprice=input("Now please enter the actual cost of the house :")
                        loangiven=(a*int(annual_salary))*(1/2)
                        print(name.upper(),"we can sanction only an amount of",loangiven,"ruppes (calculated by anaysing the details entered).")
                        time.sleep(2)
                        print()
                        print("Please provide an appropriate amount (less than or equal to the amount that we provide) or else your loan will not be sanctioned!!")
                        time.sleep(2)
                        loanamt=int(input("Enter the loan amount :"))
                        if loanamt>loangiven:
                            print("The amount asked is greater than the amount that the bank can provide...:(")
                            print("Unfortunately your loan cannot be sanctioned :")
                            print()
                            print("Thank you for using RSV bank!!")
                            print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                            return 1
                        else:
                            print(name.upper(),"your loan of",loanamt,"has been sanctioned:")
                            actualprice=loanamt*((1+(8/(12*100)))**a)
                            emi=(actualprice/(12*a))
                            print("Dear customer we are happy to inform you that your house loan of ",loanamt,"has been sanctioned")
                            time.sleep(3)
                            print()
                            print(name.upper(),"your EMI is :",emi,"for any further enqiery pls mail our bank (rsvbank@gmail.com)")
                            d99["house_loan"]=d1
                            f1=open(str(acc_no)+".dat","rb")
                            sur=pickle.load(f1)
                            sur.update(d99)
                            f1.close()
                            f99=open(str(acc_no)+".dat","wb")
                            pickle.dump(sur,f99)
                            f99.close()
                            print()
                            print("Thank you for using RSV bank!!")
                            print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                            return 1
                    def houseloan():
                        print("Please provide us with the necesarry details regarding the loan amount you require......")
                        time.sleep(2)
                        print()
                        print("The rate of interest for home loan is 8 percent compounded monthly")
                        time.sleep(2)
                        if int(age)>=50:
                            print("As your age is above 50, the term of the loan will be 10 years (maximum):")
                            t=int(input("Now enter the no of years (term of loan):"))
                            if t>10:
                                print("Sorry customer we don't provide loans of term more than 10 years for people more than 50 years of age :")
                                time.sleep(2)
                                print()
                                print("Your loan cannot be sanctioned")
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                house(t)
                        else:
                            print("The term of the loan will be 20 years (maximum):")
                            t=int(input("Now enter the no of years (term of loan):"))
                            if t>20:
                                print("Sorry customer we don't provide loans of term more than 20 years :")
                                time.sleep(2)
                                print("Your loan cannot be sanctioned")
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                house(t)
                    print('\n')
                    print("Dear customer welcome to 'RSV HOME LOANS'. A dream come true to build your own HOME at the lowest interest rate ever")
                    print("We are very glad to help you. Follow the introductions given below and fill the following details...")
                    time.sleep(2)
                    print('/n')
                    print("STEP 1: Please provide us with the following details. The details given with utmost care, as wrong or false details may prevent your loan beng sanctioned.")
                    time.sleep(4)
                    i=0
                    while i==0:
                        print('\n')
                        name=input("Enter your Full Name :")
                        if name.isspace() or len(name)==0 or name.isdigit():
                            print("Dear customer please enter a proper name.......")
                        else:
                            i=1
                            d1["name"]=name
                    while i==1:
                        father_name=input("Enter your Father's name :")
                        if father_name.isspace() or len(father_name)==0 or father_name.isdigit():
                            print("Dear customer please enter a proper name.......")
                        else:
                            i=2
                            d1["father_name"]=father_name
                    while i==2:
                        gender=input("Enter your Gender (Male/Female/Others) :")
                        if gender.upper()=="MALE" or gender.upper()=="FEMALE" or gender.upper()=="OTHERS":
                            i=4
                            d1["gender"]=gender
                        else:
                            print("Please enter a valid option Dear Customer....")
                    while i==4:
                        age=input("Enter your age :")
                        if age.isdigit():
                            if int(age)<18 or int(age)>70:
                                print('\n')
                                print("Dear customer we are sorry to inform that we cannot provide you this loan as your age is less than 18 or greater than 70...:(")
                                time.sleep(2)
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                i=5
                                d1["age"]=age
                                print(name.upper(),"now please provide us with a few more details....")
                                time.sleep(2)
                        else:
                            print("Please enter a valid age as instructed.......")
                    while i==5:
                        residential_address=input("Enter your Residential Address :")
                        if residential_address.isspace() or residential_address.isdigit() or len(residential_address)==0:
                            print("Dear customer please enter a proper address.......")
                        else:
                            i=6
                            d1["residential_address"]=residential_address
                    while i==6:
                        permanent_address=input("Enter your Permanent Address :")
                        if permanent_address.isspace() or permanent_address.isdigit() or len(permanent_address)==0:
                            print("Dear customer please enter a proper address.......")
                        else:
                            i=7
                            d1["permanent_address"]=permanent_address
                    while i==7:
                        district=input("Enter the name of your district :")
                        if district.isspace() or district.isdigit() or len(district)==0 or len(district)<3:
                            print("Dear customer please enter a proper district name.......")
                        else:
                            i=8
                            d1["district"]=district
                    while i==8:
                        state=input("Enter the name of your state :")
                        if state.isspace() or state.isdigit() or len(state)==0 or len(state)<3:
                            print("Dear customer please enter a proper state name.......")
                        else:
                            i=9
                            d1["state"]=state
                    while i==9:
                        pincode=input("Enter your Pincode (in digits) :")
                        if pincode.isspace() or pincode.isalpha() or len(pincode)==0:
                            print("Dear customer please enter a proper pincode.......")
                        else:
                            if pincode.isdigit() and len(str(pincode))==6:
                                i=10
                                d1["pincode"]=pincode
                            else:
                                print("Dear customer please enter a proper pincode without any speacial characters.......")
                    while i==10:
                        phone_no1=input("Enter your phone/telephone number (in digits) :")
                        if phone_no1.isspace() or phone_no1.isalpha() or len(phone_no1)==0:
                            print("Dear customer please enter a proper phone number.......")
                        else:
                            if phone_no1.isdigit() and len(str(phone_no1))==10:
                                i=11
                                d1["phone_no1"]=phone_no1
                            else:
                                print("Dear customer please enter a proper phone number without any special characters.......")
                    while i==11:
                        phone_no2=input("Enter your alternate phone/telephone number (in digits) :")
                        if phone_no2.isspace() or phone_no2.isalpha() or len(phone_no2)==0:
                            print("Dear customer please enter a proper phone number.......")
                        else:
                            if phone_no2.isdigit() and len(str(phone_no2))==10:
                                i=13
                                d1["phone_no2"]=phone_no2
                            else:
                                print("Dear customer please enter a proper phone number without any special characters.......")
                    while i==13:
                        annual_salary=input("Enter your Annual income (in digits) :")
                        if annual_salary.isspace() or annual_salary.isalpha() or len(annual_salary)==0:
                            print("Dear customer please enter a proper annual salary.......")
                        else:
                            if annual_salary.isdigit():
                                i=14
                                d1["annual_salary"]=annual_salary
                            else:
                                print("Dear customer please enter a proper annual salary without any speacial characters.......")
                    print('\n')
                    time.sleep(1)
                    print("Now please provide us with your bank statement (transactions of past one year) and pay slip (if employee) for verification purposes to rsvbanks@gmail.com")
                    time.sleep(4)
                    houseloan()
                    
                def personal_loan():
                    d1={}
                    d99={}
                    print()
                    print()
                    print(ven*50,"RSV PERSONAL LOANS")
                    print()
                    print()
                    print("Dear customer welcome to 'RSV PERSONAL LOANS'. Take personal loans to develop your life style. Sometimes later means never, so make today like never before. Take personal loans from our bank at the lowest interest rate ever!")
                    time.sleep(4)
                    i=0
                    while i==0:
                        print('\n')
                        name=input("Enter your Full Name :")
                        if name.isspace() or len(name)==0 or name.isdigit():
                            print("Dear customer please enter a proper name.......")
                        else:
                            i=1
                            d1["name"]=name
                    print("Hi",name.upper(),", nice to meet you...")
                    print("Please provide us with the following details....")
                    while i==1:
                        father_name=input("Enter your Father's name :")
                        if father_name.isspace() or len(father_name)==0 or father_name.isdigit():
                            print("Dear customer please enter a proper name.......")
                        else:
                            i=2
                            d1["father_name"]=father_name
                    while i==4:
                        age=input("Enter your age :")
                        if age.isdigit():
                            if int(age)<18 or int(age)>70:
                                    print('\n')
                                    print("Dear customer we are sorry to inform that we cannot provide you this loan as your age is less than 18 or greater than 70...:(")
                                    time.sleep(2)
                                    print("Thank you for using RSV bank!!")
                                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                    return 1
                            else:
                                i=5
                                d1["age"]=age
                                print(name.upper(),"now please provide us with a few more details....")
                                time.sleep(2)
                        else:
                            print("Please enter a valid age as instructed.......")
                    while i==5:
                        residential_address=input("Enter your Residential Address :")
                        if residential_address.isspace() or residential_address.isdigit() or len(residential_address)==0:
                            print("Dear customer please enter a proper address.......")
                        else:
                            i=6
                            d1["residential_address"]=residential_address
                    while i==6:
                        permanent_address=input("Enter your Permanent Address :")
                        if permanent_address.isspace() or permanent_address.isdigit() or len(permanent_address)==0:
                            print("Dear customer please enter a proper address.......")
                        else:
                            i=7
                            d1["permanent_address"]=permanent_address
                    while i==10:
                        phone_no1=input("Enter your phone/telephone number (in digits) :")
                        if phone_no1.isspace() or phone_no1.isalpha() or len(phone_no1)==0:
                            print("Dear customer please enter a proper phone number.......")
                        else:
                            if phone_no1.isdigit() and len(str(phone_no1))==10:
                                i=11
                                d1["phone_no1"]=phone_no1
                            else:
                                print("Dear customer please enter a proper phone number without any special characters.......")
                    while i==11:
                        phone_no2=input("Enter your alternate phone/telephone number (in digits) :")
                        if phone_no2.isspace() or phone_no2.isalpha() or len(phone_no2)==0:
                            print("Dear customer please enter a proper phone number.......")
                        else:
                            if phone_no2.isdigit() and len(str(phone_no2))==10:
                                i=13
                                d1["phone_no2"]=phone_no2
                            else:
                                print("Dear customer please enter a proper phone number without any special characters.......")
                    while i==13:
                        annual_salary=input("Enter your Annual income (in digits) :")
                        if annual_salary.isspace() or annual_salary.isalpha() or len(annual_salary)==0:
                            print("Dear customer please enter a proper annual salary.......")
                        else:
                            if annual_salary.isdigit():
                                i=14
                                d1["annual_salary"]=annual_salary
                            else:
                                print("Dear customer please enter a proper annual salary without any speacial characters.......")
                    print("Now to apply for personal loan, either you have to give us the value and documents of collateral or get a guarantee signature from a person whom you trust to have the collateral or the money that you are taking from the bank")
                    time.sleep(7)
                    print("Dear customer we our bank charges an interest of 14 percent compounded monthly.")
                    choice1=input("Would you like to take our loan? Please enter yes or no:")
                    if choice1=='no':
                        print("That's fine",name.upper(),"hope you come back soon.......:)")
                        print()
                        print("Thank you for using RSV bank!!")
                        print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                        return 1
                    else:
                        print(name.upper(),"That's the right choice")
                        choice=int(input("Now please enter 1-For collateral or 2-For gurantee's signature:"))
                        if choice==1:
                            print(name.upper(),", as you know the rate of interest for personal loan is 14 percent compounded monthly")
                            print("Now please enter the collateral details:")
                            print()
                            time.sleep(2)
                            print("Dear customer we accept documents of house,land,vehicle,gold as collateral")
                            time.sleep(3)
                            print("Now pls provide correct details of your assets as it will be verified by the police and in case of any false information severe action will be taken!!")
                            time.sleep(4)
                            print()
                            house=input("Enter 'yes' if you own a house or land else enter 'no':")
                            if house=='yes':
                                print("Now pls enter the details of the house/s and land/s...")
                                time.sleep(3)
                                housevalue=int(input("Please enter the value of all houses and lands(properties) you own :"))
                            else:
                                housevalue=0
                            vehicle=input("Dear customer please enter 'yes' if you own any vehicle else enter 'no':")
                            if vehicle=='yes':
                                vehiclevalue=int(input("Please enter the value of all vehicle/s you own:"))
                            else:
                                vehiclevalue=0
                            gold=input("Please enter 'yes' if you own gold as ornaments or biscuits and coins else enter 'no':")
                            if gold=='yes':
                                g1=int(input("enter the number of grams of gold owned :"))
                                gvalue=g1*4500
                            else:
                                gvalue=0
                            totalvalue=housevalue+vehiclevalue+gvalue
                            print("Dear customer according to the information given the total worth of your assets is :",totalvalue)
                            time.sleep(2)
                            print()
                            print(name.upper()," you can apply for a maximum of 80 percent of the total value of your assets that is :",(80/100)*totalvalue," at an interest of 14 percent")
                            amtrequired=int(input("Dear customer now please enter the loan amount required :"))
                            if amtrequired<=((80/100)*totalvalue):
                                t=int(input("Dear customer please enter the term of loan (maximum is 10 years):"))
                                actualamount=amtrequired*(1+(14/(12*100)))**t
                                emi=(actualamount/(12*t))
                                print("Dear customer your loan of Rs.",amtrequired,"has been sanctioned successfully :")
                                time.sleep(2)
                                print()
                                print("and the EMI to be paid is :",emi)
                                time.sleep(2)
                                d99["personal_loan"]=d1
                                print()
                                f1=open(str(acc_no)+".dat","ab+")
                                pickle.dump(d99,f1)
                                f1.close()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                print("Sorry customer your loan request has not been sanctioned")
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                        if choice==2:
                            i=0
                            print(name.upper(),", as you know the rate of interest for personal loan is 14 percent compounded monthly")
                            print("Now please enter the details about the gurantee and his networth")
                            time.sleep(3)
                            while i==0:
                                print('\n')
                                gurantor_name=input("Enter the Full Name of gurantee :")
                                if gurantor_name.isspace() or len(gurantor_name)==0 or gurantor_name.isdigit():
                                    print("Dear customer please enter a proper name.......")
                                else:
                                    i=5
                                    d1["gurantor_name"]=gurantor_name
                            while i==5:
                                guranteeadress=input("Enter the adress of the gurantee :")
                                if guranteeadress.isspace() or guranteeadress.isdigit() or len(guranteeadress)==0:
                                    print("Dear customer please enter a proper address.......")
                                else:
                                    i=10
                                    d1["guranteeadress"]=guranteeadress
                            while i==10:
                                guranteevalue=input("Enter the networth of the gurantee :")
                                if guranteevalue.isspace() or guranteevalue.isalpha() or len(guranteevalue)==0:
                                    print("Dear customer please enter a proper value.......")
                                else:
                                    if guranteevalue.isdigit():
                                        i=11
                                        d1["guranteevalue"]=guranteevalue
                                    else:
                                        print("Dear customer please enter a proper phone number without any special characters.......")
                            print("Note that the details of each asset of the gurantee must be sent through email to rsvbank@gmail.com")
                            time.sleep(2)
                            amtrequired1=int(input("Dear customer now please enter the loan amount required :"))
                            if amtrequired1 <=((80/100)*int(guranteevalue)):
                                t1=int(input("Dear customer please enter the term of loan (maximum is 10 years):"))
                                actualamount1=amtrequired1*(1+(14/(12*100)))**t1
                                emi1=(actualamount1/(12*t1))
                                print("Dear customer your loan of Rs.",amtrequired1,"has been sanctioned successfully :")
                                time.sleep(2)
                                print()
                                print("and the EMI to be paid is ",emi1)
                                time.sleep(2)
                                d99["personal_loan"]=d1
                                print()
                                f1=open(str(acc_no)+".dat","ab+")
                                pickle.dump(f1,d99)
                                f1.close()
                                print("Thank you for using RSV bank!! ")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                            else:
                                print("Sorry customer your loan request has not been sanctioned")
                                print()
                                print("Thank you for using RSV bank!!")
                                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                                return 1
                ven=' '
                print()
                print()
                print(ven*50,"RSV LOANS")
                print()
                print()
                print("Hi customer welcome to the loans section of RSV bank...")
                print()
                time.sleep(2)
                print("We provide different loans at respective interest rates which suit everybody....")
                print()
                time.sleep(2)
                print("Please choose a loan that you want to take or the loan about which you want to know about..")
                print()
                time.sleep(5)
                loan_choice=input("""           1 - for AGRICULTURAL LOAN
                       2 - for CAR LOAN
                       3 - for EDUCATIONAL LOAN
                       4 - for HOUSE LOAN
                       5 - for PERSONAL LOAN

                               Now enter your choice :""")
                l69=["1","2","3","4","5"]
                if loan_choice=='1':
                    agro_loan()
                if loan_choice=='2':
                    car_loan()
                if loan_choice=='3':
                    educational_loan()
                if loan_choice=='4':
                    house_loan()
                if loan_choice=='5':
                    personal_loan()
                if loan_choice not in l69:
                    print("Dear customer you have entered a wrong choice...")
                    print()
                    print("Thank you for using RSV bank!!")
                    print()
                    print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
            loans(acc_no)
        if ros==2:
            def fund_transfer(a):
                print()
                print()
                print("RSV FUNDS")
                print()
                print("Welcome to RSV fund transfers")
                time.sleep(2)
                print("Dear customer now......")
                time.sleep(1)
                print("please select from the following options ")
                time.sleep(2)
                print()
                print("""1- Deposit
2- Withdraw
3- Transfer funds
4- Check transaction""")
                choice=int(input("Enter your choice :"))
                if choice==1:
                    l=[]
                    l1=[]                                     
                    f=open("account_no.txt","r")
                    f1=f.readlines()
                    if str(a)+'\n' in f1:
                        f2=open(str(a)+".dat","rb")
                        f33=pickle.load(f2)
                        f3=f33["new_user"]
                        print()
                        b=input("Enter your password :")
                        if b==f3['password']:
                            print("The password entered has been verified........")
                            print()
                            amt=int(input("Dear customer please enter the amount to be deposited :"))
                            bal=f3['bal']
                            bal+=amt
                            print("Dear customer your current balance is :",bal)
                            f4=open(str(a)+".dat","wb")
                            f3['bal']=bal
                            l=f3["deposit"]
                            if len(l)==0:
                                l1.append(str(date.today())+":"+str(amt))
                                f3['deposit']=l1
                                pickle.dump(f33,f4)
                            else:
                                for i in l:
                                    l1.append(i)
                                l1.append(str(date.today())+":"+str(amt))
                                f3['deposit']=l1
                                pickle.dump(f33,f4)
                                f.close()
                                f2.close()
                                f4.close()
                        else:
                            f.close()
                            f2.close()
                            print()
                            print("Dear customer password entered is wrong")
                            print("Acess denied")
                            main_page()
                    else:
                        f.close()
                        print()
                        print("Dear customer the account number entered is wrong")
                        print("Acess denied")
                        main_page()
                    
                if choice==2:
                    l=[]
                    l1=[] 
                    fa=open("account_no.txt","r")
                    f1=fa.readlines()
                    if str(a)+'\n' in f1:
                        print()
                        f2=open(str(a)+".dat","rb")
                        f33=pickle.load(f2)
                        f3=f33["new_user"]
                        b=input("Enter your password :")
                        if b==f3['password']:
                            print("The password entered has been verified........")
                            print()
                            amt=int(input("Dear customer please enter the amount to be withdrawn :"))
                            bal=f3['bal']
                            if bal>=amt:
                                bal-=amt
                                print("Dear customer now you balance is :",bal)
                                f4=open(str(a)+".dat","wb")
                                f3['bal']=bal
                                l=f3["withdraw"]
                                if len(l)==0:
                                    l1.append(str(date.today())+":"+str(amt))
                                    f3['withdraw']=l1
                                    pickle.dump(f33,f4)
                                else:
                                    for i in l:
                                        l1.append(i)
                                    l1.append(str(date.today())+":"+str(amt))
                                    f3['deposit']=l1
                                    pickle.dump(f33,f4)
                                    fa.close()
                                    f2.close()
                                    f4.close()
                            else:
                                fa.close()
                                f2.close()
                                print()
                                print("Dear customer the process has been terminated due to 'Insufficient Balance'")
                        else:
                            fa.close()
                            f2.close()
                            print()
                            print("Dear customer password entered is wrong")
                            print("Acess denied")
                            main_page()
                    else:
                        fa.close()
                        print()
                        print("Dear customer the account number entered is wrong")
                        print("Acess denied")
                        main_page()
                    
                if choice==3:
                    l=[]
                    l1=[]
                    l2=[]
                    l3=[]
                    fb=open("account_no.txt","r")
                    f1=fb.readlines()
                    if str(a)+'\n' in f1:
                        print()
                        f2=open(str(a)+".dat","rb")
                        f33=pickle.load(f2)
                        f3=f33["new_user"]
                        b1=input("Enter your password :")
                        if b1==f3['password']:
                            print("The password entered has been verified........")
                            b=input("Now please enter the account number to which you want to transfer the funds :")
                            if b+'\n' in f1:
                                f4=open(b+".dat","rb")
                                f55=pickle.load(f4)
                                f5=f55["new_user"]
                                print("The account number entered has been verified... ")
                                print()
                                amt=int(input("Enter the amount to be transferred :"))
                                bal=f3['bal']
                                if amt<=bal:
                                    f6=open(str(a)+".dat","wb")
                                    f7=open(b+".dat","wb")
                                    bal1=f5['bal']
                                    bal1+=amt
                                    bal-=amt
                                    f3["bal"]=bal
                                    f5["bal"]=bal1
                                    l=f3["fundtransfer"]
                                    l3=f5["fundtransfer"]
                                    if len(l)==0:
                                        l1.append(str(date.today())+":"+str(amt)+":"+"transferred")
                                        f3['fundtransfer']=l1
                                        pickle.dump(f33,f6)
                                        print("Dear customer you have successfully tansferred",amt,"from",a,"to",b)
                                    if len(l3)==0:
                                        l2.append(str(date.today())+":"+str(amt)+":"+"received")
                                        f5['fundtransfer']=l2
                                        pickle.dump(f55,f7)
                                    if len(l)!=0:
                                        for i in l:
                                            l1.append(i)
                                        l1.append(str(date.today())+":"+str(amt)+":"+"transferred")
                                        f3['fundtransfer']=l1
                                        pickle.dump(f33,f6)
                                        print("Dear customer you have successfully tansferred",amt,"from",a,"to",b)
                                    if len(l3)!=0:
                                        for i in l3:
                                            l2.append(i)
                                        l2.append(str(date.today())+":"+str(amt)+":"+"received")
                                        f5['fundtransfer']=l2
                                        pickle.dump(f55,f7)
                                else:
                                    print()
                                    print("Dear customer the process has been terminated due to 'Insufficient Balance'")
                            else:
                                print()
                                print("Dear customer the account number entered is wrong")
                        else:
                            print()
                            print("Dear customer password entered is wrong")
                            print("Acess denied")
                            main_page()
                    else:
                        fb.close()
                        print()
                        print("Dear customer the account number entered is wrong")
                        print("Acess denied")
                        main_page()
                    fb.close()
                    f2.close()
                    f4.close()
                    f6.close()
                    f7.close()
                if choice==4:
                    fc=open("account_no.txt","r")
                    f1=fc.readlines()
                    if str(a)+'\n' in f1:
                        f2=open(str(a)+".dat","rb")
                        f33=pickle.load(f2)
                        f3=f33["new_user"]
                        b=input("Enter your password")
                        if b==f3['password']:
                            print("The password entered has been verified........")
                            print()
                            print("account_balance:",f3['bal'])
                            print()
                            print("deposit_history:")
                            print()
                            for i in f3["deposit"]:
                                print(i)
                            print()
                            print("withdrawal_history:")
                            print()
                            for i in f3["withdraw"]:
                                print(i)
                            print()
                            print("Transaction history:")
                            print()
                            for i in f3["fundtransfer"]:
                                print(i)
                            print()
                            fc.close()
                            f2.close()
                        else:
                            fc.close()
                            f2.close()
                            print()
                            print("Dear customer password entered is wrong")
                            print("Acess denied")
                            main_page()
                    else:
                        fc.close()
                        print()
                        print("Dear customer the account number entered is wrong")
                        print("Acess denied")
                        main_page()
            fund_transfer(acc_no)
        if ros==3:
            def edit_user(acc_no):
                ven1=['bal','withdraw','deposit','fundtransfer','aadhar_no','pancard_no','account_number','car_loan','agro_loan','edu_loan']
                z1=0
                ven=' '
                while z1==0:
                    print('\n')
                    print(ven*40,"PROFILE",ven*25)
                    print()
                    choice=input("Do You want to edit your profile? (yes/no) :")
                    if choice.upper()=='YES' or choice.upper()=='NO':
                        z1=1
                    else:
                        print("Dear customer please enter a valid choice.......")
                if choice.upper()=="YES":
                    f5=open(str(acc_no)+".dat","rb")
                    bruh1=pickle.load(f5)
                    f6=open(str(acc_no)+".dat","wb")
                    print("Enter the below names in order to update your details (respective names for respective changes in that)")
                    bruh2=bruh1["new_user"]
                    r=0
                    for i in bruh2.keys():
                        print(i)
                        time.sleep(1)
                    while(1):
                        det=input("Enter the required detail :")
                        if det in bruh2.keys():
                            if det in ven1:
                                print("These details cannot be changed or updated")
                                pickle.dump(bruh1,f6)
                                r=1
                            else:
                                detail_edit=input("Enter the updated :")
                                bruh2[det]=detail_edit
                                bruh1["new_user"]=bruh2
                                r=1
                        if r==1:
                            z=0
                            while z==0:
                                choice=input("Do You want to edit another detail (yes/no) :")
                                if choice.upper()=="YES" or choice.upper()=="NO":
                                    z=1
                                else:
                                    print("Dear customer please enter a valid choice")
                            if choice.upper()=="YES":
                                pass
                            if choice.upper()=="NO":
                                pickle.dump(bruh1,f6)
                                break
                        else:
                            print("Dear customer detail you entered is invalid")
                            break
                    f5.close()
                    f6.close()
            edit_user(acc_no)            
        else:
            print("Thank you for using RSV bank!!")
            print("For any further enquiries please mail our bank (rsvbank@gmail.com)")

            print()
            a123=int(input("1-to exit,2-to mainpage"))
            if a123==2:
                main_page()
            else:
                pass
        
def employee():
    c=adda.adda()
    con=m.connect(user="root",passwd=c,host="localhost",database="csc_project")
    if con.is_connected:
        cur=con.cursor()
        query="create table employee (ID bigint(11) primary key,Name varchar(20) not null,age int(3),salary int,post varchar(20) not null)"
        try:
            cur.execute(query)
            print("table craeated successfully")
            l=[[1234567890,"Surya",17,52000,"executive"],[1023456789,"Roshan",20,100000,"general manager"],[9012345678,"Venkat",22,55000,"executive"],[8901234567,"Niruphan",25,15000,"clerk"],[7890123456,"Samson",24,12000,"clerk"],[6789012345,"Suraksha",20,1000000,"ceo"],[5678901234,"Rohit",22,14000,"clerk"],[4567890123,"Ramsurya",20,50000,"executive"]]
            for i in l:
                a,b,c,d,e=i[0],i[1],i[2],i[3],i[4]
                query="insert into employee values({},'{}',{},{},'{}')".format(a,b,c,d,e)
                cur.execute(query)
                con.commit()
            emp_id=int(input("Enter your employee ID :"))
            query1="select id from employee"
            cur.execute(query1)
            d=cur.fetchall()
            print(d)
            l12=[]
            if d!=[]:
                for i in range(len(d)):
                    l12.append(d[i][0])
                    print(l12)
                if emp_id in l12:
                    print("Welcome hope you are doing good...:)")
                    acc_no=int(input("Enter the account number of the customer :"))
                    f1=open("account_no.txt","r")
                    a=f1.readlines()
                    if str(acc_no)+'\n' in a:
                        f2=open(str(acc_no)+".dat","rb")
                        dumb=pickle.load(f2)
                        choice=int(input("Do you want to view all the details or specific details  (enter 1 for all/2 for specifc) :"))
                        if choice==1:
                            for i in dumb:
                                if i in ['password','aadhar_no','pancard_no']:
                                    pass
                                else:
                                    print(i,':',dumb[i])
                            print('\n')
                            con.close()
                            w=1 
                        else:
                            for i in dumb:
                                if i in ['password','aadhar_no','pancard_no']:
                                    pass
                                else:
                                    print(i)
                            while(1):
                                choice1=input("Enter the required detail from the details given above :")
                                if choice1 in dumb.keys():
                                    ez=0
                                    while ez==0:
                                        choice2=input("Do you want to access another detail? (yes/no) :")
                                        if choice2.upper()=='YES' or choice2.upper()=='NO':
                                            ez=1
                                        else:
                                            print("Dear customer please enter a valid choice......")
                                    if choice2.upper()=="YES":
                                        pass
                                    if choice2.upper()=="NO":
                                        print('\n')
                                        con.close()
                                        break
                                else:
                                    print('\n')
                                    print("NO such detail is present..")
                                    print('\n')
                                    con.close()
                                    break
                    else:
                        print("The account number entered is invalid")
                        print('\n')
                        con.close()
                        pass
                else:
                    print("The employee ID entered is invalid")
                    print('\n')
                    con.close()
                    pass
        except:
            emp_id=int(input("Enter your employee ID :"))
            query1="select id from employee"
            cur.execute(query1)
            d=cur.fetchall()
            l12=[]
            if d!=[]:
                for i in range(len(d)):
                    l12.append(d[i][0])
                if emp_id in l12:
                    print("Welcome hope you are doing good...:)")
                    acc_no=int(input("Enter the account number of the customer :"))
                    f1=open("account_no.txt","r")
                    a=f1.readlines()
                    if str(acc_no)+'\n' in a:
                        f2=open(str(acc_no)+".dat","rb")
                        dumb1=pickle.load(f2)
                        dumb=dumb1["new_user"]
                        choice=int(input("Do you want to view all the details or specific details  (enter 1 for all/2 for specifc) :"))
                        if choice==1:
                            for i in dumb:
                                if i in ['password','aadhar_no','pancard_no']:
                                    pass
                                else:
                                    print(i,':',dumb[i])
                            print('\n')
                            con.close()
                            pass
                        else:
                            for i in dumb:
                                if i in ['password','aadhar_no','pancard_no']:
                                    pass
                                else:
                                    print(i)
                            while(1):
                                choice1=input("Enter the required detail from the details given above :")
                                if choice1 in dumb.keys():
                                    print(dumb[choice1])
                                    ez=0
                                    while ez==0:
                                        choice2=input("Do you want to access another detail? (yes/no) :")
                                        if choice2.upper()=='YES' or choice2.upper()=='NO':
                                            ez=1
                                        else:
                                            print("Dear customer please enter a valid choice......")
                                    if choice2.upper()=="YES":
                                        pass
                                    if choice2.upper()=="NO":
                                        print('\n')
                                        con.close()
                                        break
                                else:
                                    print('\n')
                                    print("NO such detail is present..")
                                    print('\n')
                                    con.close()
                                    break
                    else:
                        print("The account number entered is invalid")
                        print('\n')
                        con.close()
                        pass
                else:
                    print("The employee ID entered is invalid")
                    print('\n')
                    con.close()
                    pass
    else:
        print("not connected")
def info():
    print('\n')
    print("Welcome to RSV Bank dear customer. We are here to provide you the best service we can !")
    time.sleep(2)
    print("1 - General terms and conditions for opening bank account")
    time.sleep(2)
    print("2 - Benefits of our bank")
    time.sleep(2)
    print("3 - General information about the loans provided by our bank")
    global s
    global z
    s=0
    z=0
    def asking(s):
        while s==0:
            print('\n')
            global a
            a=input("Dear customer now please enter your choice (1 or 2 or 3 ) :")
            if a=='1' or a=='2' or a=='3':
                s=1
            else:
                print("Dear customer please enter a valid choice......")
    if s==0:
        asking(0)
    while z==0:
        if a=='1':
            print('\n')
            print("The General terms of conditions of our bank are as follows:")
            time.sleep(1)
            print("1) To Open account in our bank you need to provide us with valid address proof")
            time.sleep(1)
            print("2) You should provide your valid aadhar number and pan card number")
            time.sleep(1)
            print("3) You should provide your income tax details and your pay slip if you are a employee")
            time.sleep(1)
            print("4) You should declare about the case (criminal or consumer (if any))")
            time.sleep(1)
            print("5) We will be verifying your personal details and if any suspicious or wrong information given will lead to the")
            print("termination of the whole process")
            time.sleep(1)
            print("6) Interest fixed by the bank will not remain the same and it may vary from year to year")
            time.sleep(1)
            print("7) A minimum balance of 'Rupees 1000' should be there in your account or a fine of Rupees 1.50 will be charged everyday")
            time.sleep(1)
            print("8) Any inappropriate usage of bank websites will lead to legal actions!")
            time.sleep(1)
            a123=int(input("1-to exit,2-to mainpage,3-for features"))
            if a123==2:
                main_page()
                break
            elif a123==3:
                asking(0)
            else:
                print("Thank you for using RSV bank!!")
                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                z=1
                break
        if a=='2':
            print('\n')
            print("Some of the special benifits of our bank are as follows:")
            time.sleep(1)
            print("1) We provide a high interest (upto 7 percent) on savings account ")
            time.sleep(1)
            print("2) We provide 24/7 service throughout the year")
            time.sleep(1)
            print("3) We provide instant fund transfer system ")
            time.sleep(1)
            print("4) We use secured networks having our own firewall which makes it one of the most secured netbanking system")
            time.sleep(1)
            print("5) We give incentive previlages on loans to our customers")
            time.sleep(1)
            a123=int(input("1-to exit,2-to mainpage,3- for features"))
            if a123==2:
                main_page()
                break
            elif a123==3:
                asking(0)
            else:
                print("Thank you for using RSV bank!!")
                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                z=1
                break
        if a=='3':
            print('\n')
            print("We provide the following loans at a low interest possible!")
            time.sleep(1)
            print("1) Agricultural loan")
            print("2) Car loan")
            print("3) House loan")
            print("4) Student loan")
            print("5) Personal loan")
            time.sleep(1)
            print("For further details about the loans please create an acoount in our bank!")
            a123=int(input("1-to exit,2-to mainpage,3- for features"))
            if a123==2:
                main_page()
                break
            elif a123==3:
                asking(0)
            else:
                print("Thank you for using RSV bank!!")
                print("For any further enquiries please mail our bank (rsvbank@gmail.com)")
                z=1
                break
def admin():
    c=adda.adda()
    aa=' '
    print()
    print()
    print(aa*40,"RSV ADMIN")
    print()
    time.sleep(1)
    adminpassword="RSV@123"
    admin1password=input("Please enter admin password:")
    if admin1password==adminpassword:
        print("welcome back ")
        print()
        time.sleep(1)
        print('''1-->Employee details
2-->Add employee
3-->Remove employee
4-->update emplyee info''')
        time.sleep(1)
        while True:
            aa1=input("Enter your choice:")
            if aa1=='1' or aa1=='2' or aa1=='3' or aa1=='4':
                break
            else:
                print("enter a valid option")
        con=m.connect(user='root',passwd=c,host='localhost',database='csc_project')
        if con.is_connected:
            cur=con.cursor()
            if aa1=='1':
                while True:
                    aa2=int(input("enter employee id:"))
                    query100="select id from employee"
                    cur.execute(query100)
                    d100=cur.fetchall()
                    l100=[]
                    for i in range(len(d100)):
                        l100.append(d100[i][0])
                    if int(aa2) in l100:
                        query101="select * from employee where id=({})".format(int(aa2))
                        cur.execute(query101)
                        d101=cur.fetchall()
                        print("employee_id=",d101[0][0],"employee_name=",d101[0][1],"age=",d101[0][2],"salary=",d101[0][3],"post=",d101[0][4])
                        print()
                        aa4=input("do you wish to view another detail y/n:")
                        if aa4=='n' or aa4=='N':
                            break
                    else:
                        print("you have entered invalid id:")
                        aa5=input("do u like to retry y/n:")
                        if aa5=='n' or aa5=='N':
                            break
                roshan=input("do u wish to exit y/n:")
                if roshan=='y':
                    con.close()
                elif roshan=='n':
                    admin()
            if aa1=='2':
                while True:
                    aa3=int(input("enter employee id to be added:"))
                    emp_name=input("enter employee name:")
                    age=int(input("enter employee age :"))
                    salary=int(input("enter employee salary :"))
                    post=input("enter employee post :")
                    query102="select id from employee"
                    cur.execute(query102)
                    d102=cur.fetchall()
                    l102=[]
                    for i in range(len(d102)):
                        l102.append(d102[i])
                    if aa3 not in l102:
                        query103="insert into employee values({},'{}',{},{},'{}')".format(aa3,emp_name,age,salary,post)
                        cur.execute(query103)
                        con.commit()
                        aa7=input("do u like to add one more employee y/n:")
                        if aa7=='n' or aa7=='N':
                            break
                    else:
                        print("employee id already exists:")
                        print()
                        aa6=print("do u like to try again y/n:")
                        if aa6=='n' or aa6=='N':
                            break
                roshan=input("do u wish to exit y/n:")
                if roshan=='y':
                    con.close()
                elif roshan=='n':
                    admin()
            if aa1=='3':
                while True:
                    aa8=int(input("enter employee id to be removed:"))
                    query102="select id from employee"
                    cur.execute(query102)
                    d102=cur.fetchall()
                    l102=[]
                    for i in range(len(d102)):
                        l102.append(d102[i][0])
                    if aa8 in l102:
                        query103="delete from employee where id=({})".format(aa8)
                        cur.execute(query103)
                        con.commit()
                        aa7=input("do u like to remove one more employee y/n:")
                        if aa7=='n' or aa7=='N':
                            break
                    else:
                        print("employee id doesn't exists:")
                        print()
                        aa6=input("do u like to try again y/n:")
                        if aa6=='n' or aa6=='N':
                            break
                roshan=input("do u wish to exit y/n:")
                if roshan=='y':
                    con.close()
                elif roshan=='n':
                    admin()
            if aa1=='4':
                while aa1=='4':
                    aa8=int(input("enter employee id to be updated:"))
                    query102="select id from employee"
                    cur.execute(query102)
                    d102=cur.fetchall()
                    l102=[]
                    for i in range(len(d102)):
                        l102.append(d102[i][0])
                    if aa8 in l102:
                        print("Please enter the value to be updated:")
                        print('''-->name
-->age
-->salary
-->post''')
                        while True:
                            aa9=input("enter the detail name to be updated:")
                            if aa9.upper()=="NAME" or aa9.upper()=="AGE" or aa9.upper()=="SALARY" or aa9.upper()=="POST":
                                aa10=input("enter the updated value:")
                                if aa9.upper()=="NAME":
                                    query="update employee set Name=('{}') where ID=({})".format(aa10,aa8)
                                    cur.execute(query)
                                    con.commit()
                                    aa11=input("do u like to update one more value y/n:") 
                                    if aa11=='n' or aa11=='N':
                                        aa1=0
                                        break
                                elif aa9.upper()=="POST":
                                    query="update employee set post=('{}') where ID=({})".format(aa10,aa8)
                                    cur.execute(query)
                                    con.commit()
                                    aa11=input("do u like to update one more value y/n:") 
                                    if aa11=='n' or aa11=='N':
                                        aa1=0
                                        break
                                elif aa9.upper()=="AGE":
                                    query="update employee set age=({}) where ID=({})".format(aa10,aa8)
                                    cur.execute(query)
                                    con.commit()
                                    aa11=input("do u like to update one more value y/n:")
                                    if aa11=='n' or aa11=='N':
                                        aa1=0
                                        break
                                elif aa9.upper()=="SALARY":
                                    query="update employee set salary=({}) where ID=({})".format(aa10,aa8)
                                    cur.execute(query)
                                    con.commit()
                                    aa11=input("do u like to update one more value y/n:")
                                    if aa11=='n' or aa11=='N':
                                        aa1=0
                                        break
                            else:
                                print("you have entered an invalid option pls try again")
                        
                    else:
                        print("invalid employee id given")
                        aa11=input("would u like to retry y/n:")
                        if aa11=='n' or aa11=='N':
                            aa1=0
                            break
                    roshan=input("do u wish to exit y/n:")
                    if roshan=='y':
                        con.close()
                    elif roshan=='n':
                        admin()
        else:
            print("connection not established")
    else:
        print("Invalid password")
        print("access denied")
main_page()
