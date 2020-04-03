from setuptools import setup, find_packages
import os
import sys

version = "1.0.0"

if sys.argv[-1] == 'publish':
    try:
        import wheel  # NOQA
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

setup(
    name="djangocms-hello-world",
    version=version,
    url='https://github.com/Zeerooth/cmsplugin-slick-gallery',
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
    license='BSD',
    description="test project for automation demonstration",
    long_description=open('README.md').read(),
    author='Radosław Stępień',
    author_email='rstepien@cloudferro.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.11",
        "django-cms >= 3.4",
    ],
    zip_safe=False,
)