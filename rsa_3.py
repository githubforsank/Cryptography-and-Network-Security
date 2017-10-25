import random

orac_key = 0
orac_n = 0


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

def orac(enc_str):
	global orac_key
	global orac_n
	lis_k = []
	for i in range(0,len(enc_str)):
		lis_k.append(pow(enc_str[i],orac_key,orac_n))
	
	return lis_k
	

def decrp(enc_str,e,n):
	print(enc_str)
	teres = []
	for i in range(0,len(enc_str)):
		teres.append(enc_str[i]*pow(2,e,n))
	lis_tw = orac(teres)
	res = []
	for i in range(0,len(lis_tw)):
		res.append(lis_tw[i]/2)
	print(res)
		

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
orac_n = n

phi_n=1

for i in pr:
	phi_n*=(i-1)

print(phi_n)	

e = random.randint(1,phi_n)
g,s,t = exten_gcd(phi_n,e)


while(g!=1):
	e = random.randint(1,phi_n)
	g,s,t = exten_gcd(e,phi_n)


g,s,d_nu = exten_gcd(phi_n,e)

print(e)
print(d_nu)
orac_key = d_nu

print((e*d_nu)%phi_n)

inp = raw_input()

print(inp)
curr = ""

for i in range(0,len(inp)):
	a = str(ord(inp[i])-97)
	while len(a)<2:
		a = "0"+a
	curr+=a

print(curr)	

lis=[]
t_curr=""
for i in curr:
	 t_curr+=i
	 if(int(t_curr)>=n):
	 	lis.append(t_curr[:-1])
	 	t_curr = i
	 	
lis.append(t_curr)
print(lis)

lis_enc = []
for i in range(0,len(lis)):
	print(int(lis[i]))
	lis_enc.append(pow(int(lis[i]),e,n))



decrp(lis_enc,e,n)




