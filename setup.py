try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jessica Spencer',
    'url': 'https://github.com/jesspencer/SKELETON.git.',
    'author_email': 'jessicaspencer12@gmail.com.',
    'version': '0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'

}
 setup(**config)
