from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()


setup(
    name="yente",
    version="3.7.3",
    url="https://opensanctions.org/docs/api/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="OpenSanctions",
    author_email="info@opensanctions.org",
    packages=find_packages(exclude=["examples", "tests"]),
    namespace_packages=[],
    install_requires=[
        "followthemoney==3.5.4",
        "nomenklatura==3.7.0",
        "asyncstdlib==3.10.9",
        "aiocron==1.8",
        "aiocsv==1.2.4",
        "aiofiles==23.2.1",
        "types-aiofiles>=23.1.0.4,<23.3",
        "aiohttp[speedups]==3.8.6",
        "elasticsearch[async]==8.10.1",
        "fastapi==0.104.0",
        "uvicorn[standard]==0.23.2",
        "python-multipart==0.0.6",
        "email-validator==2.0.0.post1",
        "structlog==23.2.0",
        "pyicu==2.12",
        "jellyfish==1.0.1",
        "orjson==3.9.10",
        "text-unidecode==1.3",
        "click==8.1.6",
        "normality==2.5.0",
        "languagecodes==1.1.1",
        "countrynames==1.15.3",
        "fingerprints==1.2.3",
        "pantomime==0.6.1",
    ],
    extras_require={
        "dev": [
            "pip>=10.0.0",
            "bump2version",
            "wheel>=0.29.0",
            "twine",
            "mypy",
            "httpx",
            "pytest",
            "pytest-cov",
            "pytest-asyncio",
            "flake8>=2.6.0",
            "black",
        ],
    },
    entry_points={
        "console_scripts": [
            "yente = yente.cli:cli",
        ],
    },
    zip_safe=False,
)
