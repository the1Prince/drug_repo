from flask import jsonify, request
from app.models import Users, Token
from app import db

def deleteUsers(id):
    '''delete users record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id in data and id is not None:
            if token and is_expired == 'active':
                users=Users.query.filter_by(id=id).first()
                
                if users is not None:
                    
                    users.delete()
                    db.session.commit()
          
                else:
                    return jsonify('Users record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No users id provided'),500
    return jsonify('Provide a users id to delete'),500
                