---
title: Cadence Posts
---

{% assign word="cadence" %}
### {{word}}

{% for page in site.pages %}{% if page.tags contains word %} * [{{ page.title }}]({{ site.baseurl }}{{ page.url }})
{% endif%}{% endfor %}

