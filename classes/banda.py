from classes.banco import *

class Banda():

    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__email = ''
        self.__genero = ''
        self.__descricao = ''
        self.__senha = ''
        self.__confirma = ''
        self.__banco = Banco()

    def set_id(self,pId):
        if (pId > 0):
            self.__id = pId

    def set_nome(self,pNome):
        if (len(pNome) > 0):
            self.__nome = pNome

    def set_email(self,pEmail):
        self.__email = pEmail

    def set_genero(self,pGenero):
        if (len(pGenero) > 0):
            self.__genero = pGenero

    def set_descricao(self,pDescricao):
        self.__descricao = pDescricao

    def set_senha(self, pSenha):
        if (len(pSenha) > 0):
            self.__senha = pSenha

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_genero(self):
        return self.__genero

    def get_descricao(self):
        return self.__descricao

    def get_senha(self):
        return self.__senha

    def obterBandas(self):
        sql = '''SELECT Id, Nome, Email, Genero, Descr, Senha
                 FROM Banda
                 ORDER BY Id
              '''
        return self.__banco.executarSelect(sql)

    def obterBanda(self,id=0):
        if id != 0:
            self.__id = id

        sql = '''SELECT Id, Nome, Email, Genero, Descr, Senha
                 FROM Banda
                 WHERE Id = #id
              '''
        sql = sql.replace('#id',str(self.__id))
        return self.__banco.executarSelect(sql)

    # vai pegar os dados do objeto e gravar no banco
    def gravar(self):
        sql = '''INSERT INTO Banda (Nome,Email,Genero,Descr,Senha)
                 VALUES("#nome","#email","#genero","#descr","#senha")'''
        sql = sql.replace('#nome', self.__nome)
        sql = sql.replace('#email', self.__email)
        sql = sql.replace('#genero', self.__genero)
        sql = sql.replace('#descr',self.__descricao)
        sql = sql.replace('#senha',str(self.__senha))
        return self.__banco.executarInsertUpdateDelete(sql)

    def excluir(self):
        sql = '''DELETE FROM Banda WHERE Id = #id'''
        sql = sql.replace('#id',str(self.__id))
        return  self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        sql = '''UPDATE Banda
                 SET Nome = "#nome", Email = "#email", Genero = "#genero", Descr = "#descr", Senha = "#senha"
                 WHERE Id = #id'''
        sql = sql.replace('#id',str(self.__id))
        sql = sql.replace('#nome', self.__nome)
        sql = sql.replace('#email', self.__email)
        sql = sql.replace('#genero', self.__genero)
        sql = sql.replace('#descr', self.__descricao)
        sql = sql.replace('#senha', str(self.__senha))
        return self.__banco.executarInsertUpdateDelete(sql)