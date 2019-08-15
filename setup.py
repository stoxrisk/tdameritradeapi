import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='tdameritradeapi',
    version='0.1',
    description="A tool used to interact with TD Ameritrade's API",
    long_description="na yet",
    url='https://github.com/stoxrisk/tdameritradeapi',
    download_url='https://github.com/stoxrisk/tdameritradeapi',
    author='Andrew Chuba',
    author_email='andrew.chuba@live.com',
    license='MIT',
    keywords=['finance data', 'stocks', 'derivatives', 'cryptocurrencies', 'currencies', 'forex', 'td ameritrade'],
    packages=['tdameritradeapi'],
    install_requires=[
        "requests"
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    zip_safe=False
)
