import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

__version__ = '0.0.0'
Author = 'Sam1brahim '
REPO_NAME = 'https://github.com/f{Author}/Text-Summarizer'
SRC_REPO = 'textSummarizer'
Author_EMAIL = 'samirferroum@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author,
    description='Small python package for Text summaries',
    url=REPO_NAME,
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
    )