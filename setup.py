from setuptools import setup

setup(
    name="tests_discoverer",
    version="0.1",
    packages=['tests_discoverer'],
    install_requires=["click==7.1.2"],
    entry_points="""
        [console_scripts]
        tdisc=tests_discoverer.tdisc:cli
    """,
)
