# CodingBat #

* This directory contains my solutions to CodingBat - code practice problems.

* CodingBat problems can be found here:
[codingbat.net](https://codingbat.com/)

* These are python scripts I have created, modified or used. Some scripts are for fun, while others have valuable use in production.

* There's now {{scripts|length}} python file{%if scripts|length > 1%}s{% endif %} in this repo.

| Script  | DocString |
| ------------- | ------------- |
{% for x in scripts %}|<a href="./{{x.name}}">{{x.display}}</a>|{{x.docstring}}|
{% endfor %}
