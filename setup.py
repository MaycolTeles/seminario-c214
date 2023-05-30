from setuptools import find_packages, setup


with open('README.md') as file:
    readme = file.read()


setup(
    name='calculator',
    version='0.0.1',
    packages=find_packages(where='app'),
    description='A calculator package',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Maycol',
    author_email='maycolteles@hotmail.com',
    license='GNU',
    install_requires=[],
    extras_require={
        'dev': ['pytest >= 7.3.1', 'pytest-cov >= 4.1.0', 'flake8 >= 3.8.4', 'twine >= 4.0.2'],
    },
    python_requires='>=3.9',
)
