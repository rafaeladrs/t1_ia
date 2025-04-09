from bfs import bfs
import estados

def main():
    caminho_solucao = bfs(estados.estado_inicial, estados.estado_objetivo)
    if caminho_solucao:
        nomes_simples = ['f', 'l', 'ov', 'r', 'c', 'ferido']

        for i in range(len(caminho_solucao)):
            estado = caminho_solucao[i]
            linha = "["
            for nome, lado in zip(nomes_simples, estado):
                if nome == 'ferido':
                    linha += f"{nome} -> {'sim' if lado else 'não'}, "
                else:
                    linha += f"{nome} -> {lado}, "
            linha = linha.rstrip(", ") + "]"
            print(linha)

            if i < len(caminho_solucao) - 1:
                atual = caminho_solucao[i]
                prox = caminho_solucao[i + 1]
                moveram = []

                for idx, (a, b) in enumerate(zip(atual[:5], prox[:5])):
                    if a != b:
                        moveram.append(nomes_simples[idx])

                direcao = '→ dir' if prox[0] == 'd' else '← esq'

                if prox[5] and not atual[5]:
                    print("MOVIMENTO: lobo foi ferido pelo cachorro.\n")
                elif moveram == ['ov']:
                    print(f"MOVIMENTO: ovelha impaciente pulou sozinha {direcao}\n")
                elif len(moveram) == 1:
                    print(f"MOVIMENTO: {moveram[0]} foi sozinho(a) {direcao}\n")
                elif len(moveram) == 2:
                    print(f"MOVIMENTO: {moveram[0]} levou {moveram[1]} {direcao}\n")
                else:
                    print(f"MOVIMENTO: ação inesperada: {', '.join(moveram)} {direcao}\n")
            else:
                print("solução válida encontrada\n")
    else:
        print("nenhuma solução possível.")


if __name__ == "__main__":
    main()