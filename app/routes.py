import json
from time import timezone
import uuid
from flask import Request, Response, jsonify, request, session
from app import app,postreqs,getreqs
from app.models import Drug, Description, Manufacturer, Non_clinical_info, Overdose, Pharmaceutical_info, Pharmacodynamic_properties, Pharmacokinetic_properties, Special_population, Clinical_trial_data, Clinical_info,Users,Token,ClientDetails
from app import db
from app.errors import bad_request
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest
from flask_httpauth import HTTPBasicAuth
from datetime import datetime, timedelta

from app.updates import updateusers,update_description,update_manufacturer,updateclient_details,updateclinical_info,updateClinicalTrialData,updatedrugs,updateNonClinicalInfo,updateOverdose,updatePharmaceuticalInfo,updatepharmacodynamic_props,updatePharmacokineticProps,updateSpecialPopulation
from app.deletes import deleteClientDetails,deleteClinicalInfo,deleteClinicalTrialData,deleteDescription,deleteDrugs,deleteManufacturer,deleteNonClinicalInfo,deleteOverdose,deletePharmaceuticalInfo,deletePharmacodynamicProps,deletePharmacokineticProps,deleteSpecialPopulation,deleteUsers



@app.route('/')
@app.route('/index')
def index():
    hi=postreqs.greet()
    return(hi)

##################################################################################################################################
######################################### Start of POST calls############################################
############################################################################
@app.route('/v1/users/', methods=['POST'])
def create_user():
    insert = postreqs.newuser()
    return(insert)




@app.route('/v1/login', methods=['POST'])
def login():
   getin=postreqs.login()
   return(getin)
    

    
@app.route('/v1/logout', methods=['POST'])
def logout():
    logout=postreqs.logout()
    return(logout)     




@app.route('/v1/tokens/', methods=['POST'])
def post_token():
   token = postreqs.token()
   return(token)

@app.route('/v1/clientdetails/', methods=['POST'])
def post_clientdetails():
    clientdetails=postreqs.clientdetails()
    return(clientdetails)




@app.route('/v1/drugs/', methods=['POST'])
def post_drug():
  drug=postreqs.drug()
  return(drug)

    


@app.route('/v1/descriptions/', methods=['POST'])
def post_description():
    desc=postreqs.description()
    return(desc)


@app.route('/v1/manufacturer/', methods=['POST'])
def post_manufacturer():
    manufacturer=postreqs.manufacturer()
    return(manufacturer)


@app.route('/v1/non_clinical_info/', methods=['POST'])
def post_non_clinical_info():
    non_clinical=postreqs.non_clinical_info()
    return(non_clinical)


@app.route('/v1/overdose/', methods=['POST'])
def post_overdose():
    overdose=postreqs.overdose()
    return(overdose)


@app.route('/v1/pharmaceutical_info/', methods=['POST'])
def post_pharmaceutical_info():
    pharma_info=postreqs.pharmaceutical_info()
    return(pharma_info)
   


@app.route('/v1/pharmacodynamic_props/', methods=['POST'])
def post_pharmacodynamic_properties():
    pharmaco=postreqs.pharmacodynamic_props()
    return(pharmaco)

@app.route('/v1/pharmacokinetic_properties/', methods=['POST'])
def post_pharmacokinetic_properties():
    phamacokinetic=postreqs.pharmacokinetic_props()
    return(phamacokinetic)


@app.route('/v1/special_population/', methods=['POST'])
def post_special_population():
    special_pop=postreqs.special_population()
    return(special_pop)


@app.route('/v1/clinical_info/', methods=['POST'])
def post_clinical_info():
    clinical_info=postreqs.clinical_info()
    return(clinical_info)


@app.route('/v1/clinical_trial_data/', methods=['POST'])
def post_clinical_trial_data():
    clinical_trial=postreqs.clinical_trial_data()
    return(clinical_trial)


##################################################################################################################################
############################### end of POST calls################################################
#################################################################################


##################################################################################################################################
############################### Start of GET calls################################################
#################################################################################
@app.route('/v1/users/', methods=['GET'])
def get_user():
    user=getreqs.users()
    return(user)


@app.route('/v1/tokens/', methods=['GET'])
def get_token():
    token=getreqs.token()
    return(token)


@app.route('/v1/drugs/', methods=['GET'])
def get_drugs():
    drug=getreqs.drugs()
    return(drug)

@app.route('/v1/drugs/<item>', methods=['GET'])
def get_drug(item):
    drug=getreqs.drug_item(item)
    return(drug)

@app.route('/v1/descriptions/', methods=['GET'])
def get_descriptions():
    descriptions = getreqs.descriptions()
    return(descriptions)

@app.route('/v1/descriptions/<drug_id>', methods=['GET'])
def get_description(drug_id):
    description=getreqs.description(drug_id)
    return(description)

@app.route('/v1/manufacturer/', methods=['GET'])
def get_manufacturers():
    manufacturers=getreqs.manufacturers()
    return(manufacturers)

@app.route('/v1/manufacturer/<drug_id>/', methods=['GET'])
def manufacturer(drug_id):
    manufacturer=getreqs.manufacturer(drug_id)
    return(manufacturer)

@app.route('/v1/non_clinical_info/', methods=['GET'])
def non_clinical_infos():
    non_clinical_infos=getreqs.non_clinical_infos()
    return(non_clinical_infos)
    
@app.route('/v1/non_clinical_info/<drug_id>/', methods=['GET'])
def non_clinical_info(drug_id):
    non_clinical_info=getreqs.non_clinical_info(drug_id)
    return(non_clinical_info)

@app.route('/v1/overdose/', methods=['GET'])
def overdose():
    overdose=getreqs.overdose()
    return(overdose)

@app.route('/v1/overdose/<clinical_info_id>/', methods=['GET'])
def overdose_item(clinical_info_id):
    overdose=getreqs.overdose_item(clinical_info_id)
    return(overdose)

@app.route('/v1/clinical_info/', methods=['GET'])
def clinical_infos():
    clinical_infos=getreqs.clinical_infos()
    return(clinical_infos)

@app.route('/v1/clinical_info/<drug_id>/', methods=['GET'])
def clinical_info(drug_id):
    clinical_info=getreqs.clinical_info(drug_id)
    return(clinical_info)


@app.route('/v1/clinical_trial_data/', methods=['GET'])
def clinical_trial_data():
    clinical_trial_data=getreqs.clinical_trial_data()
    return(clinical_trial_data)

@app.route('/v1/clinical_trial_data/<clinical_info_id>/', methods=['GET'])
def clinical_trial_data_item(clinical_info_id):
    clinical_trial_data=getreqs.clinical_trial_data_item(clinical_info_id)
    return(clinical_trial_data)


@app.route('/v1/special_population/', methods=['GET'])
def special_population():
    special_population=getreqs.special_population()
    return(special_population)


@app.route('/v1/special_population/<clinical_info_id>/', methods=['GET'])
def special_population_item(clinical_info_id):
    special_population_item=getreqs.special_population_item(clinical_info_id)
    return(special_population_item)



@app.route('/v1/pharmaceutical_info/', methods=['GET'])
def pharmaceutical_infos():
    pharmaceutical_infos=getreqs.pharmaceutical_info()
    return(pharmaceutical_infos)


@app.route('/v1/pharmaceutical_info/<drug_id>/', methods=['GET'])
def pharmaceutical_info(drug_id):
    pharmaceutical_info=getreqs.pharmaceutical_info(drug_id)
    return(pharmaceutical_info)



@app.route('/v1/pharmacodynamic_props/', methods=['GET'])
def pharmacodynamic_infos():
    pharmacodynamic_props=getreqs.pharmacodynamic_props()
    return(pharmacodynamic_props)


@app.route('/v1/pharmacodynamic_props/<drug_id>/', methods=['GET'])
def pharmacodynamic_info(drug_id):
    pharmacodynamicPropItem=getreqs.pharmacodynamic_prpos_item(drug_id)
    return(pharmacodynamicPropItem)


@app.route('/v1/pharmacokinetic_properties/', methods=['GET'])
def pharmacokinetic_props():
    pharmacokinetic_props=getreqs.pharmacokinetic_props()
    return(pharmacokinetic_props)


@app.route('/v1/pharmacokinetic_properties/<drug_id>/', methods=['GET'])
def pharmacokinetic_prop(drug_id):
    pharmacokinetic_prop=getreqs.pharmacokinetic_props_item(drug_id)
    return(pharmacokinetic_prop)

#####################################################################################################################################
###########################################################################################################################
###################################End of get calls##############################################################
#########################################################################################################


##################################################################################################################################
########################################Start of PUT calls##########################################################
#####################################################################################################

###################Edit User table################
################update users###############
@app.route('/v1/users/',methods=['PUT'])
def updateUsers():
    '''edit users'''
    user=updateusers.updateUsers()
    return(user)


##########update password#########
@app.route('/v1/users/password/', methods=['PUT'])
def updatePassword():
    '''edit password'''
    password=updateusers.updatepassword()
    return(password)


#########update firstname#########
@app.route('/v1/users/firstname/',methods=['PUT'])
def updatefirstname():
    '''edit firstname'''
    firstname=updateusers.updatefirstname()
    return(firstname)


#########update lastname#########
@app.route('/v1/users/lastname/',methods=['PUT'])
def updatelastname():
    '''edit email'''
    lastname=updateusers.updatelastname()
    return(lastname)

#########update username#########
@app.route('/v1/users/username/',methods=['PUT'])
def updateusername():
    '''edit username'''
    user=updateusers.updateusername()
    return(user)


#########update email#########
@app.route('/v1/users/email/',methods=['PUT'])
def updateemail():
    '''edit email'''
    user=updateusers.updateemail()
    return(user)


#########update telephone#########
@app.route('/v1/users/telephone/',methods=['PUT'])
def updateTelephone():
    '''edit telephone'''
    user=updateusers.updatetelephone()
    return(user)

#########update password#########
@app.route('/v1/users/password/',methods=['PUT'])
def updatetelephone():
    '''change password'''
    user=updateusers.updatepassword()
    return(user)


###################End Edit User table################
###############################################################

#########update description#########
@app.route('/v1/descriptions/',methods=['PUT'])
def updatedescription():
    '''edit drug description'''
    description=update_description.updateDescription()
    return(description)


#########update manufacturer#########
@app.route('/v1/manufacturer/',methods=['PUT'])
def updatemanufacturer():
    '''edit drug manufacturer'''
    manufacturer=update_manufacturer.updateManufacturer()
    return(manufacturer)


#########update drugs#########
@app.route('/v1/drugs/',methods=['PUT'])
def updatedrug():
    '''edit drug'''
    drug=updatedrugs.updatedrugs()
    return(drug)


#########update non clinical info#########
@app.route('/v1/non_clinical_info/',methods=['PUT'])
def update_NonClinicalInfo():
    '''edit non clinical info'''
    nonClinicalInfo=updateNonClinicalInfo.updateNonClinicalInfo()
    return(nonClinicalInfo)


#########update overdose#########
@app.route('/v1/overdose/',methods=['PUT'])
def updateoverdose():
    '''edit overdose'''
    overdose=updateOverdose.updateOverdose()
    return(overdose)


#########update overdose#########
@app.route('/v1/pharmaceutical_info/',methods=['PUT'])
def updatepharmaceuticalInfo():
    '''edit pharmaceutical info'''
    pharmaceuticalInfo=updatePharmaceuticalInfo.updatePharmaceuticalInfo()
    return(pharmaceuticalInfo)



#########update pharmacodynamic properties#########
@app.route('/v1/pharmacodynamic_props/',methods=['PUT'])
def updatepharmacodynamicProps():
    '''edit pharmaceuticodynamic properties'''
    pharmacodynamicInfo=updatepharmacodynamic_props.updatePharmacodynamic()
    return(pharmacodynamicInfo)


#########update pharmacokinetic properties#########
@app.route('/v1/pharmacokinetic_properties/',methods=['PUT'])
def updatepharmacokineticProps():
    '''edit pharmaceuticokinetic properties'''
    pharmacokineticProps=updatePharmacokineticProps.updatePharmacokinetic()
    return(pharmacokineticProps)



#########update special population#########
@app.route('/v1/special_population/',methods=['PUT'])
def updatespecialPopulation():
    '''edit special population'''
    specialPopulation=updateSpecialPopulation.updateSpecialPopulation()
    return(specialPopulation)


#########update clinical trial data#########
@app.route('/v1/clinical_trial_data/',methods=['PUT'])
def update_clinicalTrialData():
    '''edit clinical trial data'''
    clinicalTrialData=updateClinicalTrialData.updateClinicalTrialData()
    return(clinicalTrialData)
    


#########update clinical info#########
@app.route('/v1/clinical_info/',methods=['PUT'])
def updateClinicalInfo():
    '''edit clinical info'''
    clinicalInfo=updateclinical_info.updateClinicalInfo()
    return(clinicalInfo)

###########################################################################################################################
###########################################End of Put Calls################################################
###############################################################################################

###########################################################################################################################
###########################################Start of Delete Calls################################################
###############################################################################################

#########delete clinical info#########
@app.route('/v1/clinical_info/<id>/',methods=['DeLETE'])
def delete_clinicalInfo(id):
    '''delete clinical info'''
    clinicalInfo=deleteClinicalInfo.deleteClinicalInfo(id)
    return(clinicalInfo)


#########delete clinic#########
@app.route('/v1/clinical_trial_data/<id>/',methods=['DELETE'])
def deleteClinical_trialInfo(id):
    '''delete clinical info'''
    clinicaltrial=deleteClinicalTrialData.deleteClinicalTrialData(id)
    return(clinicaltrial)

#########delete special population#########
@app.route('/v1/special_population/<id>/',methods=['DELETE'])
def deletespecialPopulation(id):
    '''delete special population'''
    specialPopulation=deleteSpecialPopulation.deleteSpecailPopulation(id)
    return(specialPopulation)


#########delete pharmacokinetic properties#########
@app.route('/v1/pharmacokinetic_properties/<id>/',methods=['DELETE'])
def deletepharmacokineticProps(id):
    '''delete pharmaceuticokinetic properties'''
    pharmacokineticProps=deletePharmacokineticProps.deletePharmacokineticProps(id)
    return(pharmacokineticProps)


#########delete pharmacodynamic properties#########
@app.route('/v1/pharmacodynamic_props/<id>/',methods=['DELETE'])
def deletepharmacodynamicProps(id):
    '''delete pharmaceuticodynamic properties'''
    pharmacodynamicInfo=deletePharmacodynamicProps.deletePharmacodynamicProps(id)
    return(pharmacodynamicInfo)


#########update overdose#########
@app.route('/v1/pharmaceutical_info/<id>/',methods=['DELETE'])
def deletepharmaceuticalInfo(id):
    '''delete pharmaceutical info'''
    pharmaceuticalInfo=deletePharmaceuticalInfo.deletePharmaceuticalInfo(id)
    return(pharmaceuticalInfo)


#########delete overdose#########
@app.route('/v1/overdose/<id>/',methods=['DELETE'])
def deleteoverdose(id):
    '''delete overdose'''
    overdose=deleteOverdose.deleteOverdose(id)
    return(overdose)


#########delete non clinical info#########
@app.route('/v1/non_clinical_info/<id>/',methods=['DELETE'])
def delete_NonClinicalInfo(id):
    '''delete non clinical info'''
    nonClinicalInfo=deleteNonClinicalInfo.deleteNonClinicalInfo(id)
    return(nonClinicalInfo)


#########delete drugs#########
@app.route('/v1/drugs/<id>/',methods=['DELETE'])
def deletedrug(id):
    '''delete drug'''
    drug=deleteDrugs.deleteDrug(id)
    return(drug)


#########update manufacturer#########
@app.route('/v1/manufacturer/<id>/',methods=['DELETE'])
def deletemanufacturer(id):
    '''delete drug manufacturer'''
    manufacturer=deleteManufacturer.deleteManufacturer(id)
    return(manufacturer)


#########delete description#########
@app.route('/v1/descriptions/<id>/',methods=['DELETE'])
def deletedescription(id):
    '''delete drug description'''
    description=deleteDescription.deleteDescription(id)
    return(description)