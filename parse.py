"""
  Parse CKW open data hosted at https://open.data.axpo.com

  There are two datasets provided by CKW, one of them is ...:
    **Datensatz A** : dataset a, anonymized data
    **Datensatz B** : dataset b, aggregated data

  This scripts does the following:
    1. Download data from website
    2. Unzip data
    3. Parse data to a compressed format

  The file names can be parse from the website or a text file, see metatada.txt

  TODO: forrmat of file names is given, just create file name with user input
          YYYYMM.csv.gzs
  *Note: prepare the download directories before runnign the script
"""
import os
from bs4 import BeautifulSoup
import requests

# use beautiful soup to parse the website and extract the download links  
url_da = "https://open.data.axpo.com/%24web/index.html#dataset-a"

# get html content
html_content = requests.get(url_da).text # string

# parse html content, extract body from html content text
soup = BeautifulSoup(html_content, features="html.parser")
html_table = soup.find_all("table") # ResultSet object : dataset a (anonymized), dataset b (aggregated)

# extract tr from element tag of html_table containing file names of dataset a
tr_list = html_table[0].find_all("tr") 

# find in bs4.element.ResultSet
file_names = []
for tr_i in tr_list:
  fn = tr_i.find_all("th")[0].text
  
  if fn.endswith(".csv.gz"):
    file_names.append(fn)

    file_size = tr_i.find_all("td")[2].text
    date = tr_i.find_all("td")[1].text
    #link = tr_i.find_all("td")[-1].contents # link
  else:
    continue

# construct download url
_prefix = "https://open.data.axpo.com/%24web/"

# get file name from user input or from a list
#   fn0 = "ckw_opendata_smartmeter_dataset_a_202308.csv.gz" # for download
#   url0 = "https://open.data.axpo.com/%24web/ckw_opendata_smartmeter_dataset_a_202308.csv.gz"

""" download a batch of files
  1. given a local directory
  2. check if files exist
  3. try to download files from the website

  *!* Note: you need to have enough disk space, this naive approach will write empty files when
  there is not enough space, those you need to clean later
"""
# check if files exist
downloads = "/home/ubuntu/d^ata/downloads/ckw" #"/Users/tabaraho/ckw" # *.gz and *.csv files
for fi in file_names:
  fn = os.path.join(downloads, fi)
  
  if os.path.exists(fn):
    print("This file exisits: {}".format(fn))

  elif not os.path.exists(fn):
    # download file and save it to downloads
    url_i = _prefix + fi
    curl_cmd = f"curl -o {fn} {url_i}"

    print(curl_cmd)
    os.system(curl_cmd)
  
# Unzip files
for fi in file_names:
  fn = os.path.join(downloads, fi)
  fout = os.path.join(downloads, fi.replace(".gz", ""))
  if os.path.exists(fn):
    print("This file exists: {}".format(fn))
    
    # unzip file
    unzip_cmd = f"gunzip -c {fn} > {fout}"
    print(unzip_cmd)
    os.system(unzip_cmd)

