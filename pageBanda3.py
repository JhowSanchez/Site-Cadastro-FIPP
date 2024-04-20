import cherrypy

class PaginaBanda3():
    texto = open("html/banda3.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html