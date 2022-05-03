from flask import jsonify, request
from app.models import Pharmaceutical_info, Token
from app import db

def deletePharmaceuticalInfo(id):
    '''delete pharmaceutcal info record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id in data and id is not None:
            if token and is_expired == 'active':
                pharmaceuticalInfo=Pharmaceutical_info.query.filter_by(id=id).first()
                
                if pharmaceuticalInfo is not None:
                    
                    pharmaceuticalInfo.delete()
                    db.session.commit()
          
                else:
                    return jsonify('Pharmaceutical info record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No pharmaceutical info id provided'),500
    return jsonify('Provide a pharmaceutical info id to delete'),500
                