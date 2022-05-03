from flask import jsonify, request
from app.models import Drug, Token
from app import db

def deleteDrug(id):
    '''delete drug record'''
    
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if token and is_expired == 'active':
        drug=Drug.query.filter_by(id=id).first()
        
                
        if drug is not None:
                    
            db.session.delete(drug)
            
            db.session.commit()

            return jsonify('drug item deleted successfully'),201
          
        else:
            return jsonify('drug record specified does not exist'),500
    else:
        return jsonify('no token provided or token has expired'),500
        