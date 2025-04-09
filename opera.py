from estados import impacienciaOvelha, vai, levaLobo, levaOvelha, levaRepolho, levaCachorro, volta, trazLobo, trazOvelha, trazRepolho, trazCachorro, estado_valido

def gerar_sucessores(estado):
    operadores = [
        vai,
        levaLobo,
        levaOvelha,
        levaRepolho,
        levaCachorro,
        volta,
        trazLobo,
        trazOvelha,
        trazRepolho,
        trazCachorro,
        impacienciaOvelha
    ]
    
    sucessores = []
    for oper in operadores:
        novo_estado = oper(estado)
        if novo_estado is not None and estado_valido(novo_estado): 
            resultado = estado_valido(novo_estado) # verifica se precisa marcar lobo ferido
            if resultado:
                sucessores.append(resultado) # adiciona apenas se for válido
    return sucessores
