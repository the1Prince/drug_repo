from flask import jsonify, request
from app.models import Manufacturer, Token
from app import db

def deleteManufacturer(id):
    '''delete manufacturer record'''
    
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if id is not None:
        if token and is_expired == 'active':
            manufacturer=Manufacturer.query.filter_by(id=id).first()
                
            if manufacturer is not None:
                    
                db.session.delete(manufacturer)
                db.session.commit()

                return jsonify('manufacturer deleted successfully'),201
          
            else:
                return jsonify('Manufacturer record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('No manufacturer id provided'),500
 
                