# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0,os.path.abspath(".."))

def setup(app):
    app.add_css_file('css/custom.css') 


project = 'Exams Bank'
copyright = '2023, Mohamed Aymn Khanfour'
author = 'Mohamed Aymn Khanfour'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# used theme: https://sphinxthemes.com/themes/awesome
html_theme = "sphinxawesome_theme"
html_static_path = ['_static']

# html_sidebars = {
#     '**': ['globaltoc.html']
# }