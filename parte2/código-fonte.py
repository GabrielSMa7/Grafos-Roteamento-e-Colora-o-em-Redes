def Dsatur(grafo, num_vertice):
    cores = {v: None for v in grafo} #Atribui nenhuma cor em cada vertice do grafo
    grau = {v: len(grafo[v]) for v in grafo} #Quantidade de vizinhos no grafo

    prim_v = max(grafo, key=lambda v: grau[v])
    cores[prim_v] = 1

    for _ in range(num_vertice - 1):
        saturacao = {}
        for v in grafo:
            if cores[v] == None:
                cores_vizinhos = set(cores[vizinho] for vizinho in grafo[v] if cores[vizinho] is not None)
                grau[v] = len(cores_vizinhos)
            
        prox_v = max(saturacao.keys(), key=lambda v: (saturacao[v], grau[v]))
        cor = 1
        while True:
            cores_adj = any(cores[vizinho] == cor for vizinho in grafo[prox_v])
            if not cores_adj:
                cores[prox_v] = cor
                break
            cor += 1

    num_cores = len(set(cores.values()))
    
    return num_cores, cores


def processar_grafo_parte2(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, "r") as arquivo:
        # Lê todas as linhas, remove espaços/quebras de linha e ignora as linhas vazias
        linhas = []
        for linha in arquivo:
            linha_limpa = linha.strip()
            if linha_limpa:  # Se a linha não estiver vazia
                linhas.append(linha_limpa)
    
    if not linhas:
        return

    # No formato especificado, a primeira linha já contém V e A (separados por TAB)
    num_vertices, num_arestas = map(int, list(filter(None, linhas[0].split("\t"))))

    # Construindo a lista de adjacência (mais eficiente que matriz para grafos esparsos)
    lista_adjacencia = {i: [] for i in range(num_vertices)}
    
    # Lendo as arestas (começam na linha 1 do arquivo)
    for i in range(1, num_arestas + 1):
        if i < len(linhas):
            u, v = map(int, list(filter(None, linhas[i].split("\t"))))
            # Como o grafo não é direcionado, a conexão vai nos dois sentidos
            lista_adjacencia[u].append(v)
            lista_adjacencia[v].append(u)
    
    print(lista_adjacencia)

    # --- TOMADA DE DECISÃO E EXECUÇÃO DOS ALGORITMOS ---
    # Aqui aplicamos a estratégia baseada nas características que você escolher
    if num_vertices <= 20:
        algoritmo = "Backtracking"
        justificativa = "Como o grafo possui poucos vertices, o Backtracking garante o numero cromatico exato sem estourar o tempo."
        
        #COLOCA O BACKTRACKING AQUI
    else:
        algoritmo = "DSatur"
        justificativa = "Para grafos maiores, o DSatur oferece excelente heuristica aproximada rodando em tempo polinomial."
        

    # --- ESCRITA DO ARQUIVO DE SAÍDA ---
    with open(arquivo_saida, "w") as arquivo:
        arquivo.write(f"ALGORITMO: {algoritmo}\n")
        arquivo.write(f"JUSTIFICATIVA: {justificativa}\n")
        arquivo.write(f"NUM_CORES: {num_cores}\n")
        arquivo.write(f"COLORACAO: {coloracao_str}\n")

# Executando para os dois arquivos da Parte 2
processar_grafo_parte2("grafo_wifi_p.txt", "saida_parte2_p.txt")
processar_grafo_parte2("grafo_wifi_m.txt", "saida_parte2_m.txt")