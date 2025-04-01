from setuptools import setup, find_packages

setup(
    name="chatgpt-4o",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python wrapper for the ChatGPT 4o API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/chatgpt-4o-unofficial-api",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
