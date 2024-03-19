def inverter_string(string):
    invertida = ''
    for caractere in string:
        invertida = caractere + invertida
    return invertida

# Exemplo de uso
texto_original = "Olá, mundo!"
texto_invertido = inverter_string(texto_original)
print("Texto original:", texto_original)
print("Texto invertido:", texto_invertido)
