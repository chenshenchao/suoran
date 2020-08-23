import setuptools

def load_content(path):
    with open(path, 'r', encoding='utf-8') as reader:
        return reader.read()

setuptools.setup(
    name='suoran',
    version='0.0.1',
    description='extends sanic',
    long_description=load_content('readme.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/chenshenchao/suoran',
    keywords='sanic suoran',
    license='MIT',
    author='chenshenchao',
    author_email='chenshenchao@outlook.com',
    platforms='any',
    classifiers= [
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=setuptools.find_packages(
        exclude=['test']
    )
)