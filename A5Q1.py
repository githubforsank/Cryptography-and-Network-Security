import random


def is_prime(num,k):
        
        if num<2:
                return False
        
        if num%2==0:
                return False
                
        r=0
        s=num-1
        
        while(s%2==0):
                r+=1
                s//=2
        
        for i in xrange(k):
                a = random.randrange(2, num-1)
                x = pow(a,s,num)
                if x==1 or x == num-1:
                        continue
                for j in xrange(r-1):
                        x = pow(x,2,num)
                        if x == num-1:
                                break
                                
                        else:
                                return False
                return True

def exten_gcd(num1,num2):
        
        s0,s1,t0,t1 = 1,0,0,1
        while n!=0:
                q,num1,num2 = num1//num2,num1,num2%num1
                s0,s1 = s1,s0-q*s1
                t0,t1 = t1,t0-q*t1
        return num2,s0,t0                                

cou = 0

pr = []

while cou<2:
        num = random.getrandbits(128)
        if is_prime(num,18) is True:
                cou+=1
                pr.append(num)
                print(num)

n = 1
for i in pr:
        n*=i

print(n)

phi_n=1

for i in pr:
        phi_n*=(i-1)

print(phi_n)        

e = random.randint(1,phi_n)

print(e)
