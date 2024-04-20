import cherrypy
import os

from pageBanda1 import PaginaBanda1
from pageBanda2 import PaginaBanda2
from pageBanda3 import PaginaBanda3
from pageBanda4 import PaginaBanda4
from pageFelipe import PaginaFelipe
from pageIndex import PaginaIndex
from pageJhow import PaginaJhow
from pagePortifolios import PaginaPortifolios
from pageSorteador import PaginaSorteador
from pageThiago import PaginaThiago
from pageYago import PaginaYago
from pageCadastro import PaginaCadastro

local_dir = os.path.dirname(__file__)

class Home():
    texto = open("html/home.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html

server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 82
}
cherrypy.config.update(server_config)

local_config = {
    "/":{"tools.staticdir.on":True,
         "tools.staticdir.dir":local_dir},
}

root = Home()
root.banda1 = PaginaBanda1()
root.banda2 = PaginaBanda2()
root.banda3 = PaginaBanda3()
root.banda4 = PaginaBanda4()
root.felipe = PaginaFelipe()
root.jhow = PaginaJhow()
root.thiago = PaginaThiago()
root.yago = PaginaYago()
root.portifolios = PaginaPortifolios()
root.indexhome = PaginaIndex()
root.sorteador = PaginaSorteador()
root.cadastro = PaginaCadastro()
cherrypy.quickstart(root,config=local_config)