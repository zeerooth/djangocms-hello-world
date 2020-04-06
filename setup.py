from setuptools import setup, find_packages

version = "1.0.1"

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-django',
    'django',
    'django-cms'
]

setup(
    name="djangocms-hello-world",
    version=version,
    url='https://github.com/Zeerooth/djangocms-hello-world',
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
    license='BSD',
    description="test project for automation demonstration in django-cms",
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
    tests_require=TEST_REQUIREMENTS,
    zip_safe=False,
)
