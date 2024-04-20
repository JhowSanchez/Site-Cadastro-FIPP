import cherrypy

class PaginaYago():
    texto = open("html/yago.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html