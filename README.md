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