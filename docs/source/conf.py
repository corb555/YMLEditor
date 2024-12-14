# Configuration file for the Sphinx documentation builder.
#
# To build .rst files for YMLEditor modules:
# Go to the projectroot folder (YMLEditor)
# sphinx-apidoc -o docs/source YMLEditor

import os
import sys

sys.path.insert(0, os.path.abspath('../../YMLEditor'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'YMLEditor'
copyright = '2024, corb555'
author = 'corb555'
release = '0.11'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon', 'myst_parser', ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
