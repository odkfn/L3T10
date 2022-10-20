# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Source for this: https://www.freecodecamp.org/news/sphinx-for-django-documentation-2454e924b3bc/
import os
import sys
import django # as of Sphinx 1.7 need to import Django
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'bandPage.settings' # Need to manually change this folder name
django.setup() # Also as of Sphinx 1.7 need to set environment or Sphinx doesn't recognise Django

project = 'silverbyskyline'
copyright = '2022, scott lynch'
author = 'scott lynch'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon'
    
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
