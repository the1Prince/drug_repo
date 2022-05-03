from flask import jsonify, request
from app.models import Clinical_info, Token
from app import db

def updateClinicalInfo():
    '''update clinical info record'''
    data = request.get_json()
    token = request.headers['TOKEN']
    id=int(data['id'])
    

    t=Token.query.filter_by(token=token).first()

    is_expired=t.status
    
    

    if data:
        if id is not None:
            if token and is_expired == 'active':
                old_data=Clinical_info.query.filter_by(id=id).first()
                
                if old_data is not None:
                    
                        
                        old_data.indication=data['absorption'],
                        old_data.dosage=data['dosage'],
                        old_data.administration=data['administration'],
                        old_data.contrindication=data['contrindication'],
                        old_data.interaction=data['interaction'],
                        old_data.fertility=data['fertility'],
                        old_data.warning_precaution=data['warning_precaution'],
                        old_data.adverse_reaction=data['adverse_reaction'],
                        
                            
                        db.session.add(old_data)
                        db.session.commit()

                        return jsonify('clinical info record deleted successfully'),200

                        return{
                            'id': old_data.id, 'cli_id': old_data.cli_id, 'indication': old_data.indication, 'dosage': old_data.dosage, 'administration': old_data.administration, 'contrindication': old_data.contrindication, 'interaction': old_data.interaction, 'fertility': old_data.fertility, 'warning_precaution': old_data.warning_precaution, 'adverse_reaction': old_data.adverse_reaction, 'drug_id': old_data.drug_id
                        }, 201
          
                else:
                    return jsonify('Drug clinical info record specified does not exist'),500
            else:
                return jsonify('no token provided or token has expired'),500
        else:
            return jsonify('No clinical info id provided'),500
    return jsonify('Provide new clinical info records for update'),500
                