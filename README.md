# Similaridade entre Textos - Análise de Keywords e Comparação

Este script em Python foi desenvolvido como parte de um trabalho acadêmico para a disciplina de Tópicos Especiais 2 do curso de Tecnologia em Análise e Desenvolvimento de Sistemas.

## Sobre o Projeto

O objetivo deste projeto é calcular a similaridade entre dois textos fornecidos como entrada, realizando as seguintes etapas:

- Extração de palavras-chave: Identificação dos termos mais comuns nos textos.
- Limpeza de dados: Remoção de stopwords, caracteres especiais e plural (opcional).
- Possibilidade de considerar sinônimos na análise.
- Cálculo da oclusão dos termos nos arrays gerados.

## Pré-requisitos

- Python 3.x
- Biblioteca NLTK

## Utilização

1. Clone o repositório para o seu ambiente local.
2. Instale as dependências necessárias: `pip install -r requirements.txt`.
3. Execute o script Python, fornecendo os caminhos para os dois arquivos de texto como entrada.

Exemplo de uso:

```bash
python similarity_analysis.py arquivo_texto1.txt arquivo_texto2.txt
