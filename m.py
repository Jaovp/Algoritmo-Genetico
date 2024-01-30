import matplotlib.pyplot as plt
from g import*

pesos_valores = [[8,60], [25,20], [30,100], [7,40], [10,50], [9,20], [9,50], [40,80], [2,5], [4,10]]

peso_maximo = 120
cromossomos = 10
geracoes = 20

n_itens = len(pesos_valores)

populacao = population(cromossomos, n_itens)

print("Populacao Inicial:")
print()
for i in range(len(populacao)):
        print(f"Individuo {i + 1}: {populacao[i]} - Fitness: {fitness(populacao[i], peso_maximo, pesos_valores)}")
print()

taxa_mutacao = 0.1
porcentagem_elitismo = 0.2
taxa_cruzamento = 0.8

fitness_values = []

# melhor fitness
melhor_fitness = float('-inf')

melhor_fitness_values = []
generations = []

for geracao in range(geracoes):
    nova_geracao_selecionada = selecao_por_roleta(populacao, peso_maximo, pesos_valores)

    nova_geracao = []

    i = 0
    while i < len(nova_geracao_selecionada):
        if i + 1 < len(nova_geracao_selecionada):
            filho1, filho2 = crossover(nova_geracao_selecionada[i], nova_geracao_selecionada[i + 1], taxa_cruzamento)
            nova_geracao.extend([filho1, filho2])
        else:
            # Caso tenha um número ímpar de indivíduos, mantém o último indivíduo na nova geração
            nova_geracao.append(nova_geracao_selecionada[i])
        i += 2

    # Aplica mutação apenas aos novos indíviduos gerados no cruzamento
    nova_geracao = aplicar_mutacao(nova_geracao, taxa_mutacao)

    populacao = nova_geracao

    for individuo in populacao:
        fitness_value = fitness(individuo, peso_maximo, pesos_valores)
        fitness_values.append(fitness_value)

        # Atualiza o melhor_fitness se o valor de fitness atual for melhor
        if fitness_value > melhor_fitness:
            melhor_fitness = fitness_value
            melhor_cromossomo = individuo

    melhor_fitness_values.append(melhor_fitness)
    generations.append(geracao + 1)

    # Exibe informações sobre a geração atual
    print(f"--- Geracao {geracao + 1} ---")
    for i in range(len(populacao)):
        print(f"Individuo {i + 1}: {populacao[i]} - Fitness: {fitness(populacao[i], peso_maximo, pesos_valores)}")
    print()
    print("Melhor fitness alcancado: ", melhor_fitness)
    print()



plt.plot(generations, melhor_fitness_values, marker='o')
plt.xlabel('Geracao')
plt.ylabel('Melhor Fitness')
plt.title('Melhor Fitness por Geracao')
plt.grid(True)
plt.show()
    