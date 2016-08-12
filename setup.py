#!/usr/bin/env python3

from setuptools import setup
from setuptools.command.install import install as _install
import os


class install(_install):

    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()
        _install.run(self)
        self.post_install_script()


INFO_CLI_MAIN_REL_VERSION = "1"
def getversion():
    try:
        bugfix_version = os.environ['BUILD_NUMBER']
        info_cli_version = INFO_CLI_MAIN_REL_VERSION + ".0." + str(bugfix_version)
    except:
        info_cli_version = INFO_CLI_MAIN_REL_VERSION + ".0.0"
    return info_cli_version


if __name__ == '__main__':
    setup(
        name='restsyscollector',
        version=getversion(),
        description='''REST SYSTEM COLLECTOR''',
        long_description='''Rest System Collector for collection and offer system metrics''',
        author="Kay Vogelgesang",
        author_email="kay.vogelgesang@apachefriends.org",
        license='GPL',
        url='http://www.onlinetech.de',
        platforms=['linux-x86_64'],
        data_files=[('/usr/bin', ['src/main/resources/bash/*'])],
        scripts=['src/main/scripts/ria_info_cli', 'src/main/scripts/ria_info_httpd', 'src/main/scripts/ria-info.sh', 'src/main/scripts/ria-info-httpd.sh', 'src/main/scripts/ria-info'],
        package_dir={'': 'src/main/python'},
        packages=['restsyscollector'],
        py_modules=[
            '__init__.py',
            'restsyscollector_service_class.py',
            'ria_info_xml_class.py',
            'ria_remote_class.py',
            'ria_utils_class.py',
            'ria_postgres_class.py',
            'zis_api_class.py'
        ],
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Development Status :: 2',
            'Environment :: Console',
            'Intended Audience :: Systems Administration',
            'License :: OSI Approved :: GPL',
            'Topic :: Software Development :: REST SYSTEM COLLECTOR'
        ],
        entry_points={},
        package_data={},
        install_requires=['argparse', 'Flask'],
        dependency_links=[],
        zip_safe=True,
        cmdclass={'install': install},
    )

