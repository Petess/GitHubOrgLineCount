#!/bin/python3

from oauthlib.oauth2  import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from os import environ

# Setup a client to access the Bitbucket API
def setup_client():
    client_id = environ.get( 'client_id' )
    client_secret = environ.get( 'client_secret' )

    if ( ( client_id == None ) or ( client_secret == None ) ):
        print( "client_id and client_secret must be set" )
        exit(1)

    bitbucket_token_url="https://bitbucket.org/site/oauth2/access_token"
    user_url="https://bitbucket.org/api/2.0/users/users?"

    bitbucket_client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=bitbucket_client)
    token = oauth.fetch_token(token_url=bitbucket_token_url,client_id=client_id,client_secret=client_secret)

    client = OAuth2Session(client=bitbucket_client,token=token)
    return client

# Get all repository slugs 
def get_all_team_repo_slugs(client):
    bitbucket_repository_list_endpoint =  "https://bitbucket.org/api/2.0/repositories/GeoscienceAustralia?pagelen=100"

    current_repo_list_page = bitbucket_repository_list_endpoint 
    more_pages = True
    reposlugs = []

    while(more_pages):
        repo_result = client.get(current_repo_list_page).json()
        
        # Get all the repo slugs
        for item in repo_result[ 'values']: 
            # print( item.get('slug'))
            print( item.get('links')['clone'][1]['href'] )
            reposlugs.append( item.get('slug' ) )
        
        # Check if there is another page to scan
        if ( repo_result.get('next') == None ):
            more_pages = False
        current_repo_list_page = repo_result.get('next')

    print('There are ', len(reposlugs), ' repositories.')

    return reposlugs

def main():
    elclient = setup_client()
    all_repo_slugs = get_all_team_repo_slugs(elclient)

if __name__ == "__main__":
    main()
