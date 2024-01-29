from random import getrandbits, randint, random, choices

def individual(n_de_itens):
    """Cria um membro da populacao"""
    return [ getrandbits(1) for x in range(n_de_itens) ]

def population(n_de_individuos, n_de_itens):
    """"Cria a populacao"""
    return [ individual(n_de_itens) for x in range(n_de_individuos) ]

def fitness(individuo, peso_maximo, pesos_valores):
    """Faz avaliação do indivíduo"""
    peso_total, valor_total = 0, 0
    for indice, presente in enumerate(individuo):
        peso_total += presente * pesos_valores[indice][0]
        valor_total += presente * pesos_valores[indice][1]

    if peso_total > peso_maximo:
        return 0  # Se exceder o peso máximo, fitness é zero
    else:
        return peso_total  #  fitness é o valor total
    
def crossover(individuo1, individuo2):
    """Realiza o crossover de ponto único entre dois indivíduos"""
    ponto_corte = randint(1, len(individuo1) - 1)
    print(f"Individuo selecionado 1: {individuo1}")
    print(f"Individuo selecionado 2: {individuo2}")
    print ("-")
    filho1 = individuo1[:ponto_corte] + individuo2[ponto_corte:]
    filho2 = individuo2[:ponto_corte] + individuo1[ponto_corte:]
    return filho1, filho2

def calcular_probabilidades_fitness(populacao, peso_maximo, pesos_valores):
    # Calcula o fitness de cada indivíduo na população
    fitness_populacao = [fitness(individuo, peso_maximo, pesos_valores) for individuo in populacao]

    # Normaliza os valores de fitness para criar uma roleta de seleção
    soma_fitness = sum(fitness_populacao)
    probabilidades = [fit / soma_fitness for fit in fitness_populacao]

    return probabilidades

def selecao_por_roleta(populacao, peso_maximo, pesos_valores):
    probabilidades = calcular_probabilidades_fitness(populacao, peso_maximo, pesos_valores)

    nova_geracao = []
    for _ in range(len(populacao)):
        # Seleciona um indivíduo baseado na roleta de probabilidades
        selecionado = choices(populacao, weights=probabilidades, k=1)[0]
        nova_geracao.append(selecionado)

    return nova_geracao

def mutacao(individuo, taxa_mutacao):
    """Realiza a mutação em um indivíduo"""
    for i in range(len(individuo)):
        if random() < taxa_mutacao:
            # Inverte o valor do bit (0 para 1 ou 1 para 0)
            individuo[i] = 1 - individuo[i]
    return individuo

def aplicar_mutacao(populacao, taxa_mutacao):
    """Aplica mutação a cada indivíduo na população"""
    populacao_mutada = [mutacao(individuo, taxa_mutacao) for individuo in populacao]
    return populacao_mutada