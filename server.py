from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS

app = Flask(__name__)
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
        return jsonify({'status': 'SMS enviado!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)