# Localizador De Código

Este programa é uma ferramenta desenvolvida para auxiliar na identificação de trechos de código-fonte que podem necessitar de revisão ou atualização. Dada uma pasta de código, ele busca por palavras-chave específicas dentro dos arquivos, reportando suas ocorrências.

## 🚀 Funcionalidades Implementadas

O `LocalizadorDeCodigo` oferece as seguintes funcionalidades principais:

* **Busca em Subpastas:** Percorre não apenas a pasta principal informada pelo usuário, mas também todas as suas subpastas e arquivos aninhados, garantindo uma varredura completa.
* **Busca por Múltiplas Palavras-Chave:** Permite ao usuário buscar por uma ou mais palavras-chave (separadas por vírgula), tornando a ferramenta versátil para diferentes cenários de análise de código.
* **Busca Case Insensitive:** A pesquisa pela(s) palavra(s)-chave não diferencia maiúsculas de minúsculas (ex: "CNPJ", "cnpj", "Cnpj" são tratados como iguais).
* **Detalhamento dos Resultados:** Para cada ocorrência encontrada, o programa exibe e registra:
  * O caminho completo do arquivo.
  * O número da linha onde a palavra foi encontrada.
  * O conteúdo da linha em que a ocorrência foi localizada.
* **Persistência dos Resultados:** Todos os achados da busca são automaticamente salvos em um arquivo de texto chamado `resultado.txt` na mesma pasta de execução do programa.

## 🛠️ Tecnologias Utilizadas

* **Linguagem de Programação:** Python 3.x
* **Módulos Padrão do Python:** `os` (para manipulação de caminhos e diretórios)

## 📁 Estrutura do Projeto

O projeto consiste em um único arquivo principal:

* `LocalizadorDeCodigo.py`: Contém todo o código-fonte do programa.

Para fins de teste e demonstração da funcionalidade, o repositório pode conter:
* `arquivos-testes`: Uma pasta com diversos arquivos (de diferentes extensões e em subpastas) para simular um ambiente real de busca de código.
* `resultado.txt`: O arquivo de saída gerado pelo programa após uma execução.

## ▶️ Como Usar

Para executar o `LocalizadorDeCodigo` em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

* Python instalado em seu computador.

## 🚀 Execute o Programa:

1.  Abra um terminal.
2.  Navegue até a pasta onde o arquivo `LocalizadorDeCodigo.py` está localizado.
3.  Execute o script com o comando:

    ```bash
    python LocalizadorDeCodigo.py
    ```

## O programa solicitará que você digite o caminho da pasta onde deseja iniciar a busca e, em seguida, as palavras-chave que procura.

    ### Exemplo de Uso:
    O terminal exibirá as seguintes solicitações:

    ```bash
    Digite o caminho da pasta onde estão os arquivos: C:\Projetos\MeuSistema
    Digite as palavras que deseja buscar (separadas por vírgula): cnpj, cpf, ie
    ```

5.  Os resultados serão exibidos no terminal e salvos automaticamente no arquivo `resultado.txt`, que será criado na mesma pasta onde o programa foi executado.
