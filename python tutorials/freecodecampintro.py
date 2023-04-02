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