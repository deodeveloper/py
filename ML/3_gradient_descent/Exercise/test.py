 #Singleton Borg pattern 
class Borg: 
  
    # state shared by each instance 
    __shared_state = dict()
    _first_initialization = True
    def getT(self):
        print("getT")
        return "tn"
    # constructor method 
    def __init__(self): 
        self.__dict__ = self.__shared_state 
        self.state = 'GeeksforGeeks'
        if(Borg._first_initialization):
            self.tenant= 'tn'
            Borg._first_initialization = False
  
    def __str__(self): 
  
        return self.state 
    

  
# main method 
if __name__ == "__main__": 
  
    person1 = Borg()    # object of class Borg 
    print(person1.tenant)
    person1.tenant="newt"
    person2 = Borg()    # object of class Borg 
    person3 = Borg()    # object of class Borg 
    
    print(person2.tenant)
  
    person1.state = 'DataStructures' # person1 changed the state 
    person2.state = 'Algorithms'     # person2 changed the state 
  
    print(person1)    # output --> Algorithms 
    print(person2)    # output --> Algorithms 
  
    person3.state = 'Geeks'  # person3 changed the 
                         # the shared state 
  
    print(person1)    # output --> Geeks 
    print(person2)    # output --> Geeks 
    print(person3)    # output --> Geeks 