# Project Euler #

* This directory contains my solutions to Project Euler problems.

* Project Euler problems can be found here:
[ProjectEuler.net](https://projecteuler.net/archives)

* These are python scripts I have created, modified or used. Some scripts are for fun, while others have valuable use in production.

* There's now {{scripts|length}} python file{%if scripts|length > 1%}s{% endif %} in this repo.

| Problem Number  | Script  | DocString |
| ------------- | ------------- | ------------- |
{% for x in scripts %}|{{x.problem_num}}|<a href="./src/{{x.name}}">{{x.display}}</a>|{{x.docstring}}|
{% endfor %}
