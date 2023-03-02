from models import *
from flask import Flask, request, render_template


@app.route('/')
def app_landing_page():
    return render_template('index.html')

@app.route('/register',methods = ['GET','POST'])
def register_here():
    if request.method == 'POST':
        formdata = request.form
        userrecord = User(firstname=formdata.get('fname'),
                          email=formdata.get('email'),
                          lastname = formdata.get('lname'),
                          gender=formdata.get('gender'))
        db.session.add(userrecord)
        db.session.commit()

        credentials = Credentials(username=formdata.get('username'),
                    password=formdata.get('password'),userref=userrecord.user_id)
        db.session.add(credentials)
        db.session.commit()

        address = Address(city = formdata.get('city'),state = formdata.get('state'))#user_adr = userrecord)
        db.session.add(address)
        db.session.commit()

        address.users.append(userrecord)
        db.session.commit()

        phone = Phone(phone_num = formdata.get('contact'),
                      vendor = formdata.get('cvendor'),userref=userrecord)
        db.session.add(phone)
        db.session.commit()
    return render_template('register.html')


@app.route('/authenticate',methods = ['POST'])
def verify_user():
    if request.method == 'POST':
        formdata = request.form
        record = Credentials.query.filter_by(username = formdata.get('username')).first() # select * from credenatils where username = formusername
        if record and record.password ==formdata.get('password'):
            return render_template('home.html',user = record.username)
        else:
            return render_template('index.html',error = "Invalid Credentails..")



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
    # app.run(debug=True)