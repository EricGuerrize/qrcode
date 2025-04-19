<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Convite Especial 💌</title>
  <style>
    body {
      background: linear-gradient(to bottom right, #f9f3ff, #d0f0ff);
      font-family: 'Segoe UI', sans-serif;
      text-align: center;
      padding: 50px;
    }
    h1 {
      font-size: 2rem;
      color: #d63384;
    }
    button {
      padding: 10px 20px;
      margin: 20px;
      font-size: 1.2rem;
      cursor: pointer;
      border: none;
      border-radius: 8px;
    }
    #sim-btn {
      background-color: #28a745;
      color: white;
    }
    #nao-btn {
      background-color: #dc3545;
      color: white;
      position: absolute;
    }
    #play-music {
      background-color: #ff69b4;
      color: white;
      position: relative;
    }
  </style>
</head>
<body>

  <h1>Você aceita ir a um date comigo? 💖</h1>

  <button id="sim-btn" onclick="window.location.href='confirmado.html'">Sim 😍</button>
  <button id="nao-btn" onmouseover="fugir()" onclick="fugir()">Não 🙈</button>

  <br><br>
  <button id="play-music" onclick="tocarMusica()">Iniciar Música 🎵</button>
  <audio id="musica-romantica" loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    Seu navegador não suporta áudio.
  </audio>

  <script>
    function fugir() {
      const btn = document.getElementById('nao-btn');
      const x = Math.random() * (window.innerWidth - 100);
      const y = Math.random() * (window.innerHeight - 50);
      btn.style.left = `${x}px`;
      btn.style.top = `${y}px`;
    }

    function tocarMusica() {
      document.getElementById('musica-romantica').play();
    }
  </script>

</body>
</html>