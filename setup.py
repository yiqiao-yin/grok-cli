from setuptools import setup, find_packages

with open('readme.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='grok-cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'composio_core',
        'composio_langchain',
        'langchain',
        'langchain_openai',
        'langchain_community',
    ],
    entry_points={
        'console_scripts': [
            'grok_cli = grok_cli.cli:main',
        ],
    },
    author='Yiqiao Yin',
    description='A CLI tool for interacting with xAI Grok 4',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
