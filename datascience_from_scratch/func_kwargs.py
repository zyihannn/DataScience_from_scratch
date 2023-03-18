import numpy as np

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

if __name__ =="__main__":
    long_arr = [1,2,3,4,5,6,7,8,2]
    res = wrapper_func(long_arr,func1,batch_size=3, k=6,method ='haha')
    print(res)