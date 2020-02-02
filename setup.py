from distutils.core import setup


setup(
    name='cliks',
    packages=['cliks'], 
    version='0.1.0',
    description='CLI para facilitar e padronizar rotinas básicas de git.',
    author='Carlos Neto',
    author_email='carlos.santos110@fatec.sp.gov.br',
    license='MIT',
    url='https://github.com/augustoliks/cliks',
    keywords=['cli', 'git', 'example'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'supervisord = supervisor.supervisord:main'
        ]
    }
)
