#!/usr/bin/python3

from github import Github
import argparse

def getCredentials():
    f = open('.creds')
    creds = f.readline()
    f.close()
    return creds

def GetReposOfType(theType):
    g = Github( getCredentials() ) 
    returnList = []

    for repo in g.get_organization("GeoscienceAustralia").get_repos(type = theType ):
        returnList.append( repo.clone_url )

    return returnList

def writeFile( fileName, ListToWriteOut ):
    outfile = open(fileName,'w')
    for item in ListToWriteOut:
        outfile.write( item + "\n")
    outfile.close()
    return

def themain():
    parser = argparse.ArgumentParser()
    requiredName = parser.add_argument_group('required named arguments')
    parser.add_argument('-f', '--file',
                        help='Filename to write out', required=True)
    args = parser.parse_args()

    forkRepoList = GetReposOfType('forks')
    publicRepoList = GetReposOfType('public')
    publicWithoutForks = [x for x in publicRepoList if x not in forkRepoList]
    writeFile( args.file, publicWithoutForks)     

if __name__ == "__main__":
    themain()
