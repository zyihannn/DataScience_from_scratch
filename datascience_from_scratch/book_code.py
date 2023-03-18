from typing import List
import numpy as np 

Vector = List[float]

def predict(x:Vector, beta:Vector)->float:
    return np.dot(x,beta)
def error(x:Vector, y:float, beta:Vector) ->float:
    return predict(x,beta) - y

def sqerror_gradient(x:Vector, y:float,beta:Vector) ->Vector:
    err =  error(x,y,beta)
    return [2*err*x_i for x_i in x]

import random

def least_squares_fit(xs:List[Vector],
                      ys:List[float],
                      learning_rate:float=0.001,
                      num_steps:int =100,
                      batch_size: int =1) ->Vector:
    
    guess = [random.random() for _ in xs[0]]

    for  _ in range(0,num_steps):
        for start in range(0,len(xs),batch_size):
            batch_xs =xs[start:start+batch_size]
            batch_ys = ys[start:start+batch_size]
            #print([sqerror_gradient(x,y,guess) for x,y in zip(batch_xs,batch_ys)])
            gradient = np.mean([sqerror_gradient(x,y,guess) for x,y in zip(batch_xs,batch_ys)],axis=0)
  
            guess = guess + gradient*(-learning_rate)

    return guess 

# k = 5 # length of xi
# m = 10 # number of x in X
# X=[]
# for _ in range(0,10):
#     X.append([1 for _ in range(0, k)])

# beta_actual = [1,2,3,4,5]
# Y= np.dot(X,beta_actual)

# hh= least_squares_fit(X,Y,batch_size =1)
# print(hh)
#from scratch.statistics import daily_minutes_good
#from scratch.gradient_descent import gradient_step
import scratch
print(dir(scratch))
#ramdon_seed(0)
