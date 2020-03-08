from requet import Requet, Log
from bs4 import BeautifulSoup
"""
Initialisation
"""
my_stoken = 'NULL'
solebox		 = Requet(True, 'www.solebox.com')
solebox.useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'



def new_session():
    global solebox
    global my_stoken

    solebox.requet('/en/my-account/',
        method='GET',
        headers={
                'Cache-Control': 'no-cache',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'referer': 'https://www.solebox.com/index.php?lang=1&'
                }
    )

    '''
    Récupère le "stoken" pour les futures requêtes
    '''
    solebox_soup = BeautifulSoup(solebox.response,"html.parser")
    my_stoken = solebox_soup.find('input',attrs={'name':'stoken'})['value']


def create_account(email,pwd,prenom,nom,street,numero_rue,ville,code_postal,tel):
    global solebox
    global my_stoken

    data_creation_compte = 'stoken='+my_stoken+'&lang=1&listtype=&actcontrol=account&cl=user&fnc=createuser&reloadaddress=&blshowshipaddress=1&invadr%5Boxuser__oxfname%5D='+prenom+'&invadr%5Boxuser__oxlname%5D='+nom+'&invadr%5Boxuser__oxstreet%5D='+street+'&invadr%5Boxuser__oxstreetnr%5D='+numero_rue+'&invadr%5Boxuser__oxaddinfo%5D=&invadr%5Boxuser__oxzip%5D='+code_postal+'&invadr%5Boxuser__oxcity%5D='+ville+'&invadr%5Boxuser__oxcountryid%5D=a7c40f63272a57296.32117580&invadr%5Boxuser__oxstateid%5D=&invadr%5Boxuser__oxbirthdate%5D%5Bday%5D=12&invadr%5Boxuser__oxbirthdate%5D%5Bmonth%5D=6&invadr%5Boxuser__oxbirthdate%5D%5Byear%5D=1994&invadr%5Boxuser__oxfon%5D='+tel+'&lgn_usr='+email+'&lgn_pwd='+pwd+'&lgn_pwd2='+pwd+'&userform='


    solebox.requet('/index.php?lang=1&',
        method='POST',
        headers={
            'Cache-Control': 'max-age=0',
            'authority':'www.solebox.com',
            'cache-control': 'max-age=0',
            'Content-Length':len(data_creation_compte),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'origin':'https://www.solebox.com',
            'referer':'https://www.solebox.com/en/my-account/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
	},
    body =data_creation_compte

    )

def login(email,pwd):
    global solebox
    global my_stoken


    data_login ='stoken='+my_stoken+'&lang=0&listtype=&actcontrol=account&fnc=login_noredirect&cl=account&lgn_usr='+email+'&lgn_pwd='+pwd

    solebox.requet('/index.php?',
        method='POST',
    	headers={
            'Cache-Control': 'max-age=0',
            'authority':'www.solebox.com',
            'cache-control': 'max-age=0',
            'Content-Length':len(data_login),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'origin':'https://www.solebox.com',
            'referer':'https://www.solebox.com/en/my-account/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        },
        body = data_login
    )

def ajoute_chaussure():
    global solebox
    global my_stoken


    """
    Les chaussures utilisées en taille 46 (peut être en rupture de stock !)
    https://www.solebox.com/index.php?cl=details&cnid=500036&anid=50157&listtype=list&
    """
    data_chaussure='stoken='+my_stoken+'&lang=1&cnid=500036&listtype=list&actcontrol=details&cl=details&aid=50165&anid=50157&parentid=50157&panid=&fnc=tobasket&am=1'

    solebox.requet('/index.php?lang=1&',
        method='POST',
    	headers={
            'Cache-Control': 'max-age=0',
            'authority':'www.solebox.com',
            'cache-control': 'max-age=0',
            'Content-Length':len(data_chaussure),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'origin':'https://www.solebox.com',
            'referer':'https://www.solebox.com/Footwear/Running/Solution.html',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
            },
            body = data_chaussure
    )

    solebox.requet('/index.php?cl=details&cnid=500036&anid=50157&listtype=list&',
        method='GET',
    	headers={
            'Cache-Control': 'no-cache',
            'referer':'https://www.solebox.com/Footwear/Running/Solution.html',
            'dnt':'1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
    )
