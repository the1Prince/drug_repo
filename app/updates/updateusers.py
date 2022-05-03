from flask import jsonify, request, session
from app.models import Users, Token
from app import db

from werkzeug.security import generate_password_hash



def  updateusername():
    
    if session is not None:
        user=Users.query.filter_by(id=session['id']).first()
        data=request.get_json()
        username=data['username']
        if username and username is not None:
            
            #user=Users(id=int(session['id']),username=username)
            user.username=data['username']
            try:


                db.session.add(user)
                db.session.commit()

                return{
                    'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, 'email':user.email, 'telephone':user.telephone
                },201
            except:
                return jsonify("Invalid usename, use a different username"),500

            
        else:
            return jsonify("No username provided"),500
    else:
            return jsonify("You're currently logged out"),500




def  updatefirstname():

    user=Users.query.filter_by(id=session['id']).first()
    data=request.get_json()
    firstname=data['firstname']
    if firstname and firstname is not None:
            
            #user=Users(id=int(session['id']),username=username)
        user.firstname=data['firstname']

        db.session.add(user)
        db.session.commit()

        return{
                'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, 'email':user.email, 'telephone':user.telephone
            },201
    else:
        return jsonify("No username provided"),500
   

def  updatelastname():

    user=Users.query.filter_by(id=session['id']).first()
    data=request.get_json()
    lastname=data['lastname']
    if lastname and lastname is not None:
            
            #user=Users(id=int(session['id']),username=username)
        user.lastname=data['lastname']

        db.session.add(user)
        db.session.commit()

        return{
                'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, 'email':user.email, 'telephone':user.telephone
            },201
    else:
        return jsonify("No username provided"),500


def  updateemail():

    user=Users.query.filter_by(id=session['id']).first()
    data=request.get_json()
    email=data['email']
    if email and email is not None:
            
            #user=Users(id=int(session['id']),username=username)
        user.email=data['email']
        #checkemail=Users.query.filter_by(email=email).first()
        try:


            db.session.add(user)
            db.session.commit()

            return{
                    'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, 'email':user.email, 'telephone':user.telephone
                },201
        except:
            return jsonify("Invalid email, use a different email"),500
    else:
        return jsonify("No username provided"),500


def  updatepassword():

    user=Users.query.filter_by(id=session['id']).first()
    data=request.get_json()
    password=data['password']
    
    if password and password is not None:
        current_pasword=generate_password_hash(password)
            
            #user=Users(id=int(session['id']),username=username)
        user.password=current_pasword
        #checkemail=Users.query.filter_by(email=email).first()
        try:


            db.session.add(user)
            db.session.commit()

            return jsonify({
                    'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, 'email':user.email, 'telephone':user.telephone
                }),201
        except:
            return jsonify("error updating password"),500
    else:
        return jsonify("No username provided"),500


def  updatetelephone():

    user=Users.query.filter_by(id=session['id']).first()
    data=request.get_json()
    telephone=data['telephone']
    if telephone and telephone is not None:
            
            #user=Users(id=int(session['id']),username=username)
        user.telephone=data['telephone']
        #checkemail=Users.query.filter_by(email=email).first()
        try:


            db.session.add(user)
            db.session.commit()

            return{
                    'id':user.id, 'firstname':user.firstname, 'lastname':user.lastname, 'email':user.email, 'telephone':user.telephone
                },201
        except:
            return jsonify("Invalid telephone, use a different telephone"),500
    else:
        return jsonify("No telephone number provided or number already exists"),500


def updateUsers():
    '''update users record'''
    data = request.get_json()
    
    id=session['id']
 
    if data:
        if id is not None:
            
            old_data=Users.query.filter_by(id=id).first()
            if old_data is not None:
                old_data.firstname=data['firstname'],
                old_data.lastname=data['lastname'],
                old_data.username=data['username'],
                old_data.email=data['email'],
                old_data.telephone=data['telephone']
                            
                db.session.add(old_data)
                db.session.commit()

                return jsonify({
                    'id':old_data.id, 'firstname':old_data.firstname, 'lastname':old_data.lastname, 'email':old_data.email, 'telephone':old_data.telephone
                }),201
          
            else:
                return jsonify('Drug manufacturer record specified does not exist'),500
           
        else:
            return jsonify('No manufacturer id provided'),500
    return jsonify('Provide new manufacturer records for update'),500
                