from setuptools import setup,find_packages


setup(
    name = "cmdline-shellsploit",
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            'shellsploit = shell.shellsploit:main',
        ]
    },
    version = "0.1",
    description = ("An open source cuztomize shellcode,backdoor,injector generator."),
    author = "B3mB4m",
    author_email = "b3mb4m@protonmail.com",
    url='https://github.com/b3mb4m/Shellsploit',
    )
