import random


def is_prime(num,k):
        
        if num == 2:
                return True
        if not num & 1:
                return False

        def check(a, s, d, num):
                x = pow(a, d, num)
                if x == 1:
                        return True
                for i in xrange(s - 1):
                        if x == num - 1:
                                return True
                        x = pow(x, 2, num)
                return x == num - 1

        s = 0
        d = num - 1

        while d % 2 == 0:
                d >>= 1
                s += 1

        for i in xrange(k):
                a = random.randrange(2, num - 1)
                if not check(a, s, d, num):
                        return False
        return True

def exten_gcd(num1,num2):
        
        s0,s1,t0,t1 = 1,0,0,1
        t_sto=num1
        while num2!=0:
                q,num1,num2 = num1//num2,num2,num1%num2
                s0,s1 = s1,s0-q*s1
                t0,t1 = t1,t0-q*t1
        while t0<0:
                t0 = t0+t_sto
        return num1,s0,t0                                

cou = 0

pr = []


print "Two 128 bits number generated :"
while cou<2:
        num = random.getrandbits(128)
        if is_prime(num,18) is True:
                cou+=1
                pr.append(num)
                print(num)


print "Now printing (n) value :"
n = 1
for i in pr:
        n*=i

print(n)

phi_n=1

for i in pr:
        phi_n*=(i-1)
print "Now printing (phi_n) value :"
print(phi_n)        

e = random.randint(1,phi_n)
g,s,t = exten_gcd(phi_n,e)


while(g!=1):
        e = random.randint(1,phi_n)
        g,s,t = exten_gcd(e,phi_n)


g,s,d_nu = exten_gcd(phi_n,e)
print "The encryption ( public ) key :"
print(e)
print "The decryption ( private ) key :"
print(d_nu)

#print((e*d_nu)%phi_n)

inp = raw_input("Enter a message to be RSA encrypted :")

print "Message : ",(inp)
curr = ""

for i in range(0,len(inp)):
        a = str(ord(inp[i])-97)
        while len(a)<2:
                a = "0"+a
        curr+=a

print "ASCII translation :"
print(curr)        

lis=[]
t_curr=""
for i in curr:
         t_curr+=i
         if(int(t_curr)>=n):
                 lis.append(t_curr[:-1])
                 t_curr = i
                 
lis.append(t_curr)
#print(lis)

lis_enc = []
for i in range(0,len(lis)):
        #print(int(lis[i]))
        lis_enc.append(pow(int(lis[i]),e,n))

print "Encrypted message ",(lis_enc)

lis_k = []

for i in range(0,len(lis_enc)):
        lis_k.append(pow(lis_enc[i],d_nu,n))
        
print "Decrypted message",(lis_k)
