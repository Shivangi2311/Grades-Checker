#giving variables values
p = 0
r = 0
t = 0
e = 0
total = 0
def data():
    #Declaring variables as global variables so they can be edited outside the function as well
    global p
    global t
    global r
    global e
    global total 
    
    credit = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,40],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]
    if (credit [0] [0]) == 120:
        print ("Progress")
        p = p + 1
    if (credit [1] [0]) == 100:
        print ("Progress (module trailer)")
        t = t + 1
    if (credit [2] [0]) == 100:
        print ("Progress (module trailer)")
        t = t + 1
    if (credit [3] [0]) == 80:
        print ("Do not Progress - module retriever")
        r = r + 1
    if (credit [4] [0]) == 60:
        print ("Do not Progress - module retriever")
        r = r + 1
    if (credit [5] [0]) == 40:
        print ("Do not Progress - module retriever")
        r = r + 1
    if (credit [6] [0]) == 20:
        print ("Do not Progress - module retriever")
        r = r + 1
    if (credit [7] [0]) == 20:
        print ("Exclude")
        e = e + 1
    if (credit [8] [0]) == 20:
        print ("Exclude")
        e = e + 1
    if (credit [9] [0]) == 0:
        print ("Exclude")
        e = e + 1
    total = p + r + t + e

    
data()    

def draw(x):
	return "*"*x
print ()
print()
#Histogram
print (f"Progress {p}: {(draw(p))}")
print (f"Trailer {t}: {(draw(t))}")
print (f"Retriver {r}: {(draw(r))}")
print (f"Excluded {e}: {(draw(e))}")
print()
print()
print (total,"Outcomes in total ")


