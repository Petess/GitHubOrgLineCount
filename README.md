# GitHubOrgLineCount
GitHubOrgLinCount is a set of scripts to count the number of lines of code in an organisation

# Installation

```bash
pip install -r requirements.txt
```

A Github authorisation token also needs to be created and placed into a .creds file in the local directory. 

# Usage

1. Run GetOrgRepos.py and redirect the output to a text file. 

2. Run repoListLineCount.sh on the text file from step one. 


# Notes

The Script from : https://stackoverflow.com/questions/26881441/can-you-get-the-number-of-lines-of-code-from-a-github-repository can quickly count the number of lines from a repository.

This repo will list all the repositories from an organisation : 
https://gist.github.com/ralphbean/5733076

This requires the Github Python API.

# Todo

1. Currently all repositories are downloaded and deleted and also placed into the same directory. This results in the totals being across the entire organisation without the projects being separate. Instead getting the Zip files of the repositories with the option of retaining the downloaded repositories will be examined. 

