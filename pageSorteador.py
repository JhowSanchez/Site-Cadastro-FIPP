import cherrypy

class PaginaSorteador():
    texto = open("html/sorteador.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html