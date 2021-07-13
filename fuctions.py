
class frist1:
    def __init__(self,inputcode):
        self.inputcode = inputcode
        

    def frist(self):
        self.inputcode=self.inputcode.replace('૦','0')
        self.inputcode=self.inputcode.replace('૧','1')
        self.inputcode=self.inputcode.replace('૨','2')
        self.inputcode=self.inputcode.replace('૩','3')
        self.inputcode=self.inputcode.replace('૪','4')
        self.inputcode=self.inputcode.replace('૫','5')
        self.inputcode=self.inputcode.replace('૬','6')
        self.inputcode=self.inputcode.replace('૭','7')
        self.inputcode=self.inputcode.replace('૮','8')
        self.inputcode=self.inputcode.replace('૯','9')
        self.inputcode = self.inputcode.replace('<','\n')
        self.inputcode = self.inputcode.replace('>','\n')
        self.inputcode=self.inputcode.replace('જો','if')
        self.inputcode=self.inputcode.replace('અથવાજો','elif')
        self.inputcode=self.inputcode.replace('નહીતો','else')
        self.inputcode =self.inputcode.replace('લખો','print')
        self.inputcode =self.inputcode.replace('જ્યાંસુધી ','while')
        
        return self.inputcode
    def maths(self):
        self.inputcode=self.inputcode.replace('$ગણિત દાખલ કરો$','import math')
        self.inputcode =self.inputcode.replace('વર્ગમૂળ','math.sqrt')   
        return self.inputcode
            
    def olp(self):
        self.inputcode =self.inputcode.replace('ફરીથી','for')
        self.inputcode =self.inputcode.replace('ની','in')
        self.inputcode =self.inputcode.replace('શ્રેણી','range')
        return self.inputcode

    def drowing(self):
        self.inputcode=self.inputcode.replace('$દોરવાનું દાખલ કરો$','import turtle')
        self.inputcode=self.inputcode.replace('દોરો.આગળ','turtle.fd')
        self.inputcode=self.inputcode.replace('દોરો.પાછળ','turtle.backword')
        self.inputcode=self.inputcode.replace('દોરો.જમણીબાજુ','turtle.right')
        self.inputcode=self.inputcode.replace('દોરો.ડાબીબાજુ','turtle.left')
        self.inputcode=self.inputcode.replace('દોરો.પેનનોરંગ','turtle.pencolor')
        self.inputcode=self.inputcode.replace('લાલ','red')
        self.inputcode=self.inputcode.replace('કાળો','black')
        self.inputcode=self.inputcode.replace('વાદળી','blue')
        self.inputcode=self.inputcode.replace('લીલો','green')
        self.inputcode=self.inputcode.replace('દોરો.વર્તુળ','turtle.circle')
        self.inputcode=self.inputcode.replace('દોરો.રદકરો','turtle.clear')
        self.inputcode=self.inputcode.replace('દોરો.પેનબંધ','turtle.pendown')
        self.inputcode=self.inputcode.replace('દોરો.પેનચાલુ','turtle.penup')
        self.inputcode=self.inputcode.replace('દોરો.રંગપૂરો','turtle.fillcolor')
    
        


        return self.inputcode
#p1 = frist1("૦૧૨૩.૩૫૨.૨૫૩૨૩૨.૩૨૫૫૩ ")
#print(p1.frist())
#$દોરવાનું દાખલ કરો$
#દોરો.આગળ
#$ગણિત દાખલ કરો$
#લખો(વર્ગમૂળ(૨૫))