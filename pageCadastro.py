import cherrypy
from classes.banda import *

class PaginaCadastro():
    topo = open("html/cabecalho.html").read()
    rodape = open("html/rodape.html").read()

    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()

    def montaFormulario(self,pId=0,pNome='',pEmail='',pGenero='',pDescricao='',pSenha='',pConfirma=''):
        html = self.topo
        html += '''
				<form action="gravarBanda" method="post">
                    <input type="hidden" id="txtId" name="txtId" value="%s"/>
                    <input class="text" type="text" id="txtNome" name="txtNome" placeholder="Nome" required="" value="%s">
                    <input class="text email" type="email" id="txtEmail" name="txtEmail" placeholder="Email" required="" value="%s">
                    <input class="text email" type="text" id="txtGenero" name="txtGenero" placeholder="Genero Musical" required="" value="%s">
                    <input class="text email" type="text" id="txtDescr" name="txtDescr" placeholder="Descriçao" required="" value="%s">
                    <input class="text" type="password" id="txtSenha" name="txtSenha" placeholder="Senha" required="" value="%s">
                    <input class="text w3lpass" type="password" id="txtConfirma" name="txtConfirma" placeholder="Confirme a senha"
                        required="" value="%s">
                    <div class="wthree-text">
                        <label class="anim">
                            <input type="checkbox" class="checkbox" required="">
                            <span>Aceito os termos e condiçoes</span>
                        </label>
                        <div class="clear"> </div>
                    </div>
                    <input type="submit" id="btnGravar" name="btnGravar" value="Cadastrar">
                </form>
                ''' % (pId, pNome, pEmail, pGenero, pDescricao, pSenha, pConfirma)
        html += self.montaTabela()
        html += self.rodape
        return html

    def montaTabela(self):
        html = '''<table class="alinha">
                      <tr>
                          <th> ID </th>
                          <th> Nome da Banda </th>
                          <th> Email da Banda </th>
                          <th> Gênero da Banda </th>
                          <th> Descrição da Banda </th>
                          <th> Ações </th>
                      </tr>'''

        objBanda = Banda()
        dados = objBanda.obterBandas()
        for banda in dados:
            html += ''' <tr>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td> %s </td>
                           <td style="text-align: center"> 
                            <a href ="excluirBanda?idBanda=%s">
                            <input class="excluir" value="Excluir">
                            </a>
                            <a href ="alterarBanda?idBanda=%s">
                            <input class="alterar" value="Alterar">
                            </a>
                           </td>
                       </tr>''' % (banda["Id"],banda["Nome"],banda["Email"],banda["Genero"],banda["Descr"],banda["Id"],banda["Id"])
        html += '</table> <br/> <br/>'
        return html

    @cherrypy.expose()
    def gravarBanda(self,txtId,txtNome,txtEmail,txtGenero,txtDescr,txtSenha,txtConfirma,btnGravar):
        if len(txtNome) > 0 and len(txtGenero) > 0 and len(txtSenha) > 0:
            objBanda = Banda   ()
            objBanda.set_nome(txtNome)
            objBanda.set_email(txtEmail)
            objBanda.set_genero(txtGenero)
            objBanda.set_descricao(txtDescr)
            objBanda.set_senha(txtSenha)
            retorno = 0 # variável para controlar o sucesso!
            if int(txtId) == 0: # novo registro no banco
                retorno = objBanda.gravar()
            else: # gravar a alteração de um registro
                # neste caso da alteração a gente precisa carregar o id no objeto, quando é uma nova espécie não precisa porque o id é gerado de forma automática
                objBanda.set_id(int(txtId))
                retorno = objBanda.alterar()
            if retorno > 0:
                return '''
                    <script>
                        alert("A banda %s foi gravada com sucesso!!");
                        window.location.href = "/cadastro"
                    </script>
                ''' % (txtNome)
            else:
                return '''
                    <h2>Erro ao gravar a banda <b>%s</b>.</h2>
                    <a href = "/">voltar</a>
                ''' % (txtNome)
        else:
            return '''
                <h2>O nome da banda deve ser informada.</h2>
                <a href = "/">voltar</a>
            '''

    @cherrypy.expose()
    def excluirBanda(self,idBanda):
        objBanda = Banda()
        objBanda.set_id(int(idBanda))
        if objBanda.excluir() > 0:
            raise cherrypy.HTTPRedirect('/cadastro')
        else:
            return '''
            <h2> Não foi possível excluir a banda!!</h2>
            <a href = "/">voltar</a>
            '''

    @cherrypy.expose()
    def alterarBanda(self,idBanda):
        objBanda = Banda()
        # estamos buscando o objeto com os dados que foram passados por parâmetro neste método
        dadosBandaSelect = objBanda.obterBanda(idBanda)
        # chamando o método para montar o formulário com os valores do banco de dados nos campos do formulário
        return self.montaFormulario(dadosBandaSelect[0]["Id"],dadosBandaSelect[0]["Nome"],dadosBandaSelect[0]["Email"],dadosBandaSelect[0]["Genero"],dadosBandaSelect[0]["Descr"],dadosBandaSelect[0]["Senha"])