from setuptools import setup

setup(
    name='financeum',
    version='0.1.0',    
    description='A Python package retrieve historical financial data.',
    url='https://github.com/frank-ceballos/financeum',
    author='Frank Ceballos',
    author_email='frank.ceballos123@gmail.com',
    license='MIT License',
    install_requires=['pandas',
                    'pandas-datareader',
                    'yahoo-finance',
                    'yfinance',
                    'get_all_tickers'                   
                      ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        ]
)