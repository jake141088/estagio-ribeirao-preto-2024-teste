def fibonacci(n):
    a, b = 0, 1

    if n == a or n == b:
        return True

    while b < n:
        a, b = b, a + b
        if b == n:
            return True

    return False

def main():
    try:
        numero = int(input("Por favor, insira um número para verificar se pertence à sequência de Fibonacci: "))
        
        if fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()