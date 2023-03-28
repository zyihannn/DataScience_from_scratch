import sys 

#iterator 
x = [1,2,3,4,5,6,7,8,9,10] 

for element in x: #here you stored all numbers in x 
    print(x) 

for i in range(1,11):
    print(i)

print(sys.getsizeof(x))
print(sys.getsizeof(range(1,11)))


# how iterator works ? 
y = [1,2,3,4,5,6,7,8,9,10] 

z = map(lambda i : i**2, y) #z is an interator object 

print(next(z))
print(next(z))
print(next(z))
print(next(z))
print('loop starts')
for i in z:
    print(i)

#print(next(y))   #this will error out cuz list is not an iterator 

# the for loop above is essentially equal to : 
while True:
    try: 
        value = next(z)
    except StopIteration:
        print('Done')
        break 



x  = range(1,11)
print(x)