from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)

@app.route("/")
def convite():
    return render_template('convite.html')

@app.route("/confirmado")
def confirmado():
    return render_template('confirmado.html')

@app.route("/enviar-sms", methods=["POST"])
def enviar_sms():
    dados = request.get_json()
    horario = dados.get('horario', 'horário indefinido')
    mensagem = f"🌹 Convite confirmado! Te espero no Olga às {horario}. 💌"

    remetente = os.getenv('EMAIL_USER')
    senha = os.getenv('EMAIL_PASS')
    destinatario = os.getenv('EMAIL_DEST')

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = 'Confirmação de Date ❤️'
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remetente, senha)
            servidor.sendmail(remetente, destinatario, msg.as_string())
        return jsonify({'status': 'E-mail enviado!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)