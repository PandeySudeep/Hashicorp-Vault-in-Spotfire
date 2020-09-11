'''
#!YMI)VB*~#|Z\u003ceanlR=\u003cA|17O

unicodestring = "!YMI)VB*~#|Z\u003ceanlR=\u003cA|17O"
utf8string = unicodestring.encode("utf-8")
#asciistring = unicodestring.encode("ascii")
#isostring = unicodestring.encode("ISO-8859-1")
#utf16string = unicodestring.encode("utf-16")
#print (utf8string)
#print (isostring)
#print (utf16string)
print (utf8string.decode("utf-8"))

#Get epoch time for JWT_CLAIMS
import datetime
timestamp = datetime.datetime(2020, 8, 19, 12, 13).timestamp()
print(timestamp)


#Generate OAUTH_TOKEN
#curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"

import json
import requests

api_url_base='http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token'
#headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(api_token)}
headers = {'Metadata-Flavor':'Google'}
response = requests.get(api_url_base, headers=headers)
print (response)  
print (response.json())



#Generate OAUTH_TOKEN
#curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"

import json
import requests

api_url_base='https://iam.googleapis.com/v1/projects/usis-risk-dec-npe-4816/serviceAccounts/ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com:signJwt'

#OAUTH_TOKEN="ya29.c.Kn_YB3nV-QKdwEvjMVCy23-yo0_WKF383LLFtnf_N7MV1vEhnbj0lWxtLLZITdKJPJZAvJLSaJ93dPzMTo3gshk34tfVs6rrXSI-x-nzjnSXzH5JoQK1QhnWxlVy-RgZr4f_Pg7jYJdiB7lQop0JPMl8qwERiCg8Dujh6jNCtz94"
#JWT_CLAIMS=""
#PROJECT=""
#SERVICE_ACCOUNT=""

payload="{\"payload\": \"{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": 1598043240}\"}"
#_payload='{\"payload\": \"{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": 1598036400}\"}'
#_payload='{"aud":"vault/usis-gcp-vault-iam-role", "sub": "ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com", "exp": 1598041740}'

authorization='Bearer ya29.c.Kn_ZB7Dcn8PVpL9bKSFYKTP3Shq-ifuQrILmTxOzAHrdvLO4LUu8EkobTqGWULWos-EBMbwkj7-yuTLtXvNrxss0Cfog2Q3JBd7CPhWciGTeYoOPgCjSpxA_zPUkn6XP0-jNYdbpyUfRdpQXbJgDAx2-TdLkEoFcu3CR9E_PlllF'
contenttype='application/json'
#payload=json.loads(_payload)
print(payload)
print(type(payload))
headers={'Authorization':authorization,'Content-Type':contenttype}
#data={'payload': json.dumps(payload)}
#data={'payload':payload }
#data=payload
response = requests.post(api_url_base,data=payload,headers=headers)
print (response)  
#print (response.json())
print(response.text)


#Generate JWT Token
#curl --header "Authorization: Bearer ya29.c.Kn_ZBwyBlk8rNS5j3J1dNPDuoAx-li0fIkb4qqeu6QXXWwgdzGDjz0k5jUj7em_Z7a2KOkYVGHHutlbZNf6rdBEHTRSNmf4z17frFuRYKreWyt5P0O3i78gIpOJF7ybLV-13dXlQyYqkHps14FlGbQmUHqvWJ9GChg6AUyITdyoo" --header "Content-Type: application/json" --data "{\"payload\": \"{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": 1598033820}\"}" --request POST "https://iam.googleapis.com/v1/projects/usis-risk-dec-npe-4816/serviceAccounts/ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com:signJwt"

#Generate OAUTH_TOKEN
curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"

#Generate JWT Token
curl --header "Authorization: Bearer ya29.c.Kn_ZB48BJjvhU6_5F4S1KX5zKG3-XRFvfSCNE64XdkXW8R755Rh95M7jGSyh4JgvTQnkL4s65PCy89V_9RL28qxKCfcGKDBRytH8WL9gcdUnRdowxZHy2JNzDX9fiL6l2jJMb9uyqlEbetXdmGIVOZ28k4xFAtqm-ItbRRs1Hk4Y" --header "Content-Type: application/json" --data "{\"payload\": \"{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": 1598299500}\"}" --request POST "https://iam.googleapis.com/v1/projects/usis-risk-dec-npe-4816/serviceAccounts/ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com:signJwt"

#Create payload.json file
{
  "role": "usis-gcp-vault-iam-role",
  "jwt": ""
}

#Log in to Vault via API call

curl --request POST --insecure --header "X-Vault-Namespace: usis-ic-us-icsaas" --data @C:\\Users\\spotfireadmin\\Desktop\\payload.json https://vault.uat.use1.crypto.gcp.efx/v1/auth/gcp/login

def getJWTToken():
    import json
    import requests
    
    api_url_base='https://iam.googleapis.com/v1/projects/usis-risk-dec-npe-4816/serviceAccounts/ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com:signJwt'
    payload="{\"payload\": \"{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": 1598301960}\"}"
    authorization='Bearer ya29.c.Kn_ZBwcobl_qsJGjUpkrWTAd5M4rYb1mAbH3XzjDu_HlB63J06cXsTxXjrL5nkc0VLmduS2KOBegsIVJ7gvZnbw7rfIoD31sB9oRuAq9VfRfAy98MVlATL5lpArv_c_Ahvi2D28pxJQx57yKp38Vktnh3vW0AdpbvJMQVkPOw13v'
    contenttype='application/json'
    headers={'Authorization':authorization,'Content-Type':contenttype}
    response = requests.post(api_url_base,data=payload,headers=headers)
    #print('Response in TEXT FORMAT:')
    print(response.text)
    #print('Type of Response Object:')
    #print(type(response))
    print('Converting Response object to JSON:')
    print(type(response.json()))
    print(response.json())
    print('Converting JSON response to String:')
    respStr=str(response.json().get("signedJwt"))
    print(respStr)
    #print(type(respStr))
    #print('length of response string')
    #print(len(respStr))
    #print('First Character:')
    #print(respStr[0])
    #print('Last Character:')
    #print(respStr[len(respStr)-1])
    #i=0
    #while(i<len(respStr)):
        #print(respStr[i])
        #i=i+1
    return respStr
    #print (response)
    #print(response.text)
#print(getJWTToken())
#print(type(getJWTToken()))
getJWTToken()

import json
import requests

api_url_base='https://vault.uat.use1.crypto.gcp.efx/v1/auth/gcp/login'
jwt=getJWTToken()
print("************************************************************************")
print(jwt)
print(type(jwt))
print("************************************************************************")
_data='{"role": "usis-gcp-vault-iam-role","jwt": \"'+jwt+'\"}'
print("##########################################################################")
print(_data)
print(type(_data))
print("###########################################################################")
headers={'X-Vault-Namespace': 'usis-ic-us-icsaas'}
#data = json.loads(_data)
response = requests.post(api_url_base,data=_data,headers=headers,verify=False)
print(response)
print(response.text)


#Generate OAUTH_TOKEN
curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"

import json
import requests

api_url_base='http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token'
#headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(api_token)}
headers = {'Metadata-Flavor':'Google'}
response = requests.get(api_url_base, headers=headers)
print (response)
OAUTH_TOKEN=str(response.json().get("access_token"))  
print (OAUTH_TOKEN)

import json
import requests
def getJWTToken():    
    api_url_base='https://iam.googleapis.com/v1/projects/usis-risk-dec-npe-4816/serviceAccounts/ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com:signJwt'
    payload="{\"payload\": \"{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": 1598541900}\"}"
    authorization='Bearer '+OAUTH_TOKEN
    contenttype='application/json'
    headers={'Authorization':authorization,'Content-Type':contenttype}
    response = requests.post(api_url_base,data=payload,headers=headers)
    respStr=str(response.json().get("signedJwt"))
    return respStr


api_url_base='https://vault.uat.use1.crypto.gcp.efx/v1/auth/gcp/login'
jwt=getJWTToken()
_data='{"role": "usis-gcp-vault-iam-role","jwt": \"'+jwt+'\"}'
headers={'X-Vault-Namespace': 'usis-ic-us-icsaas'}
response = requests.post(api_url_base,data=_data,headers=headers,verify=False)
auth=(response.json().get("auth"))
clientToken=auth.get('client_token')

#Read
#curl --header "X-Vault-Token: s.DUZ5z7HqQ6BTEZxgS4tdtfZn.1E74G" --insecure --request GET https://vault.uat.use1.crypto.gcp.efx/v1/usis-ic-us-icsaas/us-east-1/gcp/gcp-dev/psmicroservices/kv/dibi-attgbs-ar

api_read='https://vault.uat.use1.crypto.gcp.efx/v1/usis-ic-us-icsaas/us-east-1/gcp/gcp-dev/psmicroservices/kv/dibi-attgbs-ar'
headers={'X-Vault-Token':clientToken}
response=requests.get(api_read,headers=headers,verify=False)
secret_data=response.json().get("data")
pwd=secret_data.get('di.db.map.attgbsar.dbsecrete')
username=secret_data.get('di.db.map.attgbsar.username')

print(response.text)
print(pwd)
print(username)

'''

import json
import requests

api_url_base='http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token'
headers = {'Metadata-Flavor':'Google'}
response = requests.get(api_url_base, headers=headers)
OAUTH_TOKEN=str(response.json().get("access_token"))  
print('OAUTH_TOKEN')
print(OAUTH_TOKEN)

#Get epoch time for JWT_CLAIMS
import datetime
now=datetime.datetime.now()
myTime=now+datetime.timedelta(minutes = 10)
timestamp = int(datetime.datetime(myTime.year, myTime.month, myTime.day, myTime.hour, myTime.minute).timestamp())
print('timestamp')
print(timestamp)

import json
import requests
def getJWTToken():    
    api_url_base='https://iam.googleapis.com/v1/projects/usis-risk-dec-npe-4816/serviceAccounts/ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com:signJwt'
    payload='{\"payload\": \"{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": '+str(timestamp)+'}\"}'
    authorization='Bearer '+OAUTH_TOKEN
    contenttype='application/json'
    headers={'Authorization':authorization,'Content-Type':contenttype}
    response = requests.post(api_url_base,data=payload,headers=headers)
    respStr=str(response.json().get("signedJwt"))
    return respStr


api_url_base='https://vault.uat.use1.crypto.gcp.efx/v1/auth/gcp/login'
jwt=getJWTToken()
_data='{"role": "usis-gcp-vault-iam-role","jwt": \"'+jwt+'\"}'
headers={'X-Vault-Namespace': 'usis-ic-us-icsaas'}
response = requests.post(api_url_base,data=_data,headers=headers,verify=False)
auth=(response.json().get("auth"))
clientToken=auth.get('client_token')


api_read='https://vault.uat.use1.crypto.gcp.efx/v1/usis-ic-us-icsaas/us-east-1/gcp/gcp-dev/psmicroservices/kv/dibi-attgbs-ar'
headers={'X-Vault-Token':clientToken}
response=requests.get(api_read,headers=headers,verify=False)
secret_data=response.json().get("data")
pwd=secret_data.get('di.db.map.attgbsar.dbsecrete')
username=secret_data.get('di.db.map.attgbsar.username')
