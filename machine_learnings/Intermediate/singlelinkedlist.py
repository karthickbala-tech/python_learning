class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        new_data=node(data)
        if not self.head:
            self.head=new_data
        else:
            last=self.head
            while last.next:
                last= last.next
            last.next=new_data
                            
    
    def print_list(self):
        current= self.head 
        while current:
            print(current.data,end='->')
            current=current.next 
        print('None') 
          
    
l1=linkedlist()
l1.append(10)
l1.append(20)
l1.append(30)

l1.print_list()


