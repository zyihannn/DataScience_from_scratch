import numpy as np
from typing import List 
import random

# multiple linear regression:
#y_i =  alpha + beta1xi1 +beta2*xi2  .... +betak*xik
#coefficient -> beta = [alpha, beta_1,beta_2 .... beta_k]
# x_i = [1, x_i1,  x_i2, ..... x_ik]
# y_i = beta * x_i (dot product)

# [ 1, x,x,x,x,..x      [ alpha,        [ y1 
#   1, x,x,x,x,..x,  *    beta_1,    =    y2 
#   1, x,x,x,x,..x          ...          ..
#   1, ....]              beta_k ]        yk ]

Vector = List[float]

#### fitting : using gradient descend to find out least sqare errors 
def error(x: Vector, y : float, beta: Vector) -> float:
    return (np.dot(beta,x)-y) #note: this is just for one vector x, one float y
# considering the entire dataset , the error array is :
# [error1,
#  error2,
#  ....
#  error k]
x= [1,2,3]
beta=[1,1,1]
y=10
assert error(x,y,beta)==-4 


def sum_of_sqerr(X:List[Vector],Y:Vector, beta:Vector)->float:
    return  np.sum(np.array([(error(x,y,beta))**2 for x,y in zip(X,Y)]))

X=[[1,2,3],[1,2,3]]
Y=[10,10]
bet=[1,1,1]
assert sum_of_sqerr(X,Y,beta)==32

#for entire data set:
#calculate gradient of sum of square error 
def grad_sum_squared_error(X:List[Vector], Y:Vector, beta:Vector) -> Vector: 
    #error_i =  np.dot(beta,x) - y 
    #sqr_error_i  = [np.dot(beta,x) - y ]**2
    #grad_sum_sqrerror_wrt_beta1 = 2*[np.dot(beta,x11) - y1] * x11 + 2*[np.dot(beta,x21) - y1] * x21  + ... = 2*error1*x11 +2*error2*x21+...

    grad_matrix= [ 2*error(x,y,beta)*np.array(x) for x, y in zip(X,Y)]
    arr_add = np.array([0]*len(grad_matrix[0]))
    for index, lst_i in enumerate(grad_matrix):
        arr_add = arr_add + np.array(lst_i)

    return arr_add

####gradient descend 
# make a fake dataset with perfect fit:
k = 5 # length of xi
m = 10 # number of x in X
X=[]
for _ in range(0,m):
    X.append([random.randint(-10,10) for _ in range(0,k)])

beta_actual = [1,2,2,4,5]
Y= np.dot(X,beta_actual)

assert np.isclose(sum_of_sqerr(X,Y,beta_actual),0)

#starting point  :
beta = [random.random() for _ in range(k)]
print(f'initial guess for beta is : {beta} ')

learning_rate = -0.001
attemps = 1000

for _ in range(0,attemps):
    grad = grad_sum_squared_error(X, Y, beta)
    sqr_err = sum_of_sqerr(X,Y,beta)
    print(f'sum of err is :{sqr_err}')
    beta = np.array(beta) + grad*learning_rate

print(beta)











