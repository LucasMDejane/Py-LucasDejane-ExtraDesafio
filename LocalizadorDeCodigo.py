import os

caminho = input("Digite o caminho da pasta onde estão os arquivos: ")

palavras = input("Digite as palavras que deseja buscar (separadas por vírgula): ")

# cria uma lista com as palavras todas em minusculas
palavras_chave = [palavra.strip().lower() for palavra in palavras.split(',') if palavra.strip()]

print("\nBuscando pelas palavras:", palavras_chave)
print("Na pasta:", os.path.abspath(caminho), "\n")

# abre o arquivo onde os resultados serao salvos
with open("resultado.txt", "w", encoding="utf-8") as arquivo_resultado:
    registros_encontrados = 0  # contador de registros
    
    # corre todas as pastas e arquivos
    for raiz, pastas, arquivos in os.walk(caminho):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)
            
            try:
                # abre o arquivo como texto
                with open(caminho_completo, "r", encoding="utf-8", errors="ignore") as arquivo:
                    
                    # ve cada linha do arquivo
                    for numero_linha, linha in enumerate(arquivo, start=1):
                        linha_minuscula = linha.lower()
                        
                        # valida se alguma das palavras esta na linha
                        for palavra in palavras_chave:
                            if palavra in linha_minuscula:
                                texto = (
                                    f"Arquivo: {caminho_completo}\n"
                                    f"Linha: {numero_linha}\n"
                                    f"Conteúdo: {linha.strip()}\n"
                                    f"{'-'*40}\n"
                                )
                                print(texto)
                                arquivo_resultado.write(texto)
                                registros_encontrados += 1
                                break

            except Exception as erro:
                print(f"Erro ao ler o arquivo: {caminho_completo}")
                print(f"Motivo: {erro}")

print(f"\nBusca finalizada! Os resultados foram salvos no arquivo resultado.txt.")
print(f"Número total de registros encontrados: {registros_encontrados}")