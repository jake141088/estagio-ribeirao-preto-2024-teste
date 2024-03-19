def processamento(indice, soma, k):
    while k < indice:
        k += 1
        soma += k
       
    return soma
        
indice = 13
soma = 0
k = 0

resultado = processamento(indice, soma, k)

print(resultado)
#Então, ao final do processamento, o valor da variável SOMA será 91.