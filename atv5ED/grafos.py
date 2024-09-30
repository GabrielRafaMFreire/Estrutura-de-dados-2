# Gabriel Rafá Martins Freire Mat:20230145310

class GrafoBase:
    def __init__(self, arquivo):
        with open(arquivo, 'r') as arq:
            self.num_vertices = int(arq.readline().strip())
            self.dados = [list(map(int, linha.split())) for linha in arq]

class GrafoMatriz(GrafoBase):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self.matriz = self.dados  # Renomeia o atributo para matriz

    def exibir_matriz(self):
        for linha in self.matriz:
            print(' '.join(map(str, linha)))

class GrafoLista(GrafoBase):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        self.lista_adj = [[] for _ in range(self.num_vertices)]
        for i in range(self.num_vertices):
            for j, valor in enumerate(self.dados[i]):
                if valor > 0:
                    self.lista_adj[i].append(j)  # Mantém vértices adjacentes

    def exibir_lista(self):
        for indice, adjacentes in enumerate(self.lista_adj):
            print(f'Vertice {indice}: {adjacentes}')

    def bfs_rec(self, nivel_atual, visitados, predecessores):
        if not nivel_atual:
            return

        prox_nivel = []
        for vertice in nivel_atual:
            for vizinho in self.lista_adj[vertice]:
                if not visitados[vizinho]:
                    visitados[vizinho] = True
                    predecessores[vizinho] = vertice
                    prox_nivel.append(vizinho)
        self.bfs_rec(prox_nivel, visitados, predecessores)

    def encontrar_caminho_bfs(self, inicio, fim):
        visitados = [False] * len(self.lista_adj)
        predecessores = [-1] * len(self.lista_adj)
        visitados[inicio] = True
        self.bfs_rec([inicio], visitados, predecessores)

        if not visitados[fim]:
            print(f"Não existe caminho entre os vértices {inicio} e {fim}.")
        else:
            caminho = []
            atual = fim
            while atual != -1:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            print(f"Caminho BFS entre os vértices {inicio} e {fim}: {' -> '.join(map(str, caminho))}")

    def dfs(self, vertice_inicio):
        visitados = [False] * len(self.lista_adj)
        pilha = [vertice_inicio]

        while pilha:
            atual = pilha.pop()
            if not visitados[atual]:
                print(atual, end=" ")
                visitados[atual] = True
                for vizinho in reversed(self.lista_adj[atual]):
                    if not visitados[vizinho]:
                        pilha.append(vizinho)

    def encontrar_caminho_dfs(self, inicio, fim):
        visitados = [False] * len(self.lista_adj)
        predecessores = [-1] * len(self.lista_adj)
        pilha = [inicio]

        while pilha:
            atual = pilha.pop()
            if not visitados[atual]:
                visitados[atual] = True
                if atual == fim:
                    break
                for vizinho in reversed(self.lista_adj[atual]):
                    if not visitados[vizinho]:
                        pilha.append(vizinho)
                        predecessores[vizinho] = atual

        if not visitados[fim]:
            print(f"Não existe caminho entre os vértices {inicio} e {fim}.")
        else:
            caminho = []
            atual = fim
            while atual != -1:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            print(f"Caminho DFS entre os vértices {inicio} e {fim}: {' -> '.join(map(str, caminho))}")

# Exemplo de uso
grafo_matriz = GrafoMatriz('instancias-grafo/pcv4.txt')
print("\nMatriz de Adjacência:")
grafo_matriz.exibir_matriz()

grafo_lista = GrafoLista('instancias-grafo/pcv4.txt')
print("\nLista de Adjacência:")
grafo_lista.exibir_lista()

print("\nCaminho BFS entre 0 e 3:")
grafo_lista.encontrar_caminho_bfs(0, 3)

print("\nBusca em Profundidade (DFS) a partir do vértice 0:")
grafo_lista.dfs(0)
print()

print("\nCaminho DFS entre 0 e 3:")
grafo_lista.encontrar_caminho_dfs(0, 3)

