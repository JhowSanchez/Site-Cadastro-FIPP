import cherrypy

class PaginaIndex():
    texto = open("html/index.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html