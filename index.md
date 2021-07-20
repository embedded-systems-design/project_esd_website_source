---
title: Home
layout: page
---

{% capture all_tags %}{% for item in site.blog %}{% for tag in item.tags %}{{ tag }};{% endfor %}{% endfor %}{%endcapture%}
{% assign tag_words = all_tags | split:';' | sort | uniq %}

## Blog Categories

{% for word in tag_words %}[{{word}}](#{{word | strip | lower | replace: " ", "-"}}), {% endfor %}

<div class="row">
{% for word in tag_words %}
<div class="col-md-6 col-xs-12">
<div class="card">
{%comment%}
<img src="..." class="card-img-top" alt="...">
{%endcomment%}
<div class="card-body">
<h5 class="card-title">{{word}}</h5>

<ul>
{% for page in site.blog %}
{% if page.tags contains word %} 
<li>
<a href="{{ site.baseurl }}{{ page.url }}" id="{{word | strip | lower | replace: " ", "-"}}">{{ page.title }}</a>
</li>
{% endif%}
{% endfor %}
</ul>



{%comment%}
<a href="#" class="btn btn-primary">Go somewhere</a>
{%endcomment%}
</div>
</div>
</div>
{% endfor %}
</div>

### Untagged

{% for page in site.blog %}{% if page.tags.size == 0 %} * {% if page.title %}[{{ page.title }}]({{ page.url }}){% else %}[{{ page.url }}]({{ page.url }}){% endif %}
{% endif %}{% endfor %}


{% comment %}

## Main Modules

# Introduction

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5

body text

## Test Stuff

sadfasdf
$$A=B^2$$
asdfkjasldfj

<div class="alert alert-warning">
here is a warning
</div>

<div class="alert alert-danger">
here is a danger
</div>

```python
if a:
    asdf=4.0
```

{% endcomment %}
