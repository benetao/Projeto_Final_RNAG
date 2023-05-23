import random

###############################################################################
#                                   Suporte                                   #
##############################################################################+


def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.

    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.

    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades


# NOVIDADE
def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila

    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """
    
    valor_total = 0
    peso_total = 0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]["valor"]
            peso_do_item = objetos[nome_do_item]["peso"]
            
            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item

    return valor_total, peso_total


###############################################################################
#                                    Genes                                    #
###############################################################################


def gene_cb():
    """Gera um gene válido para o problema das caixas binárias

    Return:
      Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene


def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias

    Args:
      valor_max_caixa: número inteiro representando o maior valor possível que
      pode existir dentro de uma caixa.

    Return:
      Um valor entre zero a `valor_max_caixa` (inclusive).
    """
    gene = random.randint(0, valor_max_caixa)
    return gene


def gene_letra(letras):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra


###############################################################################
#                                  Indivíduos                                 #
###############################################################################


def individuo_cb(n):
    """Gera um individuo para o problema das caixas binárias.

    Args:
      n: número de genes do indivíduo.

    Return:
       Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo


def individuo_cnb(n_genes, valor_max_caixa):
    """Gera um individuo para o problema das caixas não-binárias.

    Args:
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa

    Return:
       Uma lista com n genes. Cada gene é um valor entre zero e
       `valor_max_caixa`.
    """
    individuo = []
    for i in range(n_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato


def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes


###############################################################################
#                                  População                                  #
###############################################################################


def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.

    Args:
      tamanho: tamanho da população.
      n: número de genes do indivíduo.

    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com `n`
      genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def populacao_cnb(tamanho, n_genes, valor_max_caixa):
    """Cria uma população no problema das caixas não-binárias.

    Args:
      tamanho: tamanho da população.
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa

    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com
      `n_genes` genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n_genes, valor_max_caixa))
    return populacao


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha

    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao


def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.

    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_roleta_max(populacao, fitness):
    """Seleciona individuos de uma população usando o método da roleta.

    Nota: apenas funciona para problemas de maximização.

    Args:
      populacao: lista com todos os individuos da população
      fitness: lista com o valor da funcao objetivo dos individuos da população

    Returns:
      População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(
        populacao, weights=fitness, k=len(populacao)
    )
    return populacao_selecionada


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos da população
      tamanho_torneio: quantidade de invidiuos que batalham entre si

    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)

    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2


def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.

    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.

    Ver pág. 37 do livro do Wirsansky.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    corte1 = random.randint(0, len(pai) - 2)
    corte2 = random.randint(corte1 + 1, len(pai) - 1)
    
    filho1 = pai[corte1:corte2]
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
            
    filho2 = mae[corte1:corte2]
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
            
    return filho1, filho2


###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias

    Args:
      individuo: uma lista representado um individuo no problema das caixas
      binárias

    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo


def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene no problema das caixas não-binárias

    Args:
      individuo:
        uma lista representado um individuo no problema das caixas não-binárias
      valor_max_caixa:
        maior número inteiro possível dentro de uma caixa

    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo


def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.

    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.

    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo


def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.

    Args:
      individuo: uma lista representado um individuo.

    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    
    return individuo
    


###############################################################################
#                         Função objetivo - indivíduos                        #
###############################################################################


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.

    Args:
      individiuo: lista contendo os genes das caixas binárias

    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)


def funcao_objetivo_cnb(individuo):
    """Computa a função objetivo no problema das caixas não-binárias.

    Args:
      individiuo: lista contendo os genes das caixas não-binárias

    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)


def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha

    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca


def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.

    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    for posicao in range(len(individuo) - 1):
        
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso        
               
    # Calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]

    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso
    
    return distancia


# NOVIDADE
def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.

    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """
    
    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
    
    if peso_mochila > limite:
        return 0.01
    else:
        return valor_mochila


###############################################################################
#                         Função objetivo - população                         #
###############################################################################


def funcao_objetivo_pop_cb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população

    Args:
      populacao: lista com todos os individuos da população

    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness


def funcao_objetivo_pop_cnb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população

    Args:
      populacao: lista com todos os individuos da população

    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cnb(individuo)
        fitness.append(fobj)
    return fitness


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado


def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.

    Args:
      populacao:
        Lista com todos os individuos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))
    return resultado


# NOVIDADE
def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila

    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.

    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado


###############################################################################
#                         Caixeiro Gasolina Infinita                          #
###############################################################################

def criar_pontos_intermediarios_x(x, y, num_pontos):
	"""
	Função criada para  fazer o gif do caixeiro viajante! Cria a lista de coordenadas x de pontos intermediários igualmente espaçados entre dois pontos.

    Args:
        x (list): Lista contendo as coordenadas em x dos dois pontos.
        y (list): Lista contendo as coordenadas em y dos dois pontos.
        num_pontos (int): Número de pontos intermediários a serem criados.

	Returns:
		list: Lista contendo as coordenadas em x dos pontos inicial, final e intermediários.
	"""
	pontos_x = [x[0]]  # Coordenadas x do ponto inicial
	pontos_y = [y[0]]  # Coordenadas y do ponto inicial
	# Cálculo dos incrementos em x e y entre os dois pontos
	incremento_x = (x[1] - x[0]) / (num_pontos + 1)
	incremento_y = (y[1] - y[0]) / (num_pontos + 1)
	# Criação dos pontos intermediários
	for i in range(1, num_pontos + 1):
		ponto_x = x[0] + i * incremento_x
		ponto_y = y[0] + i * incremento_y
		pontos_x.append(ponto_x)
		pontos_y.append(ponto_y)
	pontos_x.append(x[1])  # Coordenadas x do ponto final
	pontos_y.append(y[1])  # Coordenadas y do ponto final
	return pontos_x

def criar_pontos_intermediarios_y(x, y, num_pontos=30):
	"""
	Função criada para  fazer o gif do caixeiro viajante! Cria a lista de coordenadas y de pontos intermediários igualmente espaçados entre dois pontos.
	Args:
		x (list): Lista contendo as coordenadas em x dos dois pontos.
		y (list): Lista contendo as coordenadas em y dos dois pontos.
		num_pontos (int): Número de pontos intermediários a serem criados.
	Returns:
		pontos_y: Lista contendo as coordenadas em y dos pontos inicial, final e intermediários.
	"""
	pontos_x = [x[0]]  # Coordenadas x do ponto inicial
	pontos_y = [y[0]]  # Coordenadas y do ponto inicial
    # Cálculo dos incrementos em x e y entre os dois pontos
	incremento_x = (x[1] - x[0]) / (num_pontos + 1)
	incremento_y = (y[1] - y[0]) / (num_pontos + 1)
	# Criação dos pontos intermediários
	for i in range(1, num_pontos + 1):
		ponto_x = x[0] + i * incremento_x
		ponto_y = y[0] + i * incremento_y
		pontos_x.append(ponto_x)
		pontos_y.append(ponto_y)
	pontos_x.append(x[1])  # Coordenadas x do ponto final
	pontos_y.append(y[1])  # Coordenadas y do ponto final
	return pontos_y

def caminhoo_x(listax, listay):
	""" Função criada para  fazer o gif do caixeiro viajante! Curia uma lista de TODOS os pontos x para o gif, iterando a função "criar_pontos_intermediarios_y"

	Args:
    
		listax (list): Lista contendo as coordenadas em x das cidades.
		lista y (list): Lista contendo as coordenadas em y das cidades.   
    
	Returns:
		lista_unica: Lista contendo as coordenadas em x de TODOS os pontos necessários para o gif
    
    """
	lista_total_x=[]
	lista_total_y=[]

	for i in range(len(listax)-1):
		listaax=[]
		listaay=[]
		listaax= [listax[i], listax[i+1]]
		listaay= [listay[i], listay[i+1]]
		lista_total_x.append(criar_pontos_intermediarios_x(listaax, listaay, num_pontos=30))
	lista_unica = [item for lista in lista_total_x for item in lista]
	return lista_unica

def caminhoo_y(listax, listay):
    
	""" Função criada para  fazer o gif do caixeiro viajante! Curia uma lista de TODOS os pontos y para o gif, iterando a função "criar_pontos_intermediarios_y"
    
	Args:
    
       listax (list): Lista contendo as coordenadas em x das cidades.
       lista y (list): Lista contendo as coordenadas em y das cidades.   
    
    Returns:
        lista_unica: Lista contendo as coordenadas em y de TODOS os pontos necessários para o gif
    
    
    """
	lista_total_x=[]
	lista_total_y=[]

	for i in range(len(listax)-1):
		listaax=[]
		listaay=[]
		listaax= [listax[i], listax[i+1]]
		listaay= [listay[i], listay[i+1]]
		lista_total_y.append(criar_pontos_intermediarios_y(listaax, listaay, num_pontos=30))
	lista_unica = [item for lista in lista_total_y for item in lista]
	return lista_unica

###############################################################################
#                                Himelblau                                    #
###############################################################################


def gene_blau(dominio):
    """ Gera um gene para o problema da função de Himmelblau
    
    Args:
        dominio: valores possíveis para x e para y
    Return:
        Um valor aleatório do domínio estabelecido
    """
    gene = random.choice(dominio)
    return gene

def individuo_blau(N, dominio):
    """ Gera um indivíduo para o problema da função de Himmelblau
    
    Args:
        N: número de genes
        dominio_x_y: valores possíveis para x e y
        
    Return:
        Um indivíduo possível para o problema
    """
    individuo = []
    for _ in range(N):
        gene = gene_blau(dominio)
        individuo.append(gene)
    return individuo

def populacao_blau(tamanho, N, dominio):
    """ Gera uma população de indivíduos para o problema de Himmelblau
    
    Args:
        N: número de genes de cada indivíduo (2)
        tamanho: número de indivíduos da população
        dominio: valores possíveis para x e y
    
    Return:
        Uma lista contendo cada indivíduo
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_blau(N, dominio))
    return populacao

def funcao_objetivo_blau(individuo):
    """Calcula fitness de um indivíduo
    
    Args:
        individuo: lista contendo os genes de um indivíduo
        
    Return:
        O valor da função de função de Himmelblau no ponto de x e y, contidos no indivíduo
    """
    x = individuo[0]
    y = individuo[1]
    
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def funcao_objetivo_pop_blau(populacao):
    """ Calcula fitness de todos indivíduos de uma população
    
    Args:
        populacao: Lista com todos os indivíduos da população
        
    Return:
        Lista com fitness de todos os indivíduos
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_blau(individuo)
        fitness.append(fobj)
    return fitness

def torneio_blau(populacao, chance_de_competir_ind):
	"""Escolhe aleatoriamente parte a da população para competir e coloca o valor do vencedor no lugar dos perdedores
	
	Args:
		população: Lista com todos os indivíduos da população
		chance_de_competir_ind: chance de um individuo competir
        
	Return:
		Lista com todos os indivíduos já alterados com valor do vencedor
	"""
	index=[]
	melhor_fit = float("inf")
	for i in range(len(populacao)):
		if random.random() < chance_de_competir_ind:
			individuo = populacao[i]
			fobj = funcao_objetivo_blau(individuo)
			if fobj < melhor_fit:
				melhor_fit = fobj
				indice_melhor_fit = i
			index.append(i)
    
	populacao_selecionada = populacao
    
	for j in index:
		populacao_selecionada[j] = populacao[indice_melhor_fit]
    
	return populacao_selecionada

def mutacao_blau(individuo, dominio):
    """Muta gene no experimento função de Himmelblau
    
    Args:
        individuo: uma lista representando o individuo do experimento função de Himmelblau
        dominio: valores possíveis para x
        
    Return:
        Indivíduo com gene mutado.
    """
    gene= random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_blau(dominio)
    return individuo
