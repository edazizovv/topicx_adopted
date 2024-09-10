#
import setuptools
from setuptools import setup


metadata = {'name': 'topicx_adopted',
            'maintainer': 'Edward Azizov',
            'maintainer_email': 'edazizovv@gmail.com',
            'description': 'Adopted package version of NLP research repo',
            'license': 'MIT',
            'url': 'https://github.com/edazizovv/topicx_adopted',
            'download_url': 'https://github.com/edazizovv/topicx_adopted',
            'packages': setuptools.find_packages(),
            'include_package_data': True,
            'version': '0.1.0',
            'long_description': 'Author of the research: Zihan Zhang (@ZhangzihanGit). Please find the original repo on https://github.com/hyintell/topicx',
            'python_requires': '==3.9.*',
            'install_requires': []}

setup(**metadata)
