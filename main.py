""""*******************************************************************************
Autor: Israel Vitor Barreto de Oliveira
Componente Curricular: Algoritmos I
Concluido em: 25/11/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************"""""

from biblioteca import * ### IMPORTA AS FUNÇÕES DE OUTRO ARQUIVO PYTHON

def main(): ### FUNÇÃO PRINCIPAL DO PROGRAMA
    dicAtleta = {} ### CRIA UM DICIONARIO VAZIO
    dicAtleta = ler_arquivo(dicAtleta) ### ADICIONA OS ARQUIVOS NO DICIONARIO
    
    while True: ### ENQUANTO FOR VERDADE
        try:
            menu(dicAtleta) ### CHAMA A FUNÇÃO DO MENU
            break ### SE O USUÁRIO NÃO DIGITAR NENHUM DADO INVÁLIDO IRÁ ENCERRAR O WHILE
        except Exception as exceção: 
            print(exceção)

if __name__ == '__main__': ### CONTROLE DE ESCOPO DE EXECUÇÃO
    main() ### CHAMA A FUNÇÃO PRINCIPAL
            

