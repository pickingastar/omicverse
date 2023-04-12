r"""
Shim setup.py
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from setuptools import setup, find_packages  

setup(  
    name = 'Pyomic',  
    version = '1.2.7',
    # keywords = ('chinesename',),  
    description = 'A python framework library for omics analysis',  
    license = 'GNU License',  
    install_requires = ['pybind11','hnswlib','ERgene','numpy','scanpy','pandas==1.5.3','matplotlib','scikit-learn','scipy','networkx','multiprocess',
                        'seaborn','datetime','statsmodels','gseapy==0.10.8','ipywidgets','lifelines','ktplotspy','python-dotplot',
                        'boltons','ctxcore','termcolor','pygam','pillow','gdown','igraph','leidenalg','s_gd2','graphtools','datashader',
                        'phate','wget','deep-forest'],  
    packages = find_packages(),  # 要打包的项目文件夹
    include_package_data=True,   # 自动打包文件夹内所有数据
    author = 'ZehuaZeng',  
    author_email = 'Starlitnightly@163.com',
    url = 'https://github.com/Starlitnightly/Pyomic',
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    python_requires='>=3.8',
    py_modules=['bulk','single','bulk2single','utils'],
    # packages = find_packages(include=("*"),),  
)
