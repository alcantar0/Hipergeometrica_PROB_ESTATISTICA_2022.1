from math import e, factorial, sqrt

#Hipergeométrica
def comb(n, r):
	return float(factorial(n)/(factorial(r)*factorial(n-r)))

vetor_de_probabilidades=[]

N = int(input("Digite o número de elementos da população(N): "))
n = int(input("Digite o tamanho das amostras extráidas sem reposição(n): "))
r = int(input("Digite o número de elementos (r)  do tipo 1 (tipo que você está interessado: "))

EY = int(input("Digite a esperança da variável E[Y]: "))
k=min(r, n)

for i in range(0,k+1):
	vetor_de_probabilidades.append((comb(EY, i)*comb(N-EY, n-i))/comb(N,n))
print(f"A probabilidade de P(X<={r}: {sum(vetor_de_probabilidades[0:r+1])}")
print(f"A probabilidade de P(X<={r}): {sum(vetor_de_probabilidades[0:r])}")
print(f"A probabilidade de P(X>{r}): {1-(sum(vetor_de_probabilidades[0:r+1]))}")
