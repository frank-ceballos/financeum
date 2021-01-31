from setuptools import setup

setup(
    name='financeum',
    packages = ['financeum'],
    version='0.2.2',    
    description='A Python package retrieve historical financial data.',
    url='https://github.com/frank-ceballos/financeum',
    author='Frank Ceballos',
    author_email='frank.ceballos123@gmail.com',
    license='MIT License',
    keywords = ['PYTHON', 'STOCKS', 'FINANCE'],
    python_requires='>=3.7',
    install_requires=['pandas',
                    'pandas-datareader',
                    'yahoo-finance',
                    'yfinance',
                    'get_all_tickers'                   
                      ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9', 
        'License :: OSI Approved :: MIT License',
        ]
)