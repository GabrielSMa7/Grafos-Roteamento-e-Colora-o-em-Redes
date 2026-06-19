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