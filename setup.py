from setuptools import setup,find_packages


setup(
    name = "cmdline-shellsploit",
    packages = find_packages(exclude=["database","Outputs","disassembly","encoders","inject","core"]),
    #package_data={'mypackage'}

    entry_points={
        'console_scripts': [
            'shellsploit = Shellsploit.shellsploit:start',
        ]
    },
    version = "0.1",
    description = "Mutation Of Viruses",
    author = "B3mB4m",
    author_email = "b3mb4m@protonmail.com",
    )