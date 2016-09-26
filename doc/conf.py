# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.abspath('../'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'
project = u'can'
copyright = u'2016, Brian Thorne et al.'
author = u'Brian Thorne et al.'
# The short X.Y version.
version = u'1.5.2'
# The full version, including alpha/beta/rc tags.
release = u'1.5.2'

language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
today = False
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

pygments_style = 'sphinx'
todo_include_todos = True

html_theme = 'alabaster'
#html_static_path = ['_static']
html_show_sourcelink = False


# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'can', u'can Documentation',
     [author], 1)
]
