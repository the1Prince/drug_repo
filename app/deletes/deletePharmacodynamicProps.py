from flask import jsonify, request
from app.models import Pharmacodynamic_properties, Token
from app import db

def deletePharmacodynamicProps(id):
    '''delete pharmacodynamic properties record'''
    
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if id is not None:
        if token and is_expired == 'active':
            pharmacodynamicProps=Pharmacodynamic_properties.query.filter_by(id=id).first()
                
            if pharmacodynamicProps is not None:
                    
                db.session.delete(pharmacodynamicProps)
                db.session.commit()
                return jsonify('pharmacodynamic properties record deleted successfully')
          
            else:
                return jsonify('Pharmacodnamic properties record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('No pharmacodynamic properties id provided'),500
    
                