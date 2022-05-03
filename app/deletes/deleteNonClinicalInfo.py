from flask import jsonify, request
from app.models import Non_clinical_info, Token
from app import db

def deleteNonClinicalInfo(id):
    '''delete non clinical info record'''
 
    token = request.headers['TOKEN']
    
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    
    if id is not None:
        if token and is_expired == 'active':
            nonClinicalInfo=Non_clinical_info.query.filter_by(id=id).first()
                
            if nonClinicalInfo is not None:
                    
                db.session.delete(nonClinicalInfo)
                db.session.commit()

                return jsonify('non clinicla info record deleted successfully'),201
          
            else:
                return jsonify('Non clinical info record specified does not exist'),500
        else:
            return jsonify('no token provided or token has expired'),500
    else:
        return jsonify('non clinical info id is not provided'),500
  
                