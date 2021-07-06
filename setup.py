from setuptools import setup, find_packages
import os

version = '0.7.0'

setup(name='cellml.api.pmr2',
      version=version,
      description="CellML API utilities for PMR2",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Tommy Yu',
      author_email='tommy.yu@auckland.ac.nz',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cellml', 'cellml.api'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'cgrspy',
          'lxml',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
