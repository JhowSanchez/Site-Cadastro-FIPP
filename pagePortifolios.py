import cherrypy

class PaginaPortifolios():
    texto = open("html/portifolios.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html