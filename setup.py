from setuptools import setup

with open("description.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(name='isitkbs',
    version='0.0.7.9',
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