

class node:
    def __init__(self,value):
        self.data = value 
        self.next = None
    # def __str__(self) :
    #     return str(self.data)    
class linkedlist:
    def __init__(self):
        self.head=None
        self.n=0
        
    def __len__(self):
        return self.n        
    
    def insert_head(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head= new_node
        
if __name__ == "__main__":
   a = linkedlist()
   a.insert_head(12)
   print(len(a))