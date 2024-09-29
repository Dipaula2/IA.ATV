factorial_cache = {}

def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]

    if n == 0 or n == 1:
        value = 1
    else:
        value = n * factorial(n - 1)

    factorial_cache[n] = value
    return value

# Teste de cálculo fatorial
print(factorial(5))  # Calcula e armazena o valor de 5!
print(factorial(10))  # Calcula e armazena o valor de 10!
print(factorial(5))  # Recupera o valor de 5! do cache, sem recalcular
