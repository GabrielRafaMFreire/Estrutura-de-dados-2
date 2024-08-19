# Gabriel Rafá Martins Freire Mat: 20230145310
# Definindo o tamanho máximo da fila circular e inicializando variáveis
tamanho_maximo = 10
quantidade_atual = 0
fila = [0] * tamanho_maximo
indice_inicio = 0
indice_fim = -1

# Verifica se a fila está vazia
def esta_vazia():
    return quantidade_atual == 0 

# Verifica se a fila está cheia
def esta_cheia():
    return quantidade_atual == tamanho_maximo

# Consulta o elemento no início da fila sem removê-lo
def consultar_inicio():
    if esta_vazia():
        return "A fila está vazia."
    return fila[indice_inicio]

# Insere um novo valor no final da fila
def inserir(valor):
    global indice_fim, quantidade_atual
    if esta_cheia():
        return "A fila está cheia. Inserção não é possível."
    
    # Ajuste do índice do final da fila de forma circular
    indice_fim = (indice_fim + 1) % tamanho_maximo
    fila[indice_fim] = valor
    quantidade_atual += 1
    return True

# Remove o elemento no início da fila
def remover():
    global indice_inicio, quantidade_atual
    if esta_vazia():
        return "Não há elementos para remover."
    
    fila[indice_inicio] = 0  # Opcional: Reseta o valor removido
    indice_inicio = (indice_inicio + 1) % tamanho_maximo
    quantidade_atual -= 1

# Mostra todos os elementos da fila de forma ordenada
def mostrar_fila():
    elementos = []
    i = indice_inicio
    for _ in range(quantidade_atual):
        elementos.append(fila[i])
        i = (i + 1) % tamanho_maximo
    print(elementos)

# Testando as funções
inserir(3)
inserir(4)
inserir(5)
inserir(7)

mostrar_fila()
print("A fila está vazia?", esta_vazia())
print("A fila está cheia?", esta_cheia())
print("Elemento no início da fila:", consultar_inicio())

print("\n---- Removendo... ----")
remover()
mostrar_fila()

print("\n---- Removendo... ----")
remover()
mostrar_fila()

print("\n---- Consultando o novo início... ----")
print("Elemento no início da fila:", consultar_inicio())
