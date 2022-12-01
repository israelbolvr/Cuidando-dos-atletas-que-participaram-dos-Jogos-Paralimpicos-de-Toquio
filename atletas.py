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


class Atletas: ### CRIA A CLASSE ATLETA
    def __init__(self, nome, idade, sexo, tipoParalisia, teveCovid, modalidade,medalhas, ouro, prata, bronze):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.tipoParalisia = tipoParalisia
        self.teveCovid = teveCovid
        self.modalidade = modalidade
        self.medalhas = medalhas
        self.ouro = ouro
        self.prata = prata
        self.bronze = bronze


    def __repr__(self): ### RETORNA UMA REPRESENTAÇÃO COMO STRING DE QUALQUER OBJETO
        return (f'\nNome: {self.nome}\nIdade: {self.idade}\nSexo: {self.sexo_atleta()}\nTipo de Paralisia: {self.tipoParalisia}\nO atleta teve covid? {self.covid()}\nModalidade: {self.modalidade.name.capitalize().replace("_", " ")}\nO atleta recebeu o total de: {self.ouro} medalhas de ouro, {self.prata} medalhas de prata,{self.bronze} medalhas de bronze.')

    @property ### DEFINE UMA PROPRIEDADE
    def nome(self):
        return self._nome ### RETORNA UM ATRIBUTO AGORA CONSIDERADO COMO "PROTEGIDO"
    
    @nome.setter ### MODIFICA O ATRIBUTO
    def nome(self, value):
        assert not value.isdigit(), "Nome inválido." ### VERIFICAÇÃO DE DADOS
        assert value != '', "Nome inválido." ### VERIFICAÇÃO DE DADOS
        self._nome = value

    @property
    def idade (self):
        return self._idade

    @idade.setter
    def idade(self, value):
        assert value.isdigit(), "Idade inválida."
        assert int(value) > 0 and int(value) < 120, 'Idade inválida.'
        self._idade = int(value)

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        assert not value.isdigit(), "Gênero inválido."
        assert value == 'F' or value == 'M', 'Gênero inválido.'
        assert value != '', "Gênero inválido."
        self._sexo = value

    @property
    def tipoParalisia(self):
        return self._tipoParalisia

    @tipoParalisia.setter
    def tipoParalisia(self, value):
        assert not value.isdigit(), "Paralisia inválida."
        assert value != '', "Paralisia inválida."
        self._tipoParalisia = value

    @property
    def teveCovid(self):
        return self._teveCovid

    @teveCovid.setter
    def teveCovid(self, value):
        assert value == 'S' or value == 'N', "Dados de Covid inválido."
        assert not value.isdigit(), "Dados de Covid inválido."
        assert value != '', "Dados de Covid inválido."
        self._teveCovid = value

    @property
    def modalidade (self):
        return self._modalidade

    @modalidade.setter
    def modalidade(self, value):
        assert value.isdigit(), "Modalidade inválida."
        assert int(value) >= 0 and int(value) <= 21, 'Modalidade inválida.'
     
        self._modalidade = Modalidade(int(value))

    @property
    def medalhas(self):
        return self._medalhas

    @medalhas.setter
    def medalhas(self,value):
        assert value == 'S' or value == 'N', 'Informação de medalhas inválidas.'
        assert not value.isdigit(), "Informação de medalhas inválidas."
        assert value != '', "Informação de medalhas inválidas."
        self._medalhas = value

    @property
    def ouro(self):
        return self._ouro

    @ouro.setter
    def ouro(self, value):
        assert value.isdigit(), "Quantidade de medalhas de ouro inválida."
        self._ouro = int(value)

    @property
    def prata(self):
        return self._prata

    @prata.setter
    def prata(self, value):
        assert value.isdigit(), "Quantidade de medalhas de prata inválida."
        self._prata = int(value)
        
    @property
    def bronze(self):
        return self._bronze

    @bronze.setter
    def bronze(self, value):
        assert value.isdigit(), "Quantidade de medalhas de bronze inválida."
        self._bronze = int(value)

    def sexo_atleta(self):
        if self.sexo == 'M': ### SE O USUÁRIO DIGITAR M EM SEXO
            return 'Masculino' ### IMPRIMIRÁ "MASCULINO" INVÉS DE "M"
        elif self.sexo == 'F':
            return 'Feminino'

    def covid(self):
        if self.teveCovid == 'S': ### SE O USUÁRIO DIGITAR S EM COVID
            return 'Sim'
        elif self.teveCovid == 'N': ### IMPRIMIRÁ "SIM" INVÉS DE "S"
            return 'Não'

     

