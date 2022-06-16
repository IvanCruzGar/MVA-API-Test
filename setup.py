from setuptools import setup, find_packages

setup(name='API_requires',
      version='1.0',
      description="Practice API testing",
      author='Jaime Perez',
      author_email='jaime.perez@aspentech.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==6.1.2",
          "pytest-html==2.1.1",
          "requests==2.25.0",
          "openpyxl==3.0.6",
          "pandas==1.2.1",
          "pymssql==2.1.5",
          "pytest-csv==2.0.2",
          "requests_ntlm==1.1.0", ]
      )
