n=5
while n>0:
 print(n)
 n=n-1
print("blastoff")

print("\n")

a=27
b=3
c=a*b
print(c)

print("\n")

print(5/2)

print("\n")

#this shows how to use int() or float()
var1="2"
var2=5
var1=int(var1)
var3=var1*var2
print(var3)

print("\n")

#asks what your age is at the bar
a=input("What's your age?")
a=int(a)
if a >= 21:
    print("What would you like to drink?")
if a < 21:
    print("Sorry, I'm unable to serve you.")
    exit()

print("\n")

#this asks what do you like to drink and returns with a statement using your answer
drink=input("What's your poison?")
print("One " + drink + " coming right up!")

print("\n")

#takes input and adds 1 with a statement using your answer
ef = input("What floor are you on in europe? ")
usf = int(ef)+1
print("You would be on floor", usf ,"if you were in the USA.")

print("\n")

#elif example;right now it would print smol \n finished
x=1
if x<2:
    print("smol")
elif x<40:
    print("med")
elif x<48:
    print("wal")
print("finished")

print("\n")

#example of try/except; this will
answer=input("How old are you?")
try :
    answer=int(answer)
    print("Congrats, you are", answer , "years old!")
except :
    print("Please, use numerical digits dummy!")

print("\n")

#def example
def boof():
    print("Boom")
    print("Oof ")
boof()

#max and min function
rattlesnake = max("It's Poisonous.")
rtlsnk = min("It's a smol boy.")
print(rattlesnake)
print(rtlsnk)

#bubble="42"
#float(bubble)
#print(bubble)
#fun = bubble + 32
#print(fun)

largest_so_far = 5
print ("Before", largest_so_far)
for the_num in [2,4,9,10,6,55]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far,the_num)
print ("After" , largest_so_far)

kids = ["Jenna", "Robert", "Mason"]
for kid in kids :
    print("Happy birthday", kid)
print("Now let's sing!")

while True :
    line = input (">" ) 
    if line == "done" :
     break
    print(line)
print("Done")

smallest_so_far = 5
print ("Before", smallest_so_far)
for the_num in [7,4,9,13,3,-12]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far,the_num)
print ("After" , smallest_so_far)

#adding everything
sum=0
print("Before", sum)
for it in [12,36,35] :
    sum = sum + it
    print(sum , it)
print("After", sum)

#finding the average
count=0
sum=0
print (sum,count)
for total in [45,67,90,99,85] :
    count = count + 1
    sum= sum + total
print(sum, count)
float(sum)
average = (sum//count)
print(average)

#filtering
print("Start")
for value in [8,16,24,26] :
    if value >= 10 :
        print("Large # ", value)
print("Done")

#Boolean  
found = False
print(found)
for value in [4,6,8,9,8,2] :
    if value ==2 :
        found=True
        print( found, value)
print(found)

#this is taking forever!!!

smallest_so_far = None
print("Start")
for value in [9, 41, 12, 3, 74,15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    print (smallest_so_far, value)
print("End", smallest_so_far)

word = "super-duper"
print(word)
count = 0
for letter in word :
    if letter == "e" :
        count = count +1
print("This word has" , count , " e's inside of it!")
  
line="Please kiss my dear aunt sally."
print(line.startswith("P"))

data="skyefi21@gmail.com"
atpos=data.find("@")
print(atpos)
cpos=data.find("C",atpos)
print(cpos)

Tasks = [2,89,5,6,20,35]
print(Tasks)
Tasks[2]= 7
print(Tasks)
print(len(Tasks))

#concantenating lists
a = [15,62,33]
b = [16,63,34]
c = a + b
print(c)

#slicing lists
#t = [9,8,7,32,19]
#t = [0:2]
#print(t)

#create empty list and mess with it
Watched = list()
Watched.append("Say I Love you")
Watched.append("Gundam Iron Blooded Orphans")
Watched.append("No Game No Life")
print(Watched)
Watched.remove("No Game No Life")
Watched.append("Sword Art Online")
Watched.append(7)
print(Watched)
#if 7 in Watched:
    #print("That's a number in your anime list.")
#Watched.sort()
#print(Watched)

counter = dict()
candy = ["M&M","Kit-Kat","M&M","Reese's Peanut Butter Cups","Jolly Rancher"]
for amount in candy :
    candy[amount] = candy.get(amount,0) + 1
print(counter)
