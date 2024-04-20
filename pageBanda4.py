import cherrypy

class PaginaBanda4():
    texto = open("html/banda4.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html