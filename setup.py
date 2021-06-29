from setuptools import setup


def libs() -> list:
    temp = []
    with open("requirements.txt", "r") as req_file:
        for i in req_file.readlines():
            temp.append(i.rsplit('\n')[0])
    return temp


setup(
    name='useful',
    version='0.1.1',
    author="dot1mav",
    author_email="dot1mav@gmail.com",
    url="https://github.com/dot1mav/UseFul",
    packages=['UseFul'],
    include_package_data=True,
    install_requires=libs(),
)
