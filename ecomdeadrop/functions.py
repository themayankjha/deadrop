import sqlite3

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