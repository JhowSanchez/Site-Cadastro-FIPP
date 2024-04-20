import sqlite3

#Executar todas as rotinas necessárias para abrir, fechar conexão emitir instruções SQL (genéricas) para o BD
class Banco():

    def __init__(self):#construtor
        self.__conexao = None
        self.__cursor = None

    def __abrirConexao(self):
        self.__conexao = sqlite3.connect("bd/Banda.db")
        self.__conexao.row_factory = sqlite3.Row #isso serve para que você possa acessar os dados pelos nomes dos atributos da tabela e não somente pela posição que eles se encontram
        self.__cursor = self.__conexao.cursor()

    def __fecharConexao(self):
        self.__cursor.close()
        self.__conexao.close()

    def executarInsertUpdateDelete(self, sql):
        # Quando não recebeu o comando de SQL para ser executado
        linhasAfetadas = -10 #variável de controle de erro...
        if len(sql) > 0:
            self.__abrirConexao()

            self.__cursor.execute(sql) #executar no banco
            linhasAfetadas = self.__cursor.rowcount #número de linhas afetadas pelo comando SQL
            self.__conexao.commit()#efetuar o sql

            self.__fecharConexao()
        return linhasAfetadas

    def executarSelect(self, sql):
        dados = ''
        if len(sql) > 0:
            self.__abrirConexao()

            self.__cursor.execute(sql)
            dados = self.__cursor.fetchall() #colocar os dados que vieram do BD no dados (retorna o resultado do select) - Lista

            self.__fecharConexao()
        return dados