from setuptools import setup, find_packages

setup(
    name="storage",       # Choose a unique name
    version="0.1.0",                # Initial version
    description="library for for storing data inside telegram and using telegram as a database.",
    author="Pourya Samimi",
    author_email="itpourya@yahoo.com",
    url="https://github.com/itpourya/telegram-storage",  # Optional, link to the project
    packages=find_packages(),       # Automatically finds all packages in your folder
    install_requires=[              # List of dependencies
        "requests",                 # Example dependency
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
