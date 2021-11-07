import sqlite3,os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def searchfunc(query):
    con=sqlite3.connect('static/musicdb.db')
    cur=con.cursor()
    output=cur.execute("select * from music where name like ?",('%{}%'.format(query),))
    out=output.fetchall()
    id,name,desc,price=[],[],[],[]

    for item in out:
        id.append(item[0])
        name.append(item[1])
        desc.append(item[2])
        price.append(item[3])

    tracks={'length':len(out),'id':id,'name':name,'desc':desc,'price':price}

    return tracks

def twilioSend(mes, number):
  message = client.messages \
                  .create(
                      body=mes,
                      from_='+12815476047',
                      to=number
                  )
  print(message.sid)

def randomfunc():
    con=sqlite3.connect('static/musicdb.db')
    cur=con.cursor()
    output=cur.execute("SELECT * FROM music ORDER BY RANDOM() LIMIT 2;")
    out=output.fetchall()
    id,name,desc,price=[],[],[],[]

    for item in out:
        id.append(item[0])
        name.append(item[1])
        desc.append(item[2])
        price.append(item[3])

    tracks={'length':len(out),'id':id,'name':name,'desc':desc,'price':price}

    return tracks