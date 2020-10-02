

try:
    numero = int(input("Digite um numero: "))
except ValueError as value_error:
    """except é executado  se der erro"""
    print("Só é permitido numeros !!")
else:
    """Caso não der erro """
    print(f"Voce digitou : {numero}")
finally:
    """Finally é executado independente se der erro ou não"""
    print(f"executando o finally : fim .")

