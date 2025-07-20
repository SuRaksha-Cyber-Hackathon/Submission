from flask import Flask, request, jsonify
import smtplib
import ssl
import random
import time
from email.message import EmailMessage

app = Flask(__name__)

# Email config
SENDER_EMAIL = 'example@gmail.com' #enter your mail
SENDER_PASSWORD = 'your app password' #enter your password

otp_store = {}


OTP_EXPIRY_SECONDS = 60  # 1 minutes


def send_email(receiver_email, otp):
    message = EmailMessage()
    message['Subject'] = 'Your OTP Code'
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_email
    message.set_content(f'Your OTP is: {otp}')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(message)

@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({'error': 'Missing email in request'}), 400

    email = data['email']
    otp = random.randint(100000,999999)
    print(otp)
    timestamp = time.time()

    try:
        send_email(email, otp)
        otp_store[email] = {'otp': otp, 'timestamp': timestamp}
        return jsonify({'message': 'OTP sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    if not data or 'email' not in data or 'otp' not in data:
        return jsonify({'error': 'Missing email or otp'}), 400

    email = data['email']
    user_otp = data['otp']

    record = otp_store.get(email)
    if not record:
        return jsonify({'error': 'OTP not found. Please request a new one.'}), 404

    stored_otp = record['otp']
    timestamp = record['timestamp']

    if time.time() - timestamp > OTP_EXPIRY_SECONDS:
        del otp_store[email]
        return jsonify({'error': 'OTP expired. Please request a new one.'}), 410

    if user_otp == stored_otp:
        del otp_store[email]  # Remove after successful verification
        return jsonify({'message': 'OTP verified successfully'}), 200
    else:
        return jsonify({'error': 'Invalid OTP'}), 401

if __name__ == '__main__':
    app.run(debug=True)
