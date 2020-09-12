from functions import *

arquivo = ler_txt(entrada())

saida = escrever_txt(arquivosaida())

print("Gerando o arquivo...")

t = Tela(1)

for linha in arquivo:
    linha = linha.rstrip('\n')
    tela(linha, t.state, saida)

print("Arquivo gerado!")
