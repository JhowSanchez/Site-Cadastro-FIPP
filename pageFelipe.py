import cherrypy

class PaginaFelipe():
    texto = open("html/felipe.html").read()

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html