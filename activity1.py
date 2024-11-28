mc=str(input("do you have medical clearance?"))
att=int(input("what is your attendance?"))
if mc=="yes":
    print("they have medical clearance")
    if att>=75:
        print("you are allowed for the exam")
    else:
         print("you are not allowed")
else:
    print ("you dont have the medical clearance")
    
    


