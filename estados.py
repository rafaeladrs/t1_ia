import random

estado_inicial = ('e', 'e', 'e', 'e', 'e', False) #movimentos de inicio + flag que define se o lobo foi mordido ou nao
estado_objetivo = ('d', 'd', 'd', 'd', 'd', False) 

#verifica se um estado é valido/seguro e se precisa marcar o lobo como ferido
def estado_valido(estado):
    F, L, Ov, R, C, ferido = estado 

    if ferido:
        return estado #se esta ferido nao tem riscos

#se o lobo esta com a ovelha e sem o fazendeiro, é um estado invalido
    if L == Ov and F != L:
        return False 

#se o repolho esta com a ovelha e sem o fazendeiro, é um estado invalido
    if Ov == R and F != Ov:
        return False

# se o lobo e o cachorro estão sem o fazendeiro, cachorro morde o lobo, flag vira true
    personagens_na_margem = [
        nome for nome, pos in zip(['F', 'L', 'Ov', 'R', 'C'], estado[:5]) if pos == L
    ]
    if 'L' in personagens_na_margem and 'C' in personagens_na_margem and len(personagens_na_margem) == 2:
        return (*estado[:5], True) #muda flag

    return estado #retorna estado valido

def vai(estado):
    F, L, Ov, R, C, ferido = estado
    novo_lado = 'd' if F == 'e' else 'e' #troca lado do fazendeiro p dir
    return (novo_lado, L, Ov, R, C, ferido)

def levaLobo(estado):
    F, L, Ov, R, C, ferido = estado
    if ferido:
        return None
    if F == L:
        novo_lado = 'd' if F == 'e' else 'e' #troca lado do fazendeiro e do lobo p dir
        return (novo_lado, novo_lado, Ov, R, C, ferido)
    return None

def levaOvelha(estado):
    F, L, Ov, R, C, ferido = estado
    if F == Ov:
        novo_lado = 'd' if F == 'e' else 'e' #troca lado do fazendeiro e da ovelha p dir
        return (novo_lado, L, novo_lado, R, C, ferido) 
    return None

def levaRepolho(estado):
    F, L, Ov, R, C, ferido = estado
    if F == R:
        novo_lado = 'd' if F == 'e' else 'e' #troca lado do fazendeiro e do repolho p dir
        return (novo_lado, L, Ov, novo_lado, C, ferido)
    return None

def levaCachorro(estado):
    F, L, Ov, R, C, ferido = estado
    if F == C:
        novo_lado = 'd' if F == 'e' else 'e' #troca lado do cachorro e do fazendeiro
        return (novo_lado, L, Ov, R, novo_lado, ferido)
    return None

def volta(estado):
    F, L, Ov, R, C, ferido = estado
    novo_lado = 'e' if F == 'd' else 'd' #volta fazendeiro pra esq
    return (novo_lado, L, Ov, R, C, ferido)

def trazLobo(estado):
    F, L, Ov, R, C, ferido = estado
    if ferido:
        return None
    if F == L: 
        novo_lado = 'e' if F == 'd' else 'd' #volta fazendeiro e lobo p esq
        return (novo_lado, novo_lado, Ov, R, C, ferido)
    return None

def trazOvelha(estado):
    F, L, Ov, R, C, ferido = estado
    if F == Ov:
        novo_lado = 'e' if F == 'd' else 'd' #volta fazendeiro e ovelha p esq
        return (novo_lado, L, novo_lado, R, C, ferido)
    return None

def trazRepolho(estado):
    F, L, Ov, R, C, ferido = estado
    if F == R:
        novo_lado = 'e' if F == 'd' else 'd' #volta fazendeiro e repolho p esq
        return (novo_lado, L, Ov, novo_lado, C, ferido)
    return None

def trazCachorro(estado):
    F, L, Ov, R, C, ferido = estado
    if F == C:
        novo_lado = 'e' if F == 'd' else 'd' #volta fazendeiro com cachorro p esq
        return (novo_lado, L, Ov, R, novo_lado, ferido)
    return None

def impacienciaOvelha(estado):
    F, L, Ov, R, C, ferido = estado
    if F == Ov and random.random() < 0.2:
        novo_lado = 'd' if Ov == 'e' else 'e' #muda lado da ovelha caso o random seja menor que 20%
        return (F, L, novo_lado, R, C, ferido)
    return None