from random import randint
n=10
a=[]
#print(b)
for x in range(n):
	a.append(randint(1,99))
print(a)

for i in range(n-1):
	print("это i",i)
	for j in range(n-i-1):
		print(j)
		if a[j]>a[j+1]:
			a[j],a[j+1]= a[j+1],a[j]
		print(a)
print(a)