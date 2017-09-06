from setuptools import setup, find_packages

setup(
    name='statcounter',
    version='0.1',
    packages=find_packages(),
    url='',
    license='BSD',
    author='hunting',
    author_email='VicHunting@yandex.ua',
    description='Statcounter API client',
    install_requires=[
            'requests',
          ],
)
