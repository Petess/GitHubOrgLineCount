# GitHubOrgLineCount
GitHubOrgLinCount is a set of scripts to count the number of lines of code in an organisation. 

# Installation

```bash
pip install -r requirements.txt
```

A Github authorisation token also needs to be created and placed into a .creds file in the local directory. 

# Usage

1. Run GetOrgRepos.py and redirect the output to a text file. 

2. Run repoListLineCount.sh on the text file from step one, also with an argument of where the summaries of each repository will go. 


# Notes

The Script from : https://stackoverflow.com/questions/26881441/can-you-get-the-number-of-lines-of-code-from-a-github-repository can quickly count the number of lines from a repository.

This repo will list all the repositories from an organisation : 
https://gist.github.com/ralphbean/5733076

This requires the Github Python API.

The script repoListLineCount.sh will run on any list of github repositories. Thus if a list is obtained from Bitbucket or other repository list that also works. 

repoListLineCount.sh can be used on any list of git repositories. It has been tested on a list of several hundred Git repositories. 

# Todo

