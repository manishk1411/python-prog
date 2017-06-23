"""
This program generates some suggested random usernames for the person to create an account online.
"""
import string, datetime, random, sys,re

def create_file(myList):
    filename=datetime.datetime.now()
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","w") as file:
        """#"""
        for i in myList:
            #i = i.sub('["',"], '', i)
            #i.lstrip("'")
            #i.lstrip("[")
            #i.lstrip("]")
            #i.lstrip(",")
            newstr =str(i).replace(",", "")

            newstr1 =str(newstr).replace("'", "")
            newstr2 =str(newstr1).replace(" ", "")
            #newstr = i.replace("", "")
            file.write(newstr2+"\n")
    return filename

def generate(spchar,d,m,y,fname,lname,limit):

    #random.choice(foo)
    myList=[""]
    i=0
    while i<limit:
         from random import shuffle
         l1=random.choice(spchar)
         r1=random.randint(1,6)
         r2=random.randint(1,4)
         numpick=[d,m,y]
         num=random.choice(numpick)
        # print("suggestion Nummber"+str(i+1))
         fname=fname[:r1+1]
         lname=lname[:r2+1]
         total=[l1,num,fname,lname]
         shuffle(total)
         #print(''.join(total))
         myList.append(total)
         i=i+1
    return myList


fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
bday=input("Enter your birthday in ddmmyyyy: ")
limit=int(input("Enter how many suggestions you want: "))
d=bday[:2]
m=bday[2:4]
y=bday[-4:]
print("day is:"+d)
print("month is:"+m)
print("year is is:"+y)
spchar='@$%&.#_'

myList=generate(spchar,d,m,y,fname,lname,limit)
file=create_file(myList)
