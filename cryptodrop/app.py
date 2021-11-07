from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os,string,random
from twilio.rest import Client

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='static/uploads/'
app.config['MAX_CONTENT_PATH']=16 * 1024 * 1024

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def twilioSend(mes, number):
  message = client.messages \
                  .create(
                      body=mes,
                      from_='+12815476047',
                      to=number
                  )
  print(message.sid)

def randgen():
  uplink=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
  return uplink

uplink=randgen()

@app.route('/', methods = ['GET','POST'])
def index():
  if request.method=='GET':
    return render_template('index.html')

  btc = request.form['btc']
  doge = request.form['doge']

  if str(btc) == "1337" and str(doge) == "69420":
    return render_template('upload.html',uplink=uplink)
  else:
    return redirect('/')


@app.route('/{0}'.format(uplink), methods = ['GET','POST'])
def upload():
  f = request.files['file']
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
  return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
