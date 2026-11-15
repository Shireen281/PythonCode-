for i in range (10,0):
    print(i)

t = int(input ("enter a number"))
y = 0

for i in range(0,t,5):
    y = y+i
print (y)

y = 0
x = 0
for i in range (0,10,5 ):
   if i % 2 == 0:
        y = y+1
       x = x+1  

print("even numbers are:",y)
print("odd numbers are:",x)

