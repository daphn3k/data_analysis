from setuptools import setup

setup(name='dataexploration',
      version='0.1',
      description='Functions for exploration of pandas.DataFrame content',
      url='http://github.com/daphn3k/data_analysis',
      author='Daphne',
      license='GNU GLP v3.0',
      packages=['dataexploration'],
      install_requires=['pandas', 'numpy', 'matplotlib', 'seaborn'],
      zip_safe=False)
