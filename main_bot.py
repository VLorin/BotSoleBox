from src_bot import new_session,create_account,login,ajoute_chaussure

"""
Information relative au compte à créer (ou se connecter)
Par défaut le pays est la France
"""

email = 'testvincent2@salut.fr'
pwd = 'Salutcestcool55'
prenom = 'Vincent'
nom = 'Wiunj'
street = 'Rue de la moutarde'
numero_rue = '55'
ville = 'Paris'
code_postal = '59000'
tel = '0653468255'



"""
Choisir "create_account()" OU "login()" !
"""

new_session()
#create_account(email,pwd,prenom,nom,street,numero_rue,ville,code_postal,tel)
#Lors de la création d'un compte on est déjà connecté !
login(email,pwd)
ajoute_chaussure()