from flask import jsonify, request
from app.models import Description, Token
from app import db

def deleteDescription(id):
    '''delete description record'''
    
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if id is not None:
        if token and is_expired == 'active':
            description=Description.query.filter_by(id=id).first()
                
            if description is not None:
                    
                db.session.delete(description)
                db.session.commit()

                return jsonify('drug description successfully deleted'),201
          
            else:
                return jsonify('Drug description record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('No description id provided'),500
    
                