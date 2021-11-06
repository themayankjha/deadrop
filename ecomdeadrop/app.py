from flask import Flask, render_template, redirect, make_response, request,json
from werkzeug.utils import secure_filename
import os
from functions import searchfunc,randomfunc
app = Flask(__name__)
app.secret_key = "iz&Q9dS8X9a!kGtqgp8PwNBj&VAx4GYR8"
app.config['UPLOAD_FOLDER']='static/uploads/'
app.config['MAX_CONTENT_PATH']=16 * 1024 * 1024

@app.route('/', methods=['GET','POST'])
def index():
    try:    
        ids = request.cookies.get('ids')    
        num=len(json.loads(ids))
    except:
        num=0
    
    if 'keyword' in request.args:
        keyword = request.args.get('keyword')
        searchtracks=searchfunc(keyword)

    else:
        searchtracks=randomfunc()
        
    return render_template('index.html',title="tile",num=num,track=searchtracks)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    heckor=False
    try:
        ids = request.cookies.get('ids')   
        ids=json.loads(ids) 
        num=len(ids)
        if '1' in ids and '2' in ids and '3' in ids and num==3:
            heckor=True
    except:
        num=0

    
    if request.method == 'POST' and heckor==True:   
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))) 
    return render_template('contact.html',num=num,heckor=heckor)

@app.route('/about',methods=['GET'])
def about():
    try:
        ids = request.cookies.get('ids')    
        num=len(json.loads(ids))
    except:
        num=0
    return render_template('about.html',num=num)

@app.route('/addtocart', methods=['GET'])
def addtocart():
    if 'id' in request.args:
        id = request.args.get('id')
        try:
            ids = request.cookies.get('ids')    
            ids=json.loads(ids)
            ids.append(id)      
        except:
            ids=[id]
    resp = make_response(redirect("/"))
    resp.set_cookie('ids', json.dumps(ids))
    return resp


@app.route('/cart',methods=['GET'])
def cart():
    try:
        ids = request.cookies.get('ids')    
        num=len(json.loads(ids))
    except:
        num=0
    return render_template('cart.html',num=num)


if __name__ == '__main__':
    app.run(debug=True)

