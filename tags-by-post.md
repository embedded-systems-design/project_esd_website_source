---
title: Tags by Post
subtitle: this is text
---

{% for page in site.blog %}
## [{{ page.title }}]({{ site.baseurl }}{{ page.url }})
{% for tag in page.tags %}* {{tag}}
{% endfor %}
{% endfor %}
