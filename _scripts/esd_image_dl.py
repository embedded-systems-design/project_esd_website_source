# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:03:11 2021

@author: danaukes
"""

import os
import sys
import re
import requests
import shutil

download = False

folder = r'C:\Users\danaukes\projects\project_embedded_systems_class'
filename = 'dl_list.txt'

filename_full = os.path.join(folder,filename)

# lines = []
with open(filename_full) as f:
    s = f.read()
    # lines.extend(f.readlines())
    
# in1 = lines[0]    
def f1(asdf):
    print(asdf)
    return asdf

search_string = '(\n)*(?P<file>[a-zA-Z0-9\-\.]*.md(.old)*)\:[0-9]+\: +\[\!*\[*\]*\[*[0-9]*\]+\: (?P<url>[a-zA-Z0-9\-\.\/\:_\%]*)'
replace_string = '\0 : \1\n'
out = re.finditer(search_string,s)
a = list(out)
b = []
for item in a:
    b.append(item.groupdict())

import yaml

for ii in range(len(b)):
    newname = 'image{0:04d}'.format(ii)+ext
    b[ii]['url_new'] = newname

filename2_full = os.path.join(folder,'dl_list1.yaml')
with open(filename2_full,'w') as f:
    yaml.dump(b,f)

    
# %%
newpath = os.path.join(folder,'dl')
if download:

    if os.path.exists(newpath):
        shutil.rmtree(newpath)
    os.mkdir(newpath)

    for ii in range(len(b)):
        url = b[ii]['url']
        r = requests.get(url)
        a,ext = os.path.splitext(url)
        newname = 'image{0:04d}'.format(ii)+ext
        newimage = os.path.join(newpath,b[ii]['url_new'] )
        with open(newimage, 'wb') as f:
             f.write(r.content)
        
        # # Retrieve HTTP meta-data
        print(r.status_code)
        # print(r.headers['content-type'])
        # print(r.encoding)    


# %%
import glob

files = glob.glob(os.path.join(folder,'blog_new','**.md'))
# %%

file_dict = {}
for item in b:
    file_dict[item['file']]=[] 
for item in b:
    file_dict[item['file']].append((item['url'],item['url_new'],))
# %%


for filename,replacements in file_dict.items():
    full_filename2 = os.path.join(folder,'blog_new',filename)
    with open(full_filename2) as f:
        s_orig = f.read()
        s = s_orig[:]
        for aa,bb in replacements:
            bb='../dl/'+bb
            s=s.replace(aa,bb)
    with open(full_filename2,'w') as f:
        f.write(s)
        