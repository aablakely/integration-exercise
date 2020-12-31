from setuptools import setup

setup(
    name='integration-exercise',
    version='1.0',
    packages=[''],
    url='https://github.com/aablakely/integration-exercise',
    license='',
    author='Audrey Ann Blakely',
    author_email='audreyann.blakely@gmail.com',
    install_requires=[
        'selenium',
        'selenium.common.exceptions.WebDriverException',
        'webdriver_manager.chrome.ChromeDriverManager',
        'xml.etree.ElementTree',
        'json'
    ],
    description='XML to JSON exercise for interview'
)
