from flask import jsonify, request
from app.models import Overdose, Token
from app import db

def deleteOverdose(id):
    '''delete overdose record'''
    
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if id is not None:
        if token and is_expired == 'active':
            overdose=Overdose.query.filter_by(id=id).first()
                
            if overdose is not None:
                    
                db.session.delete(overdose)
                db.session.commit()

                return jsonify('drug overdose record successfully deleted'),201

          
            else:
                return jsonify('Overdose record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('No overdose id provided'),500

                