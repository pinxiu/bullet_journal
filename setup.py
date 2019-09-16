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
    download_url = 'https://github.com/pinxiu/bullet_journal/archive/v_06.tar.gz',
    keywords = ['bullet', 'journal', 'toolkit', 'cli'],
    install_requires=[
        'pycrypto',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'bullet_journal.registered_commands': [
            'add = bullet_journal.commands.add:main',
            'close = bullet_journal.commands.close:main',
            'delete = bullet_journal.commands.delete:main',
            'migrate = bullet_journal.commands.migrate:main',
            'daily_log = bullet_journal.commands.daily_log:main',
            'push = bullet_journal.commands.push:main',
            'pull = bullet_journal.commands.pull:main',
            'signup = bullet_journal.commands.signup:main',
            'login = bullet_journal.commands.login:main',
            'logout = bullet_journal.commands.logout:main',
        ],
        'console_scripts': [
            'bj = bullet_journal.__main__:main',
        ],
    },
)
