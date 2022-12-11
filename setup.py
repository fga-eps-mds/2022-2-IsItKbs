from setuptools import setup

with open("description.md", "r") as arq:
    long_description = arq.read()

setup(name='isitkbs',
    version='0.0.1',
    license='MIT License',
    author='Arthur de Melo, Arthur Grandão, Douglas Alves, Gabriel Campello, Paulo Victor, Rafael Ferreira, Sidney Fernando',
    long_description=long_description,
    long_description_content_type="text/markdown",
    #author_email='',
    keywords='keyboard-smashing',
    description=u'Detect keyboard smashing',
    include_package_data=True,
    packages=['isitkbs', 'models'],
    install_requires=['scikit-learn', 'nltk'],)