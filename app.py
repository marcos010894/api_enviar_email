from flask import Flask,request
import os
app = Flask(__name__)
from flask_mail import Mail, Message
app.config['MAIL_SERVER'] = os.environ.get("EMAIL_SERVER")
app.config['MAIL_PORT'] = int(os.environ.get("EMAIL_PORT" , '465'))
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL_FROM")
app.config['MAIL_PASSWORD'] = os.environ.get("EMAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = False if os.environ.get("MAIL_USE_TLS" , 'false') == "false" else True
app.config['MAIL_USE_SSL'] = True if os.environ.get('MAIL_USE_SSL', 'true') == "true" else False
mail = Mail(app)
from decorator.decorator import decorator_key
@app.route("/")
def home():
    return "ok",200

@app.route('/email', methods=['POST','GET'])
@decorator_key
def render_script():
    data = request.json
    subject = data['subject']
    sender = os.environ.get("EMAIL_FROM")
    destination = data['destination']
    body = data['body']
   
    try:
        msg = Message(subject,sender = sender,recipients=destination)
        msg.html = body
        mail.send(msg)
        return "foi",200
    except Exception as e:   

        return {"error":str(e)},200
def main():
    
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port = port)
    #app.run(debug=True)

if __name__ == "__main__":
    main()
