<a className="gh-badge" href="https://datahub.io/@brauliobarahona/CKW_smart_meter_data?_gl=1*bvkdbm*_ga*MTI5ODg4NTcwNy4xNzU4NzI0Mjg5*_ga_R6X92HM43Q*czE3NTkxNzc1NDUkbzEwJGcxJHQxNzU5MTc3ODg3JGo2MCRsMCRoMA.."><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Descrition of the data

# Content of this repository

# Setup workflow to work remotely from a VM

In order to authenticate to git and be able to clone the repository, first make sure you have
# 1. a github account
# 2. a personal access token
# 3. a ssh key pair
# 4. a ssh key pair added to your github account
# 5. a ssh key pair added to your ssh-agent

# 1. create a new ssh key pair
```bash
ssh-keygen -t rsa -b 4096 -C "hintisberg"
ssh-keygen -t ecdsa -C "hintisberg in braulio's github account"
````

# copy the public key to your clipboard
```bash
pbcopy < ~/.ssh/id_rsa.pub
```

Or simply with `cat ~/.ssh/id_rsa.pub` and then copy from the terminal output.

# use standard output to copy the public key to your clipboard and then put it to clipboard
cat ~/.ssh/id_rsa.pub | pbcopy

# copy to cliboard without pbcopy
cat ~/.ssh/id_rsa.pub

# git clone