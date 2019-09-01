from setuptools import setup

setup(name='dataframeplots',
      version='0.1',
      description='Functions for plotting pandas.DataFrame content',
      url='http://github.com/daphn3k/data_analysis',
      author='Daphne',
      license='GNU GLP v3.0',
      packages=['dataframeplots'],
      install_requires=['pandas', 'matplotlib.pyplot', 'seaborn',],
      zip_safe=False)
