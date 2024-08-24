import itertools

def processa_operacao(operacao, conjunto1, conjunto2):
    if operacao == 'U':
        resultado = sorted(set(conjunto1).union(set(conjunto2)))
        return f"Uniao: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
    elif operacao == 'I':
        resultado = sorted(set(conjunto1).intersection(set(conjunto2)))
        return f"Intersecao: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
    elif operacao == 'D':
        resultado = sorted(set(conjunto1).difference(set(conjunto2)))
        return f"Diferenca: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
    elif operacao == 'C':
        resultado = sorted(itertools.product(conjunto1, conjunto2))
        return f"Produto cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
    else:
        return "Operacao nao reconhecida"

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    num_operacoes = int(linhas[0].strip())
    indice_linha = 1
    resultados = []
    
    for i in range(num_operacoes):
        operacao = linhas[indice_linha].strip()
        conjunto1 = [x.strip() for x in linhas[indice_linha + 1].strip().split(',')]
        conjunto2 = [x.strip() for x in linhas[indice_linha + 2].strip().split(',')]
        resultado = processa_operacao(operacao, conjunto1, conjunto2)
        resultados.append(resultado)
        indice_linha += 3
    
    return resultados

def escrever_arquivo_saida(resultados, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w') as arquivo:
        for resultado in resultados:
            arquivo.write(resultado + '\n')

nome_arquivo_entrada = input("Digite o caminho para o arquivo de entrada: ")
nome_arquivo_saida = input("Digite o caminho e o nome .txt que deseja para gerar um .txt com o resultado: ")

resultados = ler_arquivo(nome_arquivo_entrada)
escrever_arquivo_saida(resultados, nome_arquivo_saida)

print("O arquivo de texto com o resultado foi gerado.")