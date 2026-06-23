def Dsatur(grafo, num_vertice):
    cores = {v: None for v in grafo} 
    grau = {v: len(grafo[v]) for v in grafo} 

    prim_v = max(grafo, key=lambda v: grau[v])
    cores[prim_v] = 1

    for _ in range(num_vertice - 1):
        saturacao = {}
        for v in grafo:
            if cores[v] is None: # Ajustado para 'is None'
                cores_vizinhos = set(cores[vizinho] for vizinho in grafo[v] if cores[vizinho] is not None)
                saturacao[v] = len(cores_vizinhos) # CORRIGIDO: Populando saturacao
        
        prox_v = max(saturacao.keys(), key=lambda v: (saturacao[v], grau[v]))
        cor = 1
        while True:
            cores_adj = any(cores[vizinho] == cor for vizinho in grafo[prox_v])
            if not cores_adj:
                cores[prox_v] = cor
                break
            cor += 1

    num_cores = len(set(cores.values()))
    cores_str = " ".join([f"{v}={cores[v]}" for v in sorted(cores.keys())])
    return num_cores, cores_str

def backtracking(v, num_cores, cores, lista_adjacencia, num_vertices):
    if v == num_vertices:
        return True
    for cor in range(1, num_cores + 1):
        if eh_seguro(v, cor, cores, lista_adjacencia):
            cores[v] = cor
            if backtracking(v + 1, num_cores, cores, lista_adjacencia, num_vertices):
                return True
            cores[v] = 0
    return False

def colorir_grafo(lista_adjacencia, num_cores):
    num_vertices = len(lista_adjacencia)
    cores = [0] * num_vertices

    if backtracking(0, num_cores, cores, lista_adjacencia, num_vertices):
        return cores
    else:
        return None
    
def encontrar_num_cores(lista_adjacencia):
    num_vertices = len(lista_adjacencia)
    for num_cores in range(1, num_vertices + 1):
        coloracao = colorir_grafo(lista_adjacencia, num_cores)
        if coloracao is not None:
            coloracao_str = " ".join([f"{i}={cor}" for i, cor in enumerate(coloracao)])
            return num_cores, coloracao_str
    return num_vertices, None

def eh_seguro(v, cor, cores, lista_adjacencia):
    for vizinho in lista_adjacencia[v]:
        if cores[vizinho] == cor:
            return False
    return True

def processar_grafo_parte2(arquivo_entrada, arquivo_saida):
    arquivo_entrada = arquivo_entrada.strip('"')
    
    with open(arquivo_entrada, "r") as arquivo:
        linhas = []
        for linha in arquivo:
            linha_limpa = linha.strip()
            if linha_limpa:  
                linhas.append(linha_limpa)
    
    if not linhas:
        return

    num_vertices, num_arestas = map(int, list(filter(None, linhas[0].split("\t"))))
    lista_adjacencia = {i: [] for i in range(num_vertices)}
    
    for i in range(1, num_arestas + 1):
        if i < len(linhas) and "\t" in linhas[i]:
            u, v = map(int, list(filter(None, linhas[i].split("\t"))))
            lista_adjacencia[u].append(v)
            lista_adjacencia[v].append(u)
    
    # --- TOMADA DE DECISÃO ---
    if num_vertices <= 20:
        algoritmo = "Backtracking"
        justificativa = "Como o grafo possui poucos vertices, o Backtracking garante o numero cromatico exato sem estourar o tempo."
        num_cores, coloracao_str = encontrar_num_cores(lista_adjacencia)
    else:
        algoritmo = "DSatur"
        justificativa = "Para grafos maiores, o DSatur oferece excelente heuristica aproximada rodando em tempo polinomial."
        num_cores, coloracao_str = Dsatur(lista_adjacencia, num_vertices)

    # --- ESCRITA DO ARQUIVO DE SAÍDA ---
    with open(arquivo_saida, "w") as arquivo:
        arquivo.write(f"ALGORITMO: {algoritmo}\n")
        arquivo.write(f"JUSTIFICATIVA: {justificativa}\n")
        arquivo.write(f"NUM_CORES: {num_cores}\n")
        arquivo.write(f"COLORACAO: {coloracao_str}\n")
    
arq_input = input("Caminho do arquivo para ser analisado: ").strip('"')
processar_grafo_parte2(arq_input, "saida_parte2.txt")