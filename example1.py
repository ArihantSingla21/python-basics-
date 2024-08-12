# import time 
# start = time.time()

# for i in range(1,100):
#     print(i)
    
# print(time.time()-start)

## code for implementing the list functionality of python
import sys 
import ctypes

    
class Meralist:
    def __init__(self):
        self.size=1
        self.n=0
        
        self.A = self.__make_array(self.size)
 ## gives us the length of the list we create         
    def __len__(self):
        return self.n
## how we want it to print the list , while we print it 
    def __str__(self):
        result=''
        
        for i in range(self.n):
            result= result + str(self.A[i])+','
            
        return '[' +result[:-1] + ']'    
    ## this helps to append the list 
    def append(self,item):
        if self.size== self.n:
            ## this is a void function which just changes the size of array 
            self.__resize(self.size*2)
        self.A[self.n]=item
        self.n= self.n + 1  
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return "index out of the list "
    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)        
        self.size= new_capacity
        
        for i in range(self.n):
            B[i]=self.A[i]
        ##reassigning the arry to the original array     
        self.A= B    
        
    def pop(self):
        if self.n==0:
            return "the list is empty"
        print(self.A[self.n-1])
        self.n= self.n -1 
        
    def clear(self):
        self.n=0
        self.size=1 
        
    def find(self, value):
        for i in range(self.n):
            if self.A[i] == value:
                return i
        return "ValueError : item not found"  
    
    def insert(self, index , value):
        if self.size== self.n:
            self.__resize(self.size*2)
        for i in range(self.n,index,-1):
          self.A[i]= self.A[i-1]
        self.A[index]=value
        self.n= self.n+1         
        
    def __delitem__(self,index):
        if 0<= index <self.n: 
            for i in range(index, self.n):
                self.A[index]=self.A[index+1]
                
            self.n= self.n - 1    
            
    def remove(self, value):
        pos = self.find(value)
        if type(pos) == int :
            self.__delitem__(pos)
        else:
            return pos       
        
    def sort(self):
        for i in range(0,self.n):
            for j in range(i+1,self.n):
                if(self.A[i]>self.A[j]):
                    temp = self.A[i]
                    self.A[i]=self.A[j]
                    self.A[j]=temp
    def min(self):
        min = float('inf')
        for i in range(self.n):
            if(min>self.A[i]):
                min = self.A[i]
        return min        
                            
                         
              
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)() 
    




if __name__ == "__main__":
    a = Meralist()
    print(a)
    # a.append("arihant")
    # a.append(True)
    a.append(1000)
    a.append(90)
    a.append(89)
    a.append(911)
    a.append(78)
    
    print(len(a))
    print(a)
    a.insert(2,50)
    # del a[100]
    print(a.min())
    a.sort()
    print(a)
    a.remove(911)
    print(a)
    # a.pop()
    # a.pop()
    # a.pop()
    # a.pop()
    
    print(a.find(True))
    a.clear()
    print(a)
    
           