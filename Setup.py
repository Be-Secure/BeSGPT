import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "dependencies.txt")) as dependencyfile:
  projdependencies = dependencyfile.read().strip().split("\n");

setup(
  name="BesGPT",
  version="0.0.1",
  description="GPT based tool for Open Source Security Speacilists",
  long_description="""
  BeSGPT is focused on security assessment tool empowered by AI model.
  It helps security assessment specialists via interactive session. It
  guide the specialist to perform steps and setup environment to assess
  the Open Source Software.
  """,
  author="Anil Singla",
  author_email="anilsingla111@gmail.com",
  url="https://github.com/Be-Secure/BeSGPT",
  project_urls="",
  license="MIT License",
  packages=["BeSGPT"] + find_packages(),
  install_requires=projdependencies,
  entry_points={
    "console_scripts": [
      "BeSGPT=src.main:main,
      "BeSGPT-Cookie=src.cookie:main,
      "BeSGPT-Connection=src.connection:main,
    ]
  },
)
