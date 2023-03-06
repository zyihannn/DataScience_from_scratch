import numpy as np
from typing import List 
import random

# multiple linear regression:
#y_i
#coefficient -> beta = [alpha, beta_1,beta_2 .... beta_k]
# x_i = [1, x_i1,  x_i2, ..... x_ik]
# y_i = beta * x_i (dot product)

# [ x,x,x,x,..x      [ alpha,        [ y 
#   x,x,x,x,..x,  *    beta_1,    =    y 
#   x,x,x,x,..x          ...          ..
#   ....]              beta_k ]        y ]

Vector = List[float]

#### fitting : using gradient descend to find out least sqare errors 
def squared_error(x: Vector, y : float, beta: Vector) -> float:
    return (np.dot(beta,x)-y)**2 #this is just for one x, one y 

#for entire data set:
def sum_squared_error(X:List[Vector], Y:Vector, beta:Vector) -> float:
    return np.sum([squared_error(x, y , beta) for x, y in zip(X,Y)])

#calculate gradient of sum of square error 
def grad_sum_squared_error(X:List[Vector], Y:Vector, beta:Vector) -> float: 
    #error =  np.dot(beta,x) - y 
    #sqr_error  = (error)**2
    #grad_wrt_beta = np.dot((2*error) ,x)
    
    grad_list= [np.dot(2*(np.dot(beta,x) -y),x) for x, y in zip(X,Y)]
    arr_add = np.array([0]*len(X[0]))

    for grad_arr in grad_list:
        arr_add = arr_add + grad_arr

        
    return arr_add

####gradient descend 
# make a fake dataset with perfect fit:
k = 5 # length of xi
m = 10 # number of x in X
X=[]
for _ in range(0,10):
    X.append([random.uniform(-50,50) for _ in range(0, k)])

beta_actual = [1,2,3,4,5]
Y= np.dot(X,beta_actual)

print(X)
print(Y)
assert(False)




#start point  :
beta = [random.random() for _ in range(k)]
print(f'initial guess for beta is : {beta} ')
learning_rate = -0.001
attemps = 100

for _ in range(0,attemps):
    grad = grad_sum_squared_error(X, Y, beta)
    beta = np.array(beta) + grad*learning_rate
    print(beta)











