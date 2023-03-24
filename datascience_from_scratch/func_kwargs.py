import numpy as np

### example 1 
def func1(array:list, k =1 , method ='IQR'):
    print(f'value of k is {k}')
    print(f'method is {method}')
    return np.array(array) + k*2

def wrapper_func(array:list, func, batch_size =3,**kwargs):
    
    grab_array=[]
    for index in range(0,len(array),batch_size):
        sub_array = array[index: (index+batch_size)]
        processed_array  = func(np.array(sub_array),**kwargs)
        grab_array =  grab_array + list(processed_array)
    return grab_array





### example 2
def func1(arg1,arg2,arg3):
    print(arg1,arg2,arg3)

def func2(arg1=None, arg2=None, arg3= None):
    print(arg1, arg2 , arg3)

args = [2,2,3]
func1(args)
func1(*args)

kwargs = {"arg2":2 ,"arg1":1, "arg3":3}
func2(*kwargs) # passing the keys of the dict as positional arguments in func2 
func2(**kwargs) # passing the keys and values to func2 as key word arguments  

if __name__ =="__main__":
    long_arr = [1,2,3,4,5,6,7,8,2]
    res = wrapper_func(long_arr,func1,batch_size=3, k=6,method ='haha')
    print(res)