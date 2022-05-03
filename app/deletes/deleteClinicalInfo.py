from flask import jsonify, request
from app.models import Clinical_info, Token
from app import db

def deleteClinicalInfo(id):
    '''delete clinical info record'''
    
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if id is not None:
        if token and is_expired == 'active':
            clinicalInfo=Clinical_info.query.filter_by(id=id).first()
                
            if clinicalInfo is not None:
                    
                db.session.delete(clinicalInfo)
                db.session.commit()
          
            else:
                return jsonify('Clinical info record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('No clinical info id provided'),500
    
                