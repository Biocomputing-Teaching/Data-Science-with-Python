# About the course Data-Science-with-Python

This repo contains the main contents of a course on `Data Science with Python`. Contents of this course are used in the study abroad subject with the same name at the [Faculty of Sciences, Technology and Engineering](https://mon.uvic.cat/fcte/) at the [UVic-UCC](https://www.uvic.cat).

## Instructions to build the HTML site

The repo contains an HTML site that can be accessed through [this link](https://compbiochbiophlab.gihub.io/Data-Science-with-Python/intro.html). To build the site when updating the material of the repo, you should install [jupyter book](https://jupyterbook.org/en/stable/intro.html) and [ghp-import](https://pypi.org/project/ghp-import/), to make the handling of the `gh-pages` branch easier. In short, once installed and assuming that your local repo copy is `<local_github>/Tools` do the following:

```
cd <local_github>
jb build Data-Science-with-Python; cd Data-Science-with-Python; git add .; git commit -m "update"; git push; ghp-import -n -p -f _build/html
```