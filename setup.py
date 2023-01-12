import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='create_bag_of_words',
    version='0.0.1',
    author='Pranav Amlekar',
    author_email='pranavamlekar@gmail.com',
    description='Installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pranava777/create_bag_of_words.git',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    # },
    license='MIT',
    packages=['create_bag_of_words'],
    install_requires=['more-itertools'],
)