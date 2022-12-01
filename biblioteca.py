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

from modalidades import *  ### IMPORTA AS FUNÇÕES DE OUTRO ARQUIVO PYTHON
from atletas import *
import jsonpickle, os ### IMPORTA OS MÓDULOS 

def ler_arquivo(dicionario): ### FUNÇÃO QUE LÊ OS ARQUIVOS GUARDADOS
    if os.path.exists('lista_atletas.json'): ### SE O ARQUIVO EXISTIR NO SISTEMA
        try:
            arquivo = open('lista_atletas.json', 'r') ### ABRE O ARQUIVO E O LÊ
            dicionario = jsonpickle.decode(arquivo.read()) 
            arquivo.close() ### FECHA O ARQUIVO
        except: ### SE O ARQUIVO NÃO EXISTIR
            print('Ainda não foi cadastrado nenhum atleta.')

    return dicionario

def adiciona_arquivo(dicionario): ### CRIA UM NOVO ARQUIVO/SOBRESCREVE O ARQUIVO QUE JÁ EXISTE
    arquivo = open('lista_atletas.json', 'w') ### ABRE O ARQUIVO E ESCREVE
    arquivo.write(jsonpickle.encode(dicionario))
    arquivo.close() ### FECHA O ARQUIVO

def entrada(): ###FUNÇÃO QUE IMPRIME O ÍNICIO DO PROGRAMA
    print()
    print("", "_" * 45)
    print("|", " " * 43, "|", "\n|      CADASTRO DE ATLETAS PARALIMPICOS       |\n|"," "  * 43, "|")
    print("","‾" * 45)
    

def printar_entrada(): ### FUNÇÃO QUE IMPRIME AS OPÇÕES DO MENU
    print('''Bem vindo ao cadastro de atletas.\n
Para cadastrar um novo atleta, digite 1.
Para editar o cadastro de um atleta, digite 2.
Para excluir um atleta cadastrado, digite 3.
Para mostrar as informações de todos os atletas, digite 4.
Para mostrar os resultados, digite 5.   
    ''')

def printar_menu(): ### FUNÇÃO QUE IMPRIME AS OPÇÕES DO MENU
    print('''\nOpção 1: Cadastrar novo atleta.
Opção 2: Editar atleta.
Opção 3: Remover atleta.
Opção 4: Visualizar informação de todos os atletas.
Opção 5: Resultados do programa.\n''')

def printarModalidade(dicionario):
    atletas = ler_arquivo(dicionario)
    modalidades = [0 for i in range(22)]

    for atleta in atletas.values():
        modalidades[atleta.modalidade.value] += 1

    for quantidade in range(len(modalidades)):
        print(f'{quantidade}: {Modalidade(quantidade).name.capitalize().replace("_", " ")}')

def entradaDados(dicionario): ### FUNÇÃO QUE RECEBE OS DADOS DO ATLETA.
    ouro,prata,bronze = '0','0','0' ### OURO, PRATA E BRONZE PADRONIZADOS COMO '0'.
    continuar = 'S'
    while continuar == 'S': ### ENQUANTO CONTINUAR FOR SIM.
        atleta = None
        while atleta is None: ### ENQUANTO O ATLETA NÃO FOR CADASTRADO O PROGRAMA IRÁ SE REPETIR.
            print(f'\nEntre com os dados do atleta:')  
            nome = input('Digite o nome do atleta: ').title() ### SOLICITA O NOME DO ATLETA.
            if nome in dicionario.keys(): ### SE O NOME JÁ ESTIVER NO DICIONÁRIO O ATLETA NÃO VAI SER CADASTRADO, POIS, JÁ EXISTE.
                print('Atleta já está cadastrado.')
                break ### E ENCERRA O CADASTRO.
            idade = input('Digite a idade: ') ### SOLICITA A IDADE DO ATLETA.
            sexo = input('Digite o sexo do atleta[M/F]: ').upper() ### SOLICITA O SEXO DO ATLETA.
            tipoParalisia = input('Digite a paralisia: ').title() ### SOLICITA O TIPO DE PARALISIA DO ATLETA.
            teveCovid = input('O atleta teve covid? [S/N]: ').upper() ### SOLICITA SE O ATLETA TEVE COVID OU NÃO.
            verModalidade = input('Deseja ver o menu de modalidades[S/N]: ').strip().upper()[0] ### SOLICITA SE O USUÁRIO QUER VER A LISTA DE MODALIDADES.
            assert verModalidade.isalpha(), 'Digite a opção de ver modalidade corretamente.'
            assert verModalidade == 'S' or verModalidade == 'N', 'Digite a opção de ver modalidade corretamente.'
            assert verModalidade != '', 'Digite a opção de ver modalidade corretamente.'
            if verModalidade == 'S':
                print(printarModalidade(dicionario))
            modalidade = input('Digite a modalidade de acordo com o número correspondente [0/21]: ') ### SOLICITA A MODALIDADE DO ATLETA.
            medalhas = input('O atleta ganhou medalhas? [S/N]: ').upper() ### SOLICITA SE O ATLETA GANHOU MEDALHAS.
            if medalhas == 'S': ### SE O ATLETA GANHOU MEDALHAS
                ouro = input("O atleta ganhou alguma medalha de ouro? Se sim, quantas? ") ### SOLICITA QUANTAS DE OURO O ATLETA GANHOU.
                prata = input("O atleta ganhou alguma medalha de prata? Se sim, quantas? ") ### SOLICITA QUANTAS DE PRATA O ATLETA GANHOU.
                bronze = input("O atleta ganhou alguma medalha de bronze? Se sim, quantas? ") ### SOLICITA QUANTAS DE BRONZE O ATLETA GANHOU.
            try: ### SE TODAS AS INFORMAÇÕES ESTIVEREM CORRETAS
                atleta = Atletas(nome, idade, sexo, tipoParalisia, teveCovid, modalidade, medalhas, ouro, prata, bronze) 
                dicionario[atleta.nome] = atleta ### O ATLETA VAI SER CADASTRADO NO DICIONÁRIO.
            except Exception as exceção: ### SE OS DADOS NÃO FOREM DIGITADOS CORRETAMENTE O ATLETA NÃO SERÁ CADASTRADO E O PROGRAMA IRÁ SE REPETIR.
                print(exceção) ### VAI PRINTAR O ERRO.
        continuar = input('Deseja cadastrar outro atleta? ').strip().upper()[0] ### SOLICITA SE O USUÁRIO QUER CADASTRAR OUTRO ATLETA.
        while continuar not in 'SN':
            continuar = input("Opção inválida. Digite a opção corretamente [S/N]: ").strip().upper()[0]
        
    return dicionario

def atualizar_atleta(dicionario): ### FUNÇÃO QUE ATUALIZA OS DADOS DO ATLETA
    ouro,prata,bronze = '0','0','0'
    atleta = None
    while atleta is None:
        print(f'Entre com os dados do atleta: ')  
        nome = input('Digite o nome do atleta: ').title()
        if nome in dicionario.keys():
                print('Atleta já está cadastrado.')
                break
        idade = input('Digite a idade: ')
        sexo = input('Digite o sexo do atleta [M/F]: ').upper()
        tipoParalisia = input('Digite a paralisia: ')
        teveCovid = input('O atleta teve covid? [S/N]: ').upper()
        verModalidade = input('Deseja ver o menu de modalidades[S/N]: ')
        assert verModalidade.isalpha(), 'Digite a opção de ver modalidade corretamente.'
        assert verModalidade == 'S' or verModalidade == 'N', 'Digite a opção de ver modalidade corretamente.'
        assert verModalidade != '', 'Digite a opção de ver modalidade corretamente.'
        if verModalidade == 'S':
            print(printarModalidade(dicionario))
        modalidade = input('Digite a modalidade de acordo com o número correspondente [0/21]: ')
        medalhas = input('O atleta ganhou medalhas? [S/N]: ').upper()
        if medalhas == 'S':
                ouro = input("O atleta ganhou alguma medalha de ouro? Se sim, quantas? ")
                prata = input("O atleta ganhou alguma medalha de prata? Se sim, quantas? ")
                bronze = input("O atleta ganhou alguma medalha de bronze? Se sim, quantas? ")
        try:
            atleta = Atletas(nome, idade, sexo, tipoParalisia, teveCovid, modalidade, medalhas, ouro, prata, bronze)
            dicionario[atleta.nome] = atleta               
        except Exception as exceção:
            print(exceção)

    return dicionario

def menu(dicionario): ### FUNÇÃO QUE EXECUTA O MENU DO PROGRAMA
    entrada()
    continuar = 'S'
    while continuar == 'S':
        printar_menu()
        menu = input('Digite a opção desejada: ') ### SOLICITA A OPÇÃO QUE O USUÁRIO QUER NO MENU
        assert menu.isdigit(), 'Opção inválida' ### VERIFICAÇÃO DE DADOS
        menu = int(menu) ### TRANSFORMA STRING EM INTEIRO
        assert int(menu) > 0 and int(menu) <= 5, 'Opção inválida' ### VERIFICAÇÃO DE DADOS
        if menu == 1: ### SE A OPÇÃO FOR 1
            dicionario = ler_arquivo(dicionario) ### VAI LER O ARQUIVO
            while True:
                try:
                    dicionario = entradaDados(dicionario) ### VAI CHAMAR A FUNÇÃO DE CADASTRAR O ATLETA
                    adiciona_arquivo(dicionario) ### VAI CADASTRAR O NOVO ATLETA NO ARQUIVO
                    break
                except Exception as exceção:
                    print(exceção)
        elif menu == 2: ### SE A OPÇÃO FOR 2
            dicAtleta = ler_arquivo(dicionario)   
            editar = input('Qual atleta deseja editar? ').title() ### SOLICITA AO USUÁRIO QUAL ATLETA ELE QUER EDITAR
            if editar in dicAtleta.keys(): ### VERIFICA SE O ATLETA DIGITADO ESTÁ CADASTRADO
                del dicionario[editar]
                while True:
                    try:
                        atualizar_atleta(dicionario) ### CHAMA A FUNÇÃO QUE VAI EDITAR OS DADOS DO ATLETA 
                        adiciona_arquivo(dicionario) ### ADICIONA OS NOVOS DADOS AO ARQUIVO
                        break
                    except Exception as exceção:
                        print(exceção)
            else: ### SE ELE NÃO ESTIVER CADASTRADO
                print('Este atleta não está cadastrado.')
        elif menu == 3: ### SE A OPÇÃO FOR 3
            dicionario = ler_arquivo(dicionario)
            remover = input('Qual atleta deseja remover? ').title() ### SOLICITA AO USUÁRIO QUAL ATLETA ELE QUER REMOVER
            if remover in dicionario.keys(): ### VERIFICA SE O ATLETA DIGITADO ESTÁ CADASTRADO
                print(f'{dicionario[remover].nome} foi removido da lista!') 
                dicionario.pop(remover) ### REMOVE O USUÁRIO
                adiciona_arquivo(dicionario) ### ATUALIZA O ARQUIVO 
            else: ### SE ELE NÃO ESTIVER CADASTRADO
                printa('Este atleta não está cadastrado.')
        elif menu == 4: ### SE A OPÇÃO FOR 4
            dicionario = ler_arquivo(dicionario)
            printa(dicionario) ### VAI IMPRIMIR AS INFORMAÇÕES DE TODOS OS ATLETAS
        elif menu == 5: ### SE A OPÇÃO FOR 5
            respostas = input('\nQual questão deseja visualizar? [1/2/3/4/5]: ')  ### SOLICITA AO USUÁRIO QUAL RESPOSTA ELE QUER VER
            assert respostas.isdigit(), 'Opção inválida' ### VERIFICAÇÃO DE DADOS
            respostas = int(respostas)
            assert int(respostas) > 0 and int(respostas) <= 5, 'Opção inválida. Digite novamente'      
            if respostas == 1: ### SE A RESPOSTA FOR 1
                questao1(dicionario) ### IMPRIMIRÁ NA TELA A RESPOSTA DA QUESTÃO 1
            elif respostas == 2:
                questao2(dicionario)
            elif respostas == 3:
                questao3(dicionario)
            elif respostas == 4:
                questao4(dicionario)
            elif respostas == 5:
                questao5(dicionario)
        continuar = input('Deseja continuar? ').strip().upper()[0]
        while continuar not in 'SN':
            continuar = input("Opção inválida. Digite a opção corretamente [S/N]: ").strip().upper()[0]
        if continuar == 'N':
            print('\n\nPrograma encerrado.')

def printa(dicionario): ### FUNÇÃO QUE VAI IMPRIMIR AS INFORMAÇÕES NA TELA
    dicionario = ler_arquivo(dicionario)
    for chave in dicionario: ### VAI LER OS ELEMENTOS NO DICIONÁRIO
        print(f'\nAtleta: {chave}')
        atleta = dicionario[chave]
        print('Nome do atleta:',atleta.nome.title())
        print('A idade do atleta é:',atleta.idade)
        print('O sexo do atleta é:', atleta.sexo_atleta())
        print('O tipo de paralisia do atleta é:', atleta.tipoParalisia.title())
        print('O atleta teve covid?', atleta.covid().title())
        print('A modalidade do atleta foi:', atleta.modalidade.name.capitalize().replace("_", " "))
        print(f'O atleta recebeu o total de: {atleta.ouro} medalhas de ouro, {atleta.prata} medalhas de prata, {atleta.bronze} medalhas de bronze.\n')

def questao1(dicionario): ### FUNÇÃO DA QUESTÃO 1
    atletas = ler_arquivo(dicionario) ### ARMAZENA OS DADOS DO ARQUIVO EM UMA VARIÁVEL
    sexo_masculino = [0 for i in range(22)] ### VAI CRIAR UMA LISTA COM 22 ZEROS
    sexo_feminino = [0 for i in range(22)]
    for atleta in atletas.values(): ### PARA CADA ELEMENTO NO DICIONÁRIO
        if atleta.sexo == "F": ### SE O SEXO DO ATLETA FOR "F" (FEMININO)
            sexo_feminino[atleta.modalidade.value]+= 1 ### VAI SER ADICIONADO + 1 À CADA ÍNDICE CORRESPONDENTE DA CLASSE DE MODALIDADE
        else:
            sexo_masculino[atleta.modalidade.value]+= 1
    for quantidade in range(len(sexo_feminino)): ### PARA CADA ELEMENTO NO INTERVALO DO TAMANHO DA LISTA
        if sexo_feminino[quantidade] > 0: ### SE O ELEMENTO TIVER UM VALOR MAIOR QUE 0
            print(f'A quantidade de atletas femininas que participaram da modalidade {Modalidade(quantidade).name.capitalize().replace("_", " ")} foi: {sexo_feminino[quantidade]}')   
    for quantidade in range(len(sexo_masculino)):
        if sexo_masculino[quantidade] > 0:
            print(f'A quantidade de atletas masculinos que participaram da modalidade {Modalidade(quantidade).name.capitalize().replace("_", " ")} foi: {sexo_masculino[quantidade]}')

def questao2(dicionario): ### FUNÇÃO DA QUESTÃO 2
    atletas = ler_arquivo(dicionario)
    sexo_masculino = [0 for i in range(22)]
    sexo_feminino = [0 for i in range(22)]
    for atleta in atletas.values():
        if atleta.sexo == 'F' and atleta.teveCovid == 'S': ### SE FOR O ATLETA FOR MULHER E SE O ATLETA APRESENTOU COVID
            sexo_feminino[atleta.modalidade.value]+= 1
        if atleta.sexo == 'M' and atleta.teveCovid == 'S': ### SE FOR O ATLETA FOR HOMEM E SE O ATLETA APRESENTOU COVID
            sexo_masculino[atleta.modalidade.value]+= 1
    for quantidade in range(len(sexo_feminino)):
        if sexo_feminino[quantidade] > 0:
            print(f'A quantidade de atletas femininas que teve covid e que participaram da modalidade {Modalidade(quantidade).name.capitalize().replace("_", " ")} foi: {sexo_feminino[quantidade]}')
    for quantidade in range(len(sexo_masculino)):
        if sexo_masculino[quantidade] > 0:
            print(f'A quantidade de atletas masculinos que teve covid e que participaram da modalidade {Modalidade(quantidade).name.capitalize().replace("_", " ")} foi: {sexo_masculino[quantidade]}')

def questao3(dicionario): ### FUNÇÃO DA QUESTÃO 3
    atletas = ler_arquivo(dicionario)
    listaMedalhas = [[0 for c in range(3)] for l in range(22)] ### CRIARÁ UMA "MATRIZ" COM 3 COLUNAS E 22 LINHAS
    for atleta in atletas.values():
        if atleta.medalhas == 'S': ### SE O ATLETA GANHOU MEDALHAS
            listaMedalhas[atleta.modalidade.value][0] += atleta.ouro
            listaMedalhas[atleta.modalidade.value][1] += atleta.prata
            listaMedalhas[atleta.modalidade.value][2] += atleta.bronze


    for quantidade in range(len(listaMedalhas)):
        if listaMedalhas[quantidade][0] > 0 or listaMedalhas[quantidade][1] > 0 or listaMedalhas[quantidade][2] > 0:
            print(f'A quantidade de medalhas que os atletas da modalidade {Modalidade(quantidade).name.capitalize().replace("_", " ")} sendo elas: {listaMedalhas[quantidade][0]} medalhas de ouro, {listaMedalhas[quantidade][1]} medalhas de prata, {listaMedalhas[quantidade][2]} medalhas de bronze.')
      
def questao4(dicionario): ### FUNÇÃO DA QUESTÃO 4
    atletas = ler_arquivo(dicionario)
    sexo_masculino = [0 for i in range(22)]
    sexo_feminino = [0 for i in range(22)]
    for atleta in atletas.values():
        if atleta.sexo == "F" and atleta.medalhas == 'S': ### SE FOR O ATLETA FOR MULHER E SE O ATLETA GANHOU MEDALHAS
            sexo_feminino[atleta.modalidade.value]+= 1
        if atleta.sexo == 'M' and atleta.medalhas == 'S':
            sexo_masculino[atleta.modalidade.value]+= 1
    for quantidade in range(len(sexo_feminino)):
        if sexo_feminino[quantidade] > 0:
            print(f'A quantidade de atletas femininas que participaram da modalidade {Modalidade(quantidade).name.capitalize().replace("_", " ")} e ganharam medalhas foi: {sexo_feminino[quantidade]}')
    for quantidade in range(len(sexo_masculino)):
        if sexo_masculino[quantidade] > 0:
            print(f'A quantidade de atletas masculinos que participaram da modalidade {Modalidade(quantidade).name.capitalize().replace("_", " ")} e ganharam medalhas foi: {sexo_masculino[quantidade]}')
    consultarInfo = input('\nDeseja consultar as informações dos atletas? [S/N]: ').strip().upper()[0] ### SOLICITA SE O USUÁRIO QUER VER AS INFORMAÇÕES DOS ATLETAS QUE GANHARAM MEDALHAS
    assert consultarInfo == 'S' or consultarInfo == 'N', 'Entrada de dados inválida.' ### VERIFICAÇÃO DE DADOS
    while consultarInfo not in 'SN':
        consultarInfo = input("Opção inválida. Digite a opção corretamente [S/N]: ").strip().upper()[0]
    if consultarInfo == 'S': ### SE O USUÁRIO QUISER VER AS INFORMAÇÕES
        print('\n************************INFORMAÇÕES DOS ATLETAS ABAIXO ************************')
        for chave in atletas:
            atleta = atletas[chave]
            if atleta.medalhas == 'S':
                print(f'\nAtleta: {chave}')
                print('Nome do atleta:',atleta.nome)
                print('A idade do atleta é:',atleta.idade)
                print('O sexo do atleta é:', atleta.sexo_atleta())
                print('O tipo de paralisia do atleta é:', atleta.tipoParalisia)
                print('O atleta teve covid?', atleta.teveCovid)
                print('A modalidade do atleta foi:', atleta.modalidade.name.capitalize().replace("_", " "))
                print(f'O atleta recebeu o total de: {atleta.ouro} medalhas de ouro, {atleta.prata} medalhas de prata, {atleta.bronze} medalhas de bronze.\n')

def questao5(dicionario): ### FUNÇÃO DA QUESTÃO 5
    atletas = ler_arquivo(dicionario)
    modalidades = [0 for i in range(22)]
    listaParticipou = []
    lista_naoParticipou = []
    listaParticipouMedalha = []
    listaParticipou_SemMedalha = []

    for atleta in atletas.values():
        if atleta.sexo == 'F' or atleta.sexo == 'M': ### SE FOR HOMEM OU MULHER
            modalidades[atleta.modalidade.value] += 1 ### VAI SER ADICIONADO + 1 À CADA ÍNDICE CORRESPONDENTE DA CLASSE DE MODALIDADE
        if atleta.medalhas == 'S': ### SE O ATLETA GANHOU MEDALHA
            if atleta.modalidade.value not in listaParticipouMedalha: ### SE A MODALIDADE JÁ NÃO ESTIVER ADICIONADA
                listaParticipouMedalha.append(atleta.modalidade.value) ### VAI ADICIONAR A MODALIDADE
                if (atleta.modalidade.value in listaParticipouMedalha) and (atleta.modalidade.value in listaParticipou_SemMedalha): ### SE A MODALIDADE ESTIVER NAS 2 LISTAS
                    listaParticipou_SemMedalha.remove(atleta.modalidade.value) ### MODALIDADE CORRESPONDENTE IRÁ SER REMOVIDA DA LISTA DOS QUE NÃO GANHARAM MEDALHAS
        elif atleta.medalhas == 'N':  ### SE O ATLETA NÃO GANHOU MEDALHA
            if (atleta.modalidade.value not in listaParticipou_SemMedalha) and (atleta.modalidade.value not in listaParticipouMedalha): ### SE NÃO ESTIVER EM NENHUMA DAS 2 LISTAS 
                listaParticipou_SemMedalha.append(atleta.modalidade.value) ### MODALIDADE CORRESPONDENTE IRÁ SER ADICIONADA NA LISTA DOS QUE NÃO GANHARAM MEDALHAS
            
            
    for quantidade in range(len(modalidades)):
        if modalidades[quantidade] > 0:
            listaParticipou.append(quantidade)
        if modalidades[quantidade] == 0:
            lista_naoParticipou.append(quantidade)
    
    

    print('************* QUADRO DE MEDALHAS DO BRASIL *************\n')
    print(f'Das 22 modalidades, o Brasil teve participação em {len(listaParticipou)}.')
    print('\n********************************************************')
    if listaParticipouMedalha:
        print(f'\nDas que participou, o Brasil ganhou medalhas em: {len(listaParticipouMedalha)}.\nSendo elas:\n')
        for quantidade in listaParticipouMedalha:
            print(f'{Modalidade(quantidade).name.capitalize().replace("_", " ")}')
    if listaParticipou_SemMedalha:
        print('\n********************************************************\n')
        print(f'Das que participou, o Brasil não ganhou medalhas em: {len(listaParticipou_SemMedalha)}.\nSendo elas:\n')
        for quantidade in listaParticipou_SemMedalha:
            print(f'{Modalidade(quantidade).name.capitalize().replace("_", " ")}')
    if lista_naoParticipou:
        print('\n********************************************************\n')
        print(f'O Brasil não teve participação em: {len(lista_naoParticipou)} modalidades.\nSendo elas:\n')
        for quantidade in lista_naoParticipou:
            print(f'{Modalidade(quantidade).name.capitalize().replace("_", " ")}')



    '''for quantidade in range(len(modalidades)):
        if modalidades[quantidade] == 0:
            print(f'{Modalidade(quantidade).name.capitalize().replace("_", " ")}', end = ', ')'''
    print()



