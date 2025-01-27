# 1. Criação de um Closure Simples
def multiplicador(numero):
    def multiplicar(valor):
        return numero * valor
    return multiplicar

multiplicar_2 = multiplicador(2)
print(multiplicar_2(5))  # Saída: 10
print(multiplicar_2(10))  # Saída: 20

# 2. Somador com Closure
def somador(numero):
    def somar(valor):
        return numero + valor
    return somar

somar_3 = somador(3)
print(somar_3(4))  # Saída: 7
print(somar_3(10))  # Saída: 13

# 3. Encapsulando Estado com Closure
def contador():
    contador_atual = 0
    def incrementar():
        nonlocal contador_atual
        contador_atual += 1
        return contador_atual
    return incrementar

cont = contador()
print(cont())  # Saída: 1
print(cont())  # Saída: 2

# 4. Closure com Parâmetro de Valor Padrão
def somador(valor_padrao):
    def somar(valor=0):
        return valor_padrao + valor
    return somar

somar_5 = somador(5)
print(somar_5(7))  # Saída: 12
print(somar_5())  # Saída: 5

# 5. Decorator Simples para Registrar Execução
def log_execucao(func):
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@log_execucao
def exemplo_funcao():
    print("Função em execução!")

exemplo_funcao()

# 6. Decorator para Medir Tempo de Execução
import time

def tempo_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução de {func.__name__}: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@tempo_execucao
def exemplo_longo():
    time.sleep(2)

exemplo_longo()

# 7. Decorator com Argumentos
def verifica_argumento(func):
    def wrapper(arg):
        if arg < 0:
            raise ValueError("O argumento deve ser positivo!")
        return func(arg)
    return wrapper

@verifica_argumento
def quadrado(numero):
    return numero ** 2

print(quadrado(4))  # Saída: 16
# print(quadrado(-3))  # Levanta ValueError

# 8. Decorator de Classe para Memoização (Cache)
class Memoizacao:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoizacao
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Saída: 55

# 9. Decorator de Classe com Argumentos
class VerificaTipo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __call__(self, func):
        def wrapper(arg):
            if not isinstance(arg, self.tipo):
                raise TypeError(f"O argumento deve ser do tipo {self.tipo.__name__}")
            return func(arg)
        return wrapper

@VerificaTipo(int)
def quadrado_tipo(numero):
    return numero ** 2

print(quadrado_tipo(5))  # Saída: 25
# print(quadrado_tipo("5"))  # Levanta TypeError
