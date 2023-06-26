import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..' 'templates'))

root_folder = os.path.abspath(os.path.dirname(__file__))
print(root_folder)
print(template_dir)
