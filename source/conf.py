# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'Sprawozdanie-z-laboratorium'
copyright = '2026, Norbert Antonovitch'
author = 'Norbert Antonovitch'

# -- General configuration ---------------------------------------------------
language = 'pl'

extensions = [
    'sphinx.ext.autodoc'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'fncychap': '\\usepackage[Sonny]{fncychap}',
    'extraclassoptions': 'openany,oneside',
    'printindex': '',
    'preamble': r'''
\usepackage{babel}
\usepackage{graphicx}
\usepackage{hyperref}
\setcounter{tocdepth}{2}
\raggedbottom

\renewcommand{\printindex}{}

\setlength{\parskip}{0pt plus 1pt}
\setlength{\parindent}{0pt}

\setlength{\headheight}{14.49998pt}
''',
    'sphinxsetup': 'hmargin={0.7in,0.7in}, vmargin={0.7in,0.7in}, verbatimwithframe=false',
}

latex_documents = [
    (
        'index', 
        '276209-bazy-danych-sprawozdanie.tex', 
        'Sprawozdanie z Laboratorium: Bazy Danych',
        'Norbert Antonovitch (276209)',
        'manual'
    ),
]

latex_show_urls = 'footnote'
latex_show_pagerefs = False
latex_max_embed_pages = 0

latex_domain_indices = False
