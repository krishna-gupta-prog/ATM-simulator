bank={
    9823648647254678:9886.34,
    8936209756732974:786.0,
    2672678675431874:97867.6
}
user=int(input("Enter your account number ->           "))
if user in bank:
    print(bank[user],"is your balance.")
    work=str(input("What do you want to do, DEPOSITE or WITHDRAW ?                  "))


    work1="withdraw"
    work2="deposite"



    if(work.casefold()==work1.casefold()):
        am_w=float(input("How much do you want to withdraw ?                 "))
        if(am_w<= bank[user]):
        

            neww=bank[user]-am_w,
            print("Your new account balance is ",neww),
            bank[user]=[neww]
        else:
            print("NO SUFFICIENT BALANCE.        ")

    elif(work.casefold()==work2.casefold()):
        am_d=float(input("How much do you want to deposite ?                "))
        newd=bank[user]+am_d
        print("Your new balance is ",newd)
        bank[user]=[newd]
    else:
        print("COMMAND IS NOT RECOGNIZED.")
else:
    print("ACCOUNT NOT FOUND")