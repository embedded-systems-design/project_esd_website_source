## honestly don't remember
Find: ```(\n)*(?<abc>[a-zA-Z0-9\-\.]*.md(.old)*)\:[0-9]+\: +\[[0-9]*\]\: (?<xyz>[a-zA-Z0-9\-\.\/\:_\%]*)```
Replace: ```$<abc> : $<xyz>\n```


## find blogger pages and replace with local

Find: ```https*://esdresources.blogspot.com/[0-9]+/[0-9]+/([a-zA-Z\-_0-9]*.html)```
Replace: ```$1```


## Find all local pages

Find: ```\[[^\]]*\]: (?!https://)(?!http://)([a-zA-Z0-9\-]*).html```
(see script for updat)

## remove all image sizing:

find:
(.jpg)?(.png)?\)\{width ?= ?"[0-9]*.?[0-9]*(?:in)?" height ?= ?"[0-9]*.?[0-9]*(?:in)?"\}

replace: 
$1$2)

## find images 

find:
(!\[[^\]]*\]\([^\)]*\))
$1{class="img-fluid"}