import cherrypy

class PaginaBanda1():
    texto = open("html/banda1.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html