# from path import path
# import logging
# import sphinx
import sys

sys.path.append('..')
import easyprocess
sys.path.pop()

release = easyprocess.__version__
print release
project = 'EasyProcess'
author = 'ponty'
copyright = '2011, ponty'

# logging.basicConfig(level=logging.DEBUG)

# Extension
extensions = [
    # -*-Extensions: -*-
    'sphinx.ext.autodoc',
    'sphinxcontrib.programoutput',
    #     'sphinxcontrib.programscreenshot',
    'sphinx.ext.graphviz',
    'sphinxcontrib.autorun',
    #'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]
intersphinx_mapping = {'python': ('http://docs.python.org/', None)}
# intersphinx_mapping =  {'http://docs.python.org/': None}

# Source
master_doc = 'index'
templates_path = ['_templates']
source_suffix = '.rst'
exclude_trees = []
pygments_style = 'sphinx'

# html build settings
html_theme = 'default'
html_static_path = ['_static']

# htmlhelp settings
htmlhelp_basename = '%sdoc' % project

# latex build settings
latex_documents = [
    ('index', '%s.tex' % project, u'%s Documentation' % project,
     author, 'manual'),
]

# remove blank pages from pdf
# http://groups.google.com/group/sphinx-
# dev/browse_thread/thread/92e19267d095412d/d60dcba483c6b13d
latex_font_size = '10pt,oneside'

latex_elements = dict(
    papersize='a4paper',
)
