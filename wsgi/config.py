import os
import sys

if 'OPENSHIFT_REPO_DIR' in os.environ:
     settings = {
          'static_path' : os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/static'),
          'template_path' : os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/templates'),
     }
else:
     settings = {
          'static_path' : os.path.join(os.getcwd(), 'wsgi/static'),
          'template_path' : os.path.join(os.getcwd(), 'wsgi/templates'),
     }
