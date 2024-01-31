from random import getrandbits, randint, random, choices

def individual(n_de_itens):
    """Cria um membro da populacao"""
    return [ getrandbits(1) for x in range(n_de_itens) ]

def population(n_de_individuos, n_de_itens):
    """"Cria a populacao"""
    return [ individual(n_de_itens) for x in range(n_de_individuos) ]


def fitness(individuo, peso_maximo, pesos_valores):
    total_peso = 0
    total_valor = 0

    for i in range(len(individuo)):
        if individuo[i] == 1:  # Se o item foi escolhido (representado por 1)
            total_peso += pesos_valores[i][0]  # Peso do item
            total_valor += pesos_valores[i][1]  # Valor do item

    # Penalização se o peso total excede a capacidade da mochila
    #if total_peso > peso_maximo:
     #   penalidade = total_peso - peso_maximo
      #  total_valor -= penalidade  # Penalização subtraindo o excesso de peso
    if total_peso > peso_maximo:
        # Se o peso excede o limite, o fitness é negativo para desfavorecer esse indivíduo
        return 1
    else:
        return total_valor

    return total_valor

def crossover(individuo1, individuo2, taxa_cruzamento):
    """Realiza o crossover de ponto único entre dois indivíduos com uma certa taxa de cruzamento"""
    if random() < taxa_cruzamento:
        ponto_corte = randint(1, len(individuo1) - 1)
        filho1 = individuo1[:ponto_corte] + individuo2[ponto_corte:]
        filho2 = individuo2[:ponto_corte] + individuo1[ponto_corte:]
        return filho1, filho2
    else:
        return individuo1, individuo2

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