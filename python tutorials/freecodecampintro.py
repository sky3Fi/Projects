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
x=input("What's your age?")
x=int(x)
if x >= 21:
    print("What would you like to drink?")
if x < 21:
    print("Sorry, I'm unable to serve you.")
    exit()

print("\n")

#this asks what do you like to drink and returns with a statement using your answer
drink=input("What's your poison?")
print("One " + drink + " coming right up!")

print("\n")

#takes input and adds 1 with a statement using your answer
ef=input("What floor are you on in europe? ")
usf=int(ef)+1
print("You would be on floor",usf,"if you were in the USA.")

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

bubble="42"
type(bubble)
float(bubble)
print(bubble)
fun = bubble + 32
print(fun)

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
        print(found,value)
        break
        found=True
    
print(found)

#this is taking forever!!!
  