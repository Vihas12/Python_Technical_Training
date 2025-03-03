import time
class Tower:
    def __init__(self):
        print("Welcome to the Tower of Hanoi\n\n")
        print("Given Problem A=[3,2,1]      B=[]      C=[]")
        print("Expected Output A=[]     B=[]        C=[3,2,1]")
        self.A=[]
        self.B=[]
        self.C=[]
    
    # def pass2(self):
    #     self.temp = self.A.pop(1)
    #     self.B.append(self.temp)
    #     time.sleep(3)
    #     print("A=",self.A ," ","B=",self.B," ","C=",self.C)
        
    def Apush(self,value):
        self.A.append(value)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B," ","C=",self.C)
    
    def Bpush(self,value):
        self.B.append(value)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B," ","C=",self.C)
    
    def Cpush(self,value):
        self.C.append(value)
        time.sleep(3)
        print("A=",self.A ," ","B=",self.B," ","C=",self.C)
    
    def Apop(self):
        return self.A.pop(-1)
    
    def Bpop(self):
        return self.B.pop(-1)
    
    def Cpop(self):
        return self.C.pop(-1)
        
obj = Tower()
obj.A = [3,2,1]
obj.Cpush(obj.Apop())
obj.Bpush(obj.Apop())
obj.Bpush(obj.Cpop())
obj.Cpush(obj.Apop())
obj.Apush(obj.Bpop())
obj.Cpush(obj.Bpop())
obj.Cpush(obj.Apop())
        