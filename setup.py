from setuptools import setup, find_packages
from pathlib import Path

# Requirements
try:
  this_directory = Path(__file__).absolute().parent
  with open((this_directory / "requirements.txt"), encoding = "utf-8") as f:
    requirements = f.readlines()
  requirements = [line.strip() for line in requirements]
except FileNotFoundError:
  requirements = []

# Metadata
setup(
  name = "brunopy123",
  version = "0.0.0.9000",
  author = "bruno meni",
  author_email = "no no no",
  description = "Toy package for learning how to publish a package.",
  license = "Apache 2.0",
  packages = find_packages(),
  install_requires = requirements
)