from distutils.core import setup

import bullet_journal

setup(
    name = bullet_journal.__title__,
    packages = ['bullet_journal', 'bullet_journal.commands'],
    version = bullet_journal.__version__,
    license='MIT',
    description = 'Toolkit to make bullet journaling simple and easy',
    author = 'Pinxiu Gong',
    author_email = 'pinxiu.gong@gmail.com',
    url = 'https://github.com/pinxiu/bullet_journal',
    download_url = 'https://github.com/pinxiu/bullet_journal/archive/v_01.tar.gz',
    keywords = ['bullet', 'journal', 'toolkit', 'command line'],
    install_requires=[
        'validators',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'bullet_journal.registered_commands': [
            'add = bullet_journal.commands.add:main',
            'close = bullet_journal.commands.close:main',
            'migrate = bullet_journal.commands.migrate:main',
            'daily_log = bullet_journal.commands.daily_log:main',
        ],
        'console_scripts': [
            'bj = bullet_journal.__main__:main',
        ],
    },
)
