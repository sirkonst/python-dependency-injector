"""`Dependency injector` setup script."""
from setuptools import setup


setup(name='acr-dependency-injector',
      version='0.1',
      description='Python dependency injection framework',
      long_description='Temporary package',
      author='ETS Labs',
      author_email='rmogilatov@gmail.com',
      license='BSD New',
      packages=['dependency_injector',
                'dependency_injector.providers'],
      install_requires=['six'],
      url='https://github.com/sirkonst/python-dependency-injector/tree/acr',
)
