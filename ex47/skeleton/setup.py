try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'ex47game',
        'author': 'May Zin Thwe',
        'url': 'URL to get it at.'
        'download_url': 'Where to download it.',
        'author_email': 'mayzinthwe62@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47', 'bin'],
        'scripts': ['weapons'],
        'name': 'ex47game'
        }

setup(**config)
