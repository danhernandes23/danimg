from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="danimg",
    version="0.0.1",
    author="dan_hernandes",
    author_email="dangusr7@gmail.com",
    description="Este pack foi criado para fins acadêmicos aprendendo com a DIO",
    long_description="Este pack foi criado para fins acadêmicos onde foi solicitado a criação de um pacote através do Python para conclusão do projeto. Este projeto foi designado através das aulas do Bootcamp da DIO: NTTDATA com Python.",
    url="https://github.com/danhernandes23",
    packages=find_packages(),
    python_requires='>=3.8',
)