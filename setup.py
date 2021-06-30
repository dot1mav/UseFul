from setuptools import setup, find_packages


def libs() -> list:
    temp = []
    with open("requirements.txt", "r") as req_file:
        for i in req_file.readlines():
            temp.append(i.rsplit('\n')[0])
    return temp


setup(
    name='useful',
    version='0.1.2',
    author="dot1mav",
    author_email="dot1mav@gmail.com",
    url="https://github.com/dot1mav/UseFul",
    packages=find_packages(),
    include_package_data=True,
    install_requires=libs(),
)
