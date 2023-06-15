import random

def computa_maternidade(individuo, objetos, ordem_dos_nomes):
    """Computa o valor de sintomas importantes em uma emergência de maternidade.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      hemorragia_total: valor de níveis de hemorragia.
      idade_gestacional_total: tempo de gestação de mulheres em uma emergência em unudade de semanas.
      dor_total: nível da dor
      meows_total: classificação que 
      choque_total: 
      leitos_total: 
    """

    hemorragia_total = 0
    idade_gestacional_total = 0
    dor_total = 0
    meows_total= 0
    choque_total = 0
    leitos_total = 0
        
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            hemorragia = objetos[nome_do_item]["hemorragia"]
            gestacional= objetos[nome_do_item]["idade gestacional"]
            dor= objetos[nome_do_item]["dor"]
            meows= objetos[nome_do_item]["meows"]
            choque= objetos[nome_do_item]["sinais de choque"]
            leitos = objetos [nome_do_item]["leito"]
            
            
            hemorragia_total += hemorragia
            idade_gestacional_total += gestacional
            dor_total += dor
            meows_total += meows
            choque_total += choque
            leitos_total += leitos 
            
    valor_mochila = 25*hemorragia_total + 2 * idade_gestacional_total + 10 * dor_total + 25*meows_total + 33 * choque_total
            

    return valor_mochila, leitos_total



def gene_cb():
    """ Gera um gene válido para o problema das caixas binárias
    
    Return:
        Um valos de zeros ou um
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene



def individuo_cb (n):
    ''' Gera um individuo para o problema da caixa binaria
    
    Args:
       n: numero de genes do individuo
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um
    '''
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo



def populacao_cb(tamanho, n):
    ''' cria uma população no problema das.
    
    Args:
       n: numero de gene de um individuo
       tamanho: tamanho da população
    
    Return:
        Uma lista onde cada item é um individuo. Um individuo é uma lista com n genes.
    '''
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n)) #ele está criando uma pop a partir de uma funcao que ja existe, n vezes
    return populacao




def selecao_roleta_max (populacao, fitness): #depende dos individuos que vão ser sorteados, o quão bom o individuo é dentro da função
    '''seleciona individuos de uma populacao usando o método de roleta. 
    
    Nota: apenas funciona para problemas de maximizaçao.
    
    Args:
       populacao: lista com todos os individuos da populacao
       fitness: valor da função objetivo dos individuos da população
       
    Returns:
       populações dos individuos selecionados.
    '''
    populacao_selecionada = random.choices(populacao, weights = fitness, k = len(populacao)) 
    return populacao_selecionada 


def cruzamento_ponto_simples(mae, pai):
    ''' Operador de cruzamento de ponto simples.
    
    Args: 
       mae: uma lista representando um individuo
       pai: uma lista representando um individuo
       
    Return:
       Duas listas, sendo que cada uma das listas representa um filho dos pais que foram os argumentos
    '''
    ponto_de_corte = random.randint(1, len(pai)-1) #seleciona numeros inteiros dentro do intervalo, inclusive ele mesmo (tipo com intervalos usando [] fechados) e tem que ser aleatório (random)
    
    filho1 = pai [:ponto_de_corte] + mae [ponto_de_corte:]
    filho2 = mae [:ponto_de_corte] + pai [ponto_de_corte:]
    
    return filho1, filho2


def mutacao_cb(individuo):
    '''realiza a mutacao de um gene no problema das caixas binárias.
    
    Args:
      individuo: uma lista representando um individuo no problema das caixas binárias.
      
    Return:
       Um individuo com gene mutado
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo



def funcao_objetivo_pop_maternidade(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da maternidade.
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de leitos na maternidade.
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_maternidade(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado


def funcao_objetivo_maternidade(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da maternidade.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        indicando o limite de leitos na maternidade.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """

    valor_mochila, leitos_total = computa_maternidade(individuo, objetos, ordem_dos_nomes)
    peso_mochila = leitos_total
    
    
    if peso_mochila > limite:
        valor_mochila = 0.01 #problema de maximizacao, para o algoritmo nao escolher esse item
        
    return valor_mochila




