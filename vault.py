'''import hvac

client = hvac.Client(url='https://vault.uat.use1.crypto.gcp.efx/')
#client = hvac.Client(url='vault_uri: "https://vault.uat.use1.crypto.gcp.efx:443')
client.is_authenticated()

#read_config_response = client.secrets.gcp.read_config()
#print('Max TTL for GCP secrets engine set to: {max_ttl}'.format(max_ttl=read_config_response['data']['max_ttl']))

***********************************************************************************************************************

import 

token = 's.ZbErDdiOkfmQZqCSc0gYQ2ZS'
r = requests.post( "{}{}".format(vault_address, "/v1/sys/wrapping/unwrap"), headers={'X-Vault-Token': token})
response = r.json()
role_id = 'usis-gcp-vault-iam-role'
print(response)

************************************************************************************************************************

set JWT_CLAIMS="{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": 1597433520}"
set OAUTH_TOKEN = "ya29.c.Kn_YB_y0FOF_D2GEL58Y5OCGeP_1xXpd7Zl7UlJruRKcF_DbK5cAHa5-5U__-m0WqifNkiFUzJ93oPNY3ESLXZy_4ljALQmFEfGjvKq0-jSTb5HQM88M1YFm4nUyOY-nLF5dPHK72pUtuzru5teU8IbzZJHRlh9m55kZBmy79C2g"
set SERVICE_ACCOUNT = "ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com"
set PROJECT = "usis-risk-dec-npe-4816"

Error in Windows VM:

{
  "error": {
    "code": 401,
    "message": "Request had invalid authentication credentials. Expected OAuth 2 access token, login cookie or other valid authentication credential. See https://developers.google.com/identity/sign-in/web/devconsole-project.",
    "status": "UNAUTHENTICATED"
  }
}

#Above error resolved by using Git Bash shell
'''

Step 1:

#Generate OAUTH_TOKEN
curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"

Step 2:
#Get epoch time for JWT_CLAIMS

Step 3:
#Set variables updating parameters - epoch time and OAUTH_TOKEN
export JWT_CLAIMS="{\\\"aud\\\":\\\"vault/usis-gcp-vault-iam-role\\\", \\\"sub\\\": \\\"ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com\\\", \\\"exp\\\": 1597777920}"
export OAUTH_TOKEN="ya29.c.Kn_YB-Wfy_vLBSVyutGI9ukGASQ10GMWVjzxrSqdJxfaEbot5YvgOCSfa1FJdMuea4N8HsiTg125HR6dnPHzhNHaPCBNP8tSBPPWy77Fx1fy30V5d2sm4777seMvulcyYcygoXB5bLNje3-NhSLssjbd_CNFRtm735rbWGeF1sT6"
export PROJECT="usis-risk-dec-npe-4816"
export SERVICE_ACCOUNT="ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com"

Step 4:

#Add roles to service accounts
#These steps are prerequisites
#gcloud projects add-iam-policy-binding usis-risk-dec-npe-4816 --member 'serviceAccount:ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com' --role 'roles/iam.serviceAccountTokenCreator'
#gcloud projects add-iam-policy-binding usis-risk-dec-npe-4816 --member 'serviceAccount:ds-efx-us-di-tier-sa@usis-risk-dec-npe-4816.iam.gserviceaccount.com' --role 'roles/iam.serviceAccountKeyAdmin'



#Generate JWT Token
curl --header "Authorization: Bearer ${OAUTH_TOKEN}" --header "Content-Type: application/json" --request POST --data "{\"payload\": \"${JWT_CLAIMS}\"}" "https://iam.googleapis.com/v1/projects/${PROJECT}/serviceAccounts/${SERVICE_ACCOUNT}:signJwt"

Step 5:

#Create payload.json file
{
  "role": "usis-gcp-vault-iam-role",
  "jwt": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImNiZWI4OTVhZWVkMmQ3ODcyM2FiOTcxNzI5YjcyOTg5YzY0NjU4YTMiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJ2YXVsdC91c2lzLWdjcC12YXVsdC1pYW0tcm9sZSIsICJzdWIiOiAiZHMtZWZ4LXVzLWRpLXRpZXItc2FAdXNpcy1yaXNrLWRlYy1ucGUtNDgxNi5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsICJleHAiOiAxNTk3NDQwNTQwfQ.HExkcpiqG96gNlW5Ila1xnywt0P3ekNeeDyVqKYI4JqVv4FGb8cRb2aB-3aChuFf7sYmMFFeVUgKH6iZ2ampxl0GMaM3-fy1wOLJjFkd4AcqSFlzBh1Loml_utMEAZakiLWh9P5LTj6Zd5Ah5hxhfZjp6ukewQ1RJfyyHZvXlmWxWRLvh-hSg-77CouZWMryIsrNKn-o7g7BRJ7PpwK4lr0OotuhqoFKkGkZGs4spWDTcXjOL6c6ti4y0JFijMccpRfPAN9GMDNOhVBXIVRBwKKnrm319jMOr7P_ZYVbPvY7TJBRmX7A7CifdLXM0knaOYXV0N7sgWdwT1obNjYVXg"
}

Step 6:

#Log in to Vault via API call

#curl --request POST --data @payload.json https://vault.uat.use1.crypto.gcp.efx:443/v1/auth/gcp/login
#curl --request POST --insecure --header "X-Vault-Namespace: usis-ic-us-icsaas" --data @payload.json https://vault.uat.use1.crypto.gcp.efx/v1/auth/gcp/login
curl --request POST --insecure --header "X-Vault-Namespace: usis-ic-us-icsaas" --data @C:\\Users\\spotfireadmin\\Desktop\\payload.json https://vault.uat.use1.crypto.gcp.efx/v1/auth/gcp/login

Step 7:

#Read secret

#https://vault.uat.use1.crypto.gcp.efx/v1/vault/secrets/us-east-1/gcp/gcp-dev/psmicroservices/kv/ic-ditier-service
#https://vault.uat.use1.crypto.gcp.efx/v1/usis-ic-us-icsaas/kv/data/us-east-1/gcp/gcp-dev/psmicroservices/kv/usis-dibi-dev-user-ar

#curl --header "X-Vault-Token: s.IgxqPESu7885O1ceTq89u786.1E74G" --header "X-Vault-Namespace: usis-ic-us-icsaas" --insecure --request GET https://vault.uat.use1.crypto.gcp.efx/v1/vault/secrets/us-east-1/gcp/gcp-dev/psmicroservices/kv/dibi-attgbs-ar | jq
curl --header "X-Vault-Token: s.bVqsmq81XAb0bmO1jJcBKxJa.1E74G" --header "X-Vault-Namespace: usis-ic-us-icsaas" --insecure --request GET https://vault.uat.use1.crypto.gcp.efx/v1/usis-ic-us-icsaas/us-east-1/gcp/gcp-dev/psmicroservices/kv/usis-dibi-dev-user-ar 