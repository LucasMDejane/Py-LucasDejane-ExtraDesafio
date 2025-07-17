# Desafio Técnico - Localizador de Código

## Introdução

A partir de 2026, a legislação brasileira permitirá o uso de CNPJs com letras e números (exemplo: A12.345.678/0001-Z9). Atualmente, a maioria dos sistemas aceita apenas CNPJs numéricos, o que pode causar problemas. 

Este desafio propõe a criação de uma ferramenta simples para localizar no código fontes os trechos onde o CNPJ está sendo tratado como somente numérico.

## Descrição do Desafio

Crie um programa chamado `LocalizadorDeCodigo` que:

1. Solicite ao usuário o caminho de uma pasta contendo arquivos de código-fonte.
2. Procure pela palavra "cnpj" dentro dos arquivos.
3. Para cada ocorrência encontrada, exiba:
   - Caminho completo do arquivo
   - Número da linha
   - Conteúdo da linha

## Requisitos

- O programa pode ser feito na linguagem de sua escolha (Python, C#, JavaScript, etc).
- A busca por "cnpj" deve ser **case insensitive** (ex: "CNPJ", "cnpj", "Cnpj", etc).
- O programa não deve travar ao encontrar arquivos binários ou protegidos.

## Pontos Extras (opcional)

Se desejar, você pode incluir:
- Busca também nas subpastas.
- Opção de buscar outras palavras além de "cnpj", como "cpf", "ie", etc.
- Salvamento dos resultados encontrados em um arquivo chamado `resultado.txt`.

## Entrega Esperada

- Código-fonte funcional do programa.
- Instruções simples de como executá-lo.
- Se possível, prints ou exemplo de execução funcionando no seu ambiente.