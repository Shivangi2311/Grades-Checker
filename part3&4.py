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
            
        
    
#giving variables values   
p = 0
t = 0
r = 0
e = 0


def credit(p_credit,d_credit,f_credit):
    #Declaring variables as global variables so they can be edited outside the function as well
    global p
    global t
    global r
    global e
    if p_credit + d_credit + f_credit != 120:
        print ("Number of credits do not equal 120")
    elif p_credit == 120:
        print ("Progress")
        p = p + 1
    elif p_credit == 100:
        print ("Progress (module trailer)")
        t = t + 1
    elif f_credit >= 80 :
        print ("Exclude")
        e = e + 1
    else :
        print ("Do not Progress - module retriever")
        r = r + 1





print ("Staff Version with Histogram")
y = 0
q = 0
count = 0
pass_credit()
while (True) :
    count = count + 1
    ask = input("Would you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: ")
    if ask == 'y':
        pass_credit()
    elif ask == 'q':
        break 

print ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def draw(x):
	return "*"*x

print ("Horizontal Histogram")

print (f"Progress {p}: {(draw(p))}")
print (f"Trailer {t}: {(draw(t))}")
print (f"Retriever {r}: {(draw(r))}")
print (f"Excluded {e}: {(draw(e))}")
print ("The total number of outcomes : ",count)

print ("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print ("Vertical Histogram")

#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
#Used the above link as reference for making the vertical histogram
header =  ['Progress|', 'Trailing|', 'Retriever|', 'Exclude']
print ('       '.join(header))
for x in range(max(p,t,r,e)):
    print("{0}                 {1}              {2}              {3}".format(
          '*' if x < p else ' ',
          '*' if x < t else ' ',
          '*' if x < r else ' ',
          '*' if x < e else ' ',
          ))

print ("The total number of outcomes : ",count)

























