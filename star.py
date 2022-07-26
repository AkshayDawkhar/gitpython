
class aq:
    colori=12
   
    def __init__(self,name,value,color) -> None:
        self.name=name
        self.color=color
        self.value=value
    
    def fullname(self):
        return self.name+str(aq.colori)
    @classmethod
    def go(cls,name,v,c):
        name1,value,color=name,c,v
        return cls(name1,value,color)
class aq1:
    colori=12
   
    def __init__(self,name,value,color) -> None:
        self.name=name
        self.color=color
        self.value=value
    
    def fullname(self):
        return self.name+str(aq1.colori)
    @classmethod
    def go(cls,name,v,c):
        name1,value,color=name,c,v
        return cls(name1,value,color)

class aqq(aq,aq1):
    colori=112
    def __init__(self, name, value, color,plang):
        super().__init__(name, value, color)
        self.plang= plang

a1=aq('akshay',1,2)
a2=aq('anish',1,2)
a2.colori=23

print(a1.__dict__['color'])
print(a1.fullname())
print(a2.fullname())

aqq1=aqq('omkar',23,24,42)
print()