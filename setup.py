from setuptools import find_packages, setup  # type: ignore


def readme():
    with open('./README.md', encoding='utf-8') as f:
        content = f.read()
    return content


setup(
    name='pre_commit_hooks',
    version='0.0.1',
    description='A pre-commit hook for OpenTAI projects',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/OpenTAI/pre-commit-hooks',
    author='OpenTAI Team',
    author_email='',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['PyYAML'],
    entry_points={
        'console_scripts': [
            'say-hello=pre_commit_hooks.say_hello:main',
            'check-copyright=pre_commit_hooks.check_copyright:main',
        ],
    },
)