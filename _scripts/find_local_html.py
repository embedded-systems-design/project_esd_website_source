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
import glob
import yaml

download = False

folder = r'projects/project_embedded_systems_class/blog_new'
filename = '*.md'

filename_full = os.path.join(os.path.expanduser('~'),folder,filename)
files = glob.glob(filename_full)

search_string = '\[[^\]]*\]: (?!https?://)(?P<file>.*)\.html'

paths = {}

for file in files:
    # # lines = []
    with open(file) as f:
        s = f.read()
    #     # lines.extend(f.readlines())
    out = re.finditer(search_string,s)
    matches=list(out)
    if len(matches)>0:
        for match in matches:
            b = match.groupdict()
            if not b['file'] in paths:
                paths[b['file']]=[file]
            else:
                paths[b['file']].append(file)
with open(os.path.join(os.path.expanduser('~'),'paths.yaml'),'w') as f:
    yaml.dump(paths,f)

# corrections = {}
# for key in paths.keys():
    # corrections[key]=''
# with open(os.path.join(os.path.expanduser('~'),'corrections.yaml'),'w') as f:
    # yaml.dump(corrections,f)
with open(os.path.join(os.path.expanduser('~'),'corrections.yaml')) as f:
    corrections = yaml.load(f,Loader = yaml.Loader)

for key,files in paths.items():
    try:
        new_value = corrections[key]
        for file in files:
            full_filename2 = os.path.join(folder,file)
            with open(full_filename2) as f:
                s_orig = f.read()
                s = s_orig[:]
                s=s.replace(key,new_value)
            with open(full_filename2,'w') as f:
                f.write(s)
    except KeyError:
        pass
        
#         s_orig = f.read()
#         s = s_orig[:]
#         for aa,bb in replacements:
#             bb='../dl/'+bb
#             s=s.replace(aa,bb)
#     with open(full_filename2,'w') as f:
#         f.write(s)

# # in1 = lines[0]    
# def f1(asdf):
#     print(asdf)
#     return asdf

# replace_string = '\0 : \1\n'
# out = re.finditer(search_string,s)
# a = list(out)
# b = []
# for item in a:
#     b.append(item.groupdict())

# import yaml

# for ii in range(len(b)):
#     newname = 'image{0:04d}'.format(ii)+ext
#     b[ii]['url_new'] = newname

# filename2_full = os.path.join(folder,'dl_list1.yaml')
# with open(filename2_full,'w') as f:
#     yaml.dump(b,f)

    
# # %%
# newpath = os.path.join(folder,'dl')
# if download:

#     if os.path.exists(newpath):
#         shutil.rmtree(newpath)
#     os.mkdir(newpath)

#     for ii in range(len(b)):
#         url = b[ii]['url']
#         r = requests.get(url)
#         a,ext = os.path.splitext(url)
#         newname = 'image{0:04d}'.format(ii)+ext
#         newimage = os.path.join(newpath,b[ii]['url_new'] )
#         with open(newimage, 'wb') as f:
#              f.write(r.content)
        
#         # # Retrieve HTTP meta-data
#         print(r.status_code)
#         # print(r.headers['content-type'])
#         # print(r.encoding)    


# # %%
# import glob

# files = glob.glob(os.path.join(folder,'blog_new','**.md'))
# # %%

# file_dict = {}
# for item in b:
#     file_dict[item['file']]=[] 
# for item in b:
#     file_dict[item['file']].append((item['url'],item['url_new'],))
# # %%


# for filename,replacements in file_dict.items():
#     full_filename2 = os.path.join(folder,'blog_new',filename)
#     with open(full_filename2) as f:
#         s_orig = f.read()
#         s = s_orig[:]
#         for aa,bb in replacements:
#             bb='../dl/'+bb
#             s=s.replace(aa,bb)
#     with open(full_filename2,'w') as f:
#         f.write(s)
        