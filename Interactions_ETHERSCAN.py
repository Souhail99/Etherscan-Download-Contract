import json
import urllib
from web3 import Web3
from helpersForSourcecode import get_contract_content_list

# Network variables
etherscan_api_key ="YOUR_ETHERSCAN_API_KEY"



def getSourceCodeContract(adresse_contrat):

    url ="https://api.etherscan.io/api?module=contract&action=getsourcecode&address="+adresse_contrat+"&apikey="+etherscan_api_key
    resultat3 = 'Not Available'
    try:
        if(True):
            with urllib.request.urlopen(url) as url:
                    data = json.loads(url.read())
                    #print(data)
                    resultat1 = data['result']
                    resultat2 = resultat1[0]
                    resultat3 = resultat2['SourceCode']
                    try: 
                        data = json.loads(resultat3)
                    except ValueError as e:
                        dicsss = get_contract_content_list(resultat2, "ethereum")
                        newstr = ""
                        for item in dicsss:
                            newstr +=item["content"]
                        return newstr
                                                

    except:
        1
    return resultat3

# contract Address :
adresse_contrat = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
# Source code
sourceCode1 = getSourceCodeContract(adresse_contrat)
#where you want to write the source code
file_path = ""
file_path = file_path + "ethereum" + "__"  + adresse_contrat+".sol"
f = open(file_path, "w")
f.write(sourceCode1)
f.close()