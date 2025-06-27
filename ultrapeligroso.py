# ultrapeligroso.py

from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Chatbot básico (no uses en producción)'

@app.route('/chat')
def chat():
    user_input = request.args.get('msg', '')

    try:
        result = eval(user_input)  # VULNERABLE A CODE INJECTION
    except Exception as e:
        result = str(e)

    if user_input.startswith("cmd:"):
        cmd = user_input[4:]
        os.system(cmd)  # VULNERABLE A OS COMMAND INJECTION
        result = f"Comando ejecutado: {cmd}"

    log = f"Usuario escribió: {user_input}\nResultado: {result}"
    with open("chat.log", "a") as f:
        f.write(log + "\n")

    return result

if __name__ == "__main__":
    app.run(debug=True)
