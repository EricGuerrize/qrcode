from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS

app = Flask(__name__)
from flask import send_from_directory
import os

@app.route('/<path:nome_arquivo>')
def arquivos_estaticos(nome_arquivo):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), nome_arquivo)
CORS(app)  # Permite chamadas de outros domínios, útil se abrir HTML direto

# Substitua com suas credenciais do Twilio
TWILIO_SID = 'SAC7aeea0374f704aeadcbda96e21fe3a0f'
TWILIO_AUTH_TOKEN = 'Sf2a84e6a5501aab31f4be875cd383f8d'
TWILIO_PHONE = '+12403262948'  # Número fornecido pelo Twilio
MEU_NUMERO = '+5565992556938'    # Seu número real para receber o SMS

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.route('/enviar-sms', methods=['POST'])
def enviar_sms():
    dados = request.get_json()
    horario = dados.get('horario', 'horário indefinido')
    mensagem = f"🌹 Convite confirmado! Te espero no Olga às {horario}. ❤️"

    try:
        client.messages.create(
            body=mensagem,
            from_=TWILIO_PHONE,
            to=MEU_NUMERO
        )
        print(f"SMS enviado para {MEU_NUMERO} com a mensagem: {mensagem}")
        return jsonify({'status': 'SMS enviado!'}), 200
    except Exception as e:
        print(f"Erro ao enviar SMS: {e}")
        return jsonify({'erro': str(e)}), 500

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)