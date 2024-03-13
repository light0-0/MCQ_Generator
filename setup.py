from setuptools import find_packages,setup

setup(
    name="MCQ_GENERATOR",
    version='0.0.1',
    author='hardik bhagat',
    author_email='bhagathardik1000@gmail.com',
    install_requires=["langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)