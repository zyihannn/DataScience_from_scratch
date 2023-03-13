from typing import List 
import numpy as np
import random 
import tqdm 

Vector = List[float]

# simple linear regression 
def predict(alpha:float, beta:float, x_i:float)->float:
    return beta*x_i + alpha 


def error(alpha:float, beta:float, x_i:float,y_i = float) ->float:
    return (predict(alpha,beta,x_i)-y_i)
    


#### definition of R-square ####
 # R square : measures the fraction of the total variation in the dependent variable that is 
 #captured by the model 

#say, y,x,y_predict 
def total_sum_of_squares(x:Vector, y:Vector)->float:
    y_mean = np.mean(y)
    return np.sum([(y_i-y_mean)**2 for y_i in y])

def sum_of_sqerrors(alpha:float,beta:float, x:Vector, y:Vector): 
    error_arr = np.array([error(alpha, beta, x_i, y_i) for x_i,y_i in zip(x,y)])
    return np.sum(error_arr**2)

def calc_r_sqr(alpha:float, beta:float, x:Vector,y:Vector):  
    return 1- sum_of_sqerrors(alpha, beta, x,y)/total_sum_of_squares(x,y)

#### using gradient descent to calculate the least squared solution ####
#recap: mean sqr error  = sum[(y_i - (beta*x_i + alpha))**2]/N
        #first derivative wrt alpha : 2*((beta*x_i+alpha)-y_i)*(1) -> 2*error -> sum(2*error)/N
        #first derivative wrt beta : 2*((beta*x_i+alpha)-y_i)*(x_i) -> sum(2*error*(x_i))/N

def mean_sqr_error_gradient(theta:Vector,x:Vector, y:Vector) -> Vector:
    alpha = theta[0]
    beta  = theta[1]
    assert len(x) == len(y), 'x vector and y vector must have same length'
    N=len(x)
    dy_d_alpha  = np.sum([2*error(alpha,beta,x_i,y_i) for x_i, y_i in zip(x,y)])/N
    dy_d_beta =  np.sum([2*error(alpha,beta,x_i,y_i)*x_i for x_i, y_i in zip(x,y)])/N
    
    return np.array([dy_d_alpha, dy_d_beta])
    


x = np.array((range(-50,50)))
y = 20*x+5
# theta : start from a random point 
theta = [random.uniform(-1,1), random.uniform(-1,1)]
learning_rate = -0.001
# theta + learning_rate*gradient
print(f'intial theta value is : {theta}')

for _ in range(0,5000):
    grad = mean_sqr_error_gradient(theta,x,y)
    theta = theta + learning_rate*grad
    

assert np.isclose(theta[0], 5,0.01), 'alpha is wrong'
assert np.isclose(theta[1],20,0.01), 'beta is wrong'
    



    
        

