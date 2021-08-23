from setuptools import setup


libs = []
with open("requirements.txt", "r") as req_file:
    for i in req_file.readlines():
        libs.append(i.rsplit("\n")[0])

setup(
    name="useful",
    version="0.2.0",
    author="dot1mav",
    author_email="dot1mav@gmail.com",
    url="https://github.com/dot1mav/UseFul",
    packages=["UseFul"],
    include_package_data=True,
    install_requires=libs,
)
