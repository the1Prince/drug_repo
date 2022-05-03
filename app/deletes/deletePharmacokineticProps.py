from flask import jsonify, request
from app.models import Pharmacokinetic_properties, Token
from app import db

def deletePharmacokineticProps(id):
    '''delete pharmacokinetic properties record'''
    
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

   
    if id is not None:
        if token and is_expired == 'active':
            pharmacokineticProps=Pharmacokinetic_properties.query.filter_by(id=id).first()
                
            if pharmacokineticProps is not None:
                    
                db.session.delete(pharmacokineticProps)
                db.session.commit()

                return jsonify('drug pharmacokinetic properties deleted successfully'),201
          
            else:
                return jsonify('Pharmacokinetic properties record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('No pharmacokinetic properties id provided'),500
    
                