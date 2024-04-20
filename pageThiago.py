import cherrypy

class PaginaThiago():
    texto = open("html/thiago.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html