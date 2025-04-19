from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

@app.route("/enviar-sms", methods=["POST"])
def enviar_sms():
    dados = request.get_json()
    horario = dados.get('horario', 'horário indefinido')
    mensagem = f"🌹 Convite confirmado! Te espero no Olga às {horario}. 💌"

    remetente = 'guerrizeeric@gmail.com'
    senha = 'gkdbnnebsqqutoqs'
    destinatario = 'guerrizeeric@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = 'Confirmação de Date ❤️'
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remetente, senha)
            servidor.sendmail(remetente, destinatario, msg.as_string())
        print(f"E-mail enviado para {destinatario}")
        return jsonify({'status': 'E-mail enviado!'}), 200
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return jsonify({'erro': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    #teste