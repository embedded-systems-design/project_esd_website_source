---
title: Posts by Tag
---

{% capture all_tags %}{% for item in site.blog %}{% for tag in item.tags %}{{ tag }};{% endfor %}{% endfor %}{%endcapture%}
{% assign tag_words = all_tags | split:';' | sort | uniq %}

## Blog Categories

{% for word in tag_words %}
### {{word}}

{% for page in site.blog %}{% if page.tags contains word %} * [{{ page.title }}]({{ site.baseurl }}{{ page.url }})
{% endif%}{% endfor %}

{% endfor %}

### Untagged

{% for page in site.blog %}{% if page.tags.size == 0 %} * {% if page.title %}[{{ page.title }}]({{ page.url }}){% else %}[{{ page.url }}]({{ page.url }}){% endif %}
{% endif %}{% endfor %}

