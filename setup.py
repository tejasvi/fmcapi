from setuptools import setup, find_packages

__version__ = "20210523.0"
__name__ = "fmcapi"
__author__ = "Dax Mickelson"
__author_email__ = "dmickels@cisco.com"
__license__ = "BSD"
__description__ = "Easier interface to Cisco's FMC API than writing your own way."
__long_description__ = """
With the removal to configure a Cisco NGFW via the command line your only option is to do so via a manager.  Some 
things are better when automated so using the manager's API gives us that power. However, the current way to write 
external scripts and interact with the FMC's API isn't that great.  We created this "wrapper" to give you an easier 
to use way of communicating with the FMC's API than using the example code provided in the API Explorer.
"""
__url__ = "https://github.com/daxm/fmcapi"
__classifiers__ = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Plugins",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Developers",
    "Intended Audience :: Other Audience",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS",
    "Operating System :: Microsoft",
    "Programming Language :: Python :: 3",
    "Topic :: Security",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking :: Firewalls",
    "Topic :: System :: Systems Administration",
    "Topic :: Utilities",
]
__keywords__ = "fmcapi fmc ftd security cisco ngfw api firepower"
__install_requires__ = [
    "requests",
    "datetime",
    "ipaddress",
]
__python_version_minimum__ = ">=3.6"
__package_data__ = {}
__data_files__ = None

setup(
    name=__name__,
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    classifiers=__classifiers__,
    keywords=__keywords__,
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=__install_requires__,
    python_requires=__python_version_minimum__,
    package_data=__package_data__,
    data_files=__data_files__,
)
