import cherrypy

class PaginaBanda2():
    # texto = open("html/banda2.html").read() - as professoras viram e autorizaram
    texto = '''<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="iso-8859-1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="shortcut icon" type="image/x-icon" href="/img/fipp-logo.png" />
  <link rel="stylesheet" href="/css/banda2.css">
  <title>Document</title>
</head>

<body>
  <div class="navbar">
    <div class="navbar-brand">
      Fipp Music Festival
    </div>
    <div class="navbar-buttons">
      <a onclick="goBack()" id="comprar-ingressos">Home</a>
    </div>
  </div>
  <video poster="/img/artworks-njrn1mle9DF1qBMA-7g9YOQ-t500x500.jpg" id="bgvid" playsinline autoplay loop preload="auto">
    <source src="/videos/Kayblack - Bonjour (VIDEO CLIPE OFICIAL)(720P_HD).mp4" type="video/webm">
    <source src="/videos/Kayblack - Bonjour (VIDEO CLIPE OFICIAL)(720P_HD).mp4" type="video/mp4">

  </video>
  <div id="polina">
    <h1>KayBlack</h1>
    <p>Genero : Rap
    <p>Data 28/03/2023 - Palacio dos Esportes</a>
    <p> O rapper Kaique Menezes, o Kayblack, 21 anos, é um dos representantes da intersecção entre o rap e o funk.
      Desentrelaçados artisticamente, os dois gêneros que possuem a mesma raiz, os extremos periféricos do Brasil, agora
      correm mais do que juntos. Em sua arte, Kayblack é capaz de unir os dois mundos, dando fôlego ao chamado
      “trapfunk”.
    </p>
    <p>OKaique começou sua trajetória no funk, aos 12 anos. Inspirado em artistas como Felipe Boladão e Neguinho do
      Kaxeta, já escrevia seus versos e projetava seu sonho de viver da música. Somente aos 20 anos deu vida à música,
      já nas batidas do trap. Em 2020, lançou seu primeiro single, Bandido Mau, que soma 5 milhões de reproduções no
      YouTube.</p>
    <button>Pause</button>
  </div>
</body>
<script>
  function goBack() {
    window.history.back();
  }
  var vid = document.getElementById("bgvid");
  var pauseButton = document.querySelector("#polina button");

  if (window.matchMedia('(prefers-reduced-motion)').matches) {
    vid.removeAttribute("autoplay");
    vid.pause();
    pauseButton.innerHTML = "Paused";
  }

  function vidFade() {
    vid.classList.add("stopfade");
  }

  vid.addEventListener('ended', function () {
    // only functional if "loop" is removed
    vid.pause();
    // to capture IE10
    vidFade();
  });


  pauseButton.addEventListener("click", function () {
    vid.classList.toggle("stopfade");
    if (vid.paused) {
      vid.play();
      pauseButton.innerHTML = "Pause";
    } else {
      vid.pause();
      pauseButton.innerHTML = "Paused";
    }
  })


</script>

</html>'''

    @cherrypy.expose()
    def index(self):
        html = self.texto

        return html