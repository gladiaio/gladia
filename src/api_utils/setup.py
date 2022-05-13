from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="gladia-api-utils",
    version="0.1.11",
    description="Utils for Gladia APIs Framework",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    author="Jean-Louis Queguiner",
    author_email="jlqueguiner@gladia.io",
    keywords="ai api fastapi artificial_intelligence gladia",
    license="MIT",
    packages=["gladia_api_utils"],
    install_requires=[
        "PyYAML",
        "requests",
        "scikit-image",
        "Pillow",
        "numpy",
        "uuid",
        "xtract",
        "gdown",
        "python-magic",
        "icecream",
        "huggingface_hub",
        "transformers",
        "GitPython",
        "pandas",
        "lxml",
        "fastapi-utils",
        "googledrivedownloader",
        "opencv-python",
        "python-forge",
        "inflect",
        "python-multipart"
    ],
    include_package_data=True,
    zip_safe=False,
)

# need sudo apt-get install git-lfs or brew install git-lfs
