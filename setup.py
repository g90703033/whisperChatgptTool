from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1.0',
    description='A brief description of my project',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='sample setuptools development',
    install_requires=[
        'gradio',
        'pychatgpt',
        'whisper',
        'requests',
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'my-command=my_package.cli:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/your_username/my_project/issues',
        'Source': 'https://github.com/your_username/my_project',
    },
)