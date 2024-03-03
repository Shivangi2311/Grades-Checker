#user-defined function for pass credit
#This contais the process that takes place in pass credit 
def pass_credit():
    while True :
        try:
            #p_credit is pass credit input 
            p_credit = input("Please enter your credits at pass : ")
            p_credit = int(p_credit)
            if p_credit in range (0,140,20):
                defer_credit(p_credit)
                return
            else :
                print ("Out of range")
        except ValueError:
            print ("Integer Required")
            
    

#user-defined function for defer credit
#This contais the process that takes place in defer credit     
def defer_credit(p_credit):
    while True :
        try:
            #d_credit is defer credit input
            d_credit  = input("Please enter your credit at defer : ")
            d_credit = int(d_credit)
            if d_credit in range (0,140,20):
                fail_credit(p_credit,d_credit)
                return
            else :
                print ("Out of range")
        except ValueError:
            print ("Integer Required")
            


#user-defined function for fail credit
#This contais the process that takes place in fail credit 
def fail_credit(p_credit,d_credit):
    while True :
        try:
            #f_credit is fail credit input 
            f_credit = input("Please enter your credit at fail : ")
            f_credit = int(f_credit)
            if f_credit in range (0,140,20):
                credit(p_credit,d_credit,f_credit)
                return
            else :
                print ("Out of range")
        except ValueError:
            print ("Integer Required")
            
        
    
   



def credit(p_credit,d_credit,f_credit):
    if p_credit + d_credit + f_credit != 120:
        print ("Total Incorrect")
    elif p_credit == 120:
        print ("Progress")
    elif p_credit == 100:
        print ("Progress (module trailer)")
    elif f_credit >= 80 :
        print ("Exclude")
    else :
        print ("Do not Progress - module retriever")    





pass_credit()

    


























