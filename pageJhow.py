import cherrypy

class PaginaJhow():
    texto = open("html/Jhow.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html