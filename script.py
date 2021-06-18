from googleads import ad_manager
from googleads import oauth2

key_file = 'C:/Users/aaguerrevere/gamapi-317120-99b0a97326bc.json'

# Initialize the GoogleRefreshTokenClient using the credentials you received
# in the earlier steps.
oauth2_client = oauth2.GoogleServiceAccountClient(
    key_file, oauth2.GetAPIScope('ad_manager'))

# Initialize the Ad Manager client.
ad_manager_client = ad_manager.AdManagerClient(oauth2_client, 'gamapi_app')
print(ad_manager_client)

