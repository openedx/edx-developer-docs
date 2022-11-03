# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""
edx-developer-docs documentation build configuration file.

This file is execfile()d with the current directory set to its
containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.
"""

from __future__ import absolute_import, unicode_literals

import os
import sys

import edx_theme

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

VERSION = '1.0.0'

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'edx_theme',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx_reredirects',
]

redirects = {}

# A list of warning types to suppress arbitrary warning messages.
suppress_warnings = [
    'image.nonlocal_uri',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Open edX Developer Docs'
copyright = edx_theme.COPYRIGHT  # pylint: disable=redefined-builtin
author = edx_theme.AUTHOR
project_title = 'Open edX Developer Documentation'
documentation_title = "{project_title}".format(project_title=project_title)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = VERSION
# The full version, including alpha/beta/rc tags.
release = VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Adds files to auto-labels for sections (e.g. :ref:`path/to/file:Section title`)
autosectionlabel_prefix_document = True

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

def edx_rtd_url(slug):
    """Use this with the readthedoc project slug to create the full URL."""
    return f"https://edx.readthedocs.io/projects/{slug}/en/latest/"

intersphinx_mapping = {
    "openreleasenotes" : (edx_rtd_url("open-edx-release-notes"), None),
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'edx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {}
html_theme_options['includehidden'] = True
html_theme_options['navigation_depth'] = 4


# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [edx_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Provides for custom behavior such as where links open.

html_js_files = [
    'js/custom.js'
]

# Output file base name for HTML help builder.
htmlhelp_basename = '{project_name}doc'.format(project_name=project)

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_target = '{project}.tex'.format(project=project)
latex_documents = [
    (master_doc, latex_target, documentation_title,
     author, 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, project_title, documentation_title,
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, project_title, documentation_title,
     author, project_title, 'Open edX Developer Documentation',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
