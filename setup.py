from setuptools import setup, find_packages

setup(
    name="sales_chatbot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
        "pandas",
        "matplotlib",
    ],
)
