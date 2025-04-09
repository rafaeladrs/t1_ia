from collections import deque
from opera import gerar_sucessores

def bfs(inicial, objetivo):
    fila = deque([(inicial, [inicial])]) 
    visitados = set()  # conjunto de estados visitados

    while fila:
        atual, caminho = fila.popleft()
        if atual == objetivo:
            return caminho #estado final

        visitados.add(atual)
        for sucessor in gerar_sucessores(atual):
            if sucessor not in visitados:
                fila.append((sucessor, caminho + [sucessor])) # adiciona novo caminho

    return None # retorna nenhum caminho encontrado