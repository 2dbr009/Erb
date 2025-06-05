from flask import Flask, request, jsonify, send_from_directory
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, static_folder='')

import os

SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SMTP_USERNAME = os.getenv('SMTP_USERNAME', 'your_email@gmail.com')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'your_app_password')
EMAIL_FROM = SMTP_USERNAME
EMAIL_TO = os.getenv('EMAIL_TO', 'contato@erbeletrica.com.br')
EMAIL_SUBJECT = 'Nova mensagem de contato - ERB Elétrica'

def create_email_message(name, email, user_message):
    """
    Creates the message content to be sent to contato@erbeletrica.com
    """
    message = (
        f"Olá,\n\n"
        f"Recebemos uma nova mensagem de contato.\n\n"
        f"Nome: {name}\n"
        f"E-mail: {email}\n"
        f"Mensagem: {user_message}\n\n"
        f"Em breve, entraremos em contato com mais detalhes.\n\n"
        f"Atenciosamente,\n"
        f"Equipe ER Elétrica"
    )
    return message

@app.route('/')
def serve_index():
    return send_from_directory('', 'index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        user_message = request.form.get('message')

        if not name or not email or not user_message:
            return jsonify({'error': 'Por favor, preencha todos os campos.'}), 400

        message_body = create_email_message(name, email, user_message)

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = EMAIL_SUBJECT
        msg['Reply-To'] = email  # Set Reply-To to user's email
        msg.attach(MIMEText(message_body, 'plain'))

        # Send email via SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

        return jsonify({'success': 'Mensagem enviada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
