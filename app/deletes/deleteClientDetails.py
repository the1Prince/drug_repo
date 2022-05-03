from flask import jsonify, request
from app.models import ClientDetails, Token
from app import db

def deleteClientDetails(id):
    '''delete client details record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id in data and id is not None:
            if token and is_expired == 'active':
                clientdetails=ClientDetails.query.filter_by(id=id).first()
                
                if clientdetails is not None:
                    
                    clientdetails.delete()
                    db.session.commit()
          
                else:
                    return jsonify('Client details record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No client details id provided'),500
    return jsonify('Provide a client details id to delete'),500
                