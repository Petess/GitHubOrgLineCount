#!/usr/bin/python3

from github import Github

def getCredentials():
    f = open('.creds')
    creds = f.readline()
    f.close()
    return creds

def GetRepos():
    g = Github( getCredentials() ) 
    count = 0
    for repo in g.get_organization("GeoscienceAustralia").get_repos(type = 'public' ):
        print( repo.name )
        count = count + 1
    print( "There are " + str( count ) + " repositories" )

def themain():
    print("Started")
    GetRepos()
    
if __name__ == "__main__":
    themain()
