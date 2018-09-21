from setuptools import setup

install_requires = [
    'numpy',
    'scipy',
]

setup(
    name='test-scipy-dependency',
    version='0.1.0',
    description='Testing the installation of a library with a scipy dependency',
    author='Peter Kerpedjiev',
    author_email='pkerpedjiev@gmail.com',
    url='',
    install_requires=install_requires,
    setup_requires=['numpy'],
    packages=['blah']
)
