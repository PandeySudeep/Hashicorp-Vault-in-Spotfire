# Hashicorp Vault

Hashicorp Vault provides features to store confidential elements like username, password, credentials etc. that an organization tries to secure. Spotfire can communicate with Hashicorp Vault and access the information stored in the vault.

The code written is in python via Spotfire's Python Data Function. The code does include key steps like

- authenticate against Hashicorp Vault
- generate tokens
- read the informationn stored in Hashicorp Vault in JSON format
- parse JSON data
