from math import e, factorial, sqrt

#Poisson
total=0
for i in range(0, 5):
	total+=(pow(e, -9.92)*pow(9.92, i)/factorial(i))
print(1-total)
print(pow(e, -9.92)*pow(9.92, 4)/factorial(4))


a=[0.0107, 0.0545, 0.1312, 0.2001, 0.2167, 0.1773, 0.1138, 0.0587, 0.0247, 0.00859, 0.00248, 0.00059]
total2=0
total3=0
for i in range(0, 12):
	total2+=a[i]*i
	total3+=pow(i-4.074, 2)*a[i]
print("Esperança da variável aleatória discreta X: ", total2)#Esperança da variável aleatória discreta X
print("Variância de X: ", total3)#Variância de X
print("Devio padrão: ", sqrt(total3))#Devio padrão



#Hipergeométrica
def comb(n, r):
	return float(factorial(n)/(factorial(r)*factorial(n-r)))
total4=[]

N = int(input("Digite o número de elementos da população(N): "))
n = int(input("Digite o tamanho das amostras extráidas sem reposição(n): "))
r = int(input("Digite o número de elementos (r)  do tipo 1 (tipo que você está interessado: "))

EY = int(input("Digite a esperança da variável E[Y]: "))
k=min(r, n)

for i in range(0,k+1):
	total4.append((comb(EY, i)*comb(N-EY, n-i))/comb(N,n))
print(f"A probabilidade de P(X<={r}: {sum(total4[0:r+1])}")
print(f"A probabilidade de P(X<={r}): {sum(total4[0:r])}")
print(f"A probabilidade de P(X>{r}): {1-(sum(total4[0:r+1]))}")
