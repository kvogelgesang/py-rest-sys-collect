#!/usr/bin/env python3
# pip install unittest-xml-reporting
# pip install coverage
# sudo pip install flake8
# pip install --upgrade --pre pybuilder
# sudo pyb install_dependencies publish
# See also as example : https://github.com/yadt/shtub/blob/master/build.py
# sudo apt-get install python-setuptools python-all debhelper dpkg-dev
# sudo -H pip install stdeb
# https://github.com/antevens/listen/blob/master/build.py

from pybuilder.core import Author, init, use_plugin, task
import os, sys
from subprocess import Popen, PIPE, STDOUT, call, check_output


ria_info_main_rel_version = "1"
name = "restsyscollector"
summary = "REST SYSTEM COLLECTOR"
description = "Rest System Collector for collection and offer system metrics"
authors = [Author("Kay Vogelgesang", "kay.vogelgesang@apachefriends.org")]
url = "http://www.onlinetech.de"
license = "GPL"


def getversion():
    try:
        bugfix_version = os.environ['BUILD_NUMBER']
        info_cli_version = ria_info_main_rel_version + ".0." + str(bugfix_version)
    except:
        info_cli_version = ria_info_main_rel_version + ".0.0"
    return info_cli_version


@task
def upload_to_pypi_server():
    pypi_server = "testserver01"
    twine = "twine"
    artifact = "target/dist/" + name + "-" + getversion() + "/dist/" + name + "-" + getversion()
    cur_version = sys.version_info
    python_short_version = str(cur_version[0]) + "." + str(cur_version[1])
    print("[INFO]  Use Python in version " + python_short_version + "for building artifacts")
    try:
        os.environ['BUILD_NUMBER']
        jenkins_workspace = os.environ['WORKSPACE']
        artifact = jenkins_workspace + "/" + artifact
        #twine = jenkins_workspace + "/venv/bin/" + twine
    except:
        print("[INFO]  Not a Jenkins build - do not upload artifacts to pypi-server " + pypi_server)
        return
    try:
        result = check_output(twine + " --version", stderr=STDOUT, shell=True)
        result = result.decode("utf-8")
        print("[INFO] Find twine as -> " + str(result))
        egg_artifact = artifact + "-py" + python_short_version + ".egg"
        tar_artifact = artifact + ".tar.gz"
        if not os.path.isfile(egg_artifact):
            print("[WARN]  Cannot find " + egg_artifact  + " to upload")
        else:
            try:
                egg_artifact = artifact + "-py" + python_short_version + ".egg"
                print("[INFO]  Start upload " + egg_artifact + " with twine to ->  " + pypi_server)
                twine_command = twine + " upload -r " + pypi_server + " " + egg_artifact
                print("[INFO]  Start -> " + twine_command)
                result = check_output(twine_command, stderr=STDOUT, shell=True)
                print(str(result))
            except Exception as e:
                print("[ERROR]  Cannot upload " + egg_artifact + " to pypi server " + pypi_server + "\n" + str(e))
                sys.exit(1)
        if not os.path.isfile(tar_artifact):
            print("[WARN]  Cannot find " + tar_artifact + ".to upload")
        else:
            try:
                print("[INFO]  Start upload " + tar_artifact + " with twine to ->  " + pypi_server)
                twine_command = twine + " upload -r " + pypi_server + " " + tar_artifact
                print("[INFO]  Start -> " + twine_command)
                result = check_output(twine_command, stderr=STDOUT, shell=True)
                print(str(result))
            except Exception as e:
                print("[ERROR]  Cannot upload " + tar_artifact + " to pypi server " + pypi_server + "\n" + str(e))
                sys.exit(1)
    except Exception as e:
        print("[ERROR]  Cannot find/execute twine -> " + twine + "\n" + str(e) + "\nPerhaps ~/.pypirc not exists?")
        sys.exit(1)


use_plugin("filter_resources")
use_plugin("python.core")
use_plugin("python.unittest")
#use_plugin("python.pyfix_unittest")
use_plugin("python.install_dependencies")
use_plugin("python.pydev")
use_plugin("python.distutils")
use_plugin("copy_resources")
#use_plugin("source_distribution")
#use_plugin("python.flake8")
use_plugin("python.coverage")
#use_plugin('python.integrationtest')
#use_plugin("python.stdeb")
version = getversion()


# default_task = ["analyze", "publish", "package", "make_deb"]
default_task = ["analyze", "publish", "package"]


@init
def initialize(project):
    project.build_depends_on('setuptools')
    project.build_depends_on('unittest-xml-reporting')
    project.build_depends_on('coverage')
    project.build_depends_on('flake8')
    project.build_depends_on('mock')
    project.build_depends_on('unittest2')
    project.build_depends_on('Flask')
    project.depends_on('argparse')
    project.depends_on('Flask')
    project.set_property("coverage_threshold_warn", 85)
    project.set_property("coverage_break_build", False)
    #project.set_property("coverage_reset_modules", True)
    #project.set_property('coverage_threshold_warn', 50)
    #project.set_property('coverage_branch_threshold_warn', 50)
    #project.set_property('coverage_branch_partial_threshold_warn', 50)
    project.set_property("dir_dist_scripts", 'scripts')
    project.set_property("copy_resources_target", "$dir_dist")
    project.set_property('verbose', True)
    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_include_test_sources', True)
    project.set_property('flake8_ignore', 'E501,E402,E731')
    project.set_property('flake8_break_build', False)
    project.set_property('deb_package_maintainer', 'Kay Vogelgesang <kay.vogelgesang@apachefriends.org>')
    project.set_property('teamcity_output', False)
    project.set_property("integrationtest_inherit_environment", True)
    #project.get_property('filter_resources_glob', ['**/riainfocli/__init__.py'])
    #project.include_file("riainfocli", "*.py")
    #project.set_property('filter_resources_glob', ['**/zabbix_json_client.py'])
    # project.depends_on('simplejson')
    # project.get_property('copy_resources_glob').append('setup.cfg')

    project.set_property("distutils_classifiers", [
                         'Programming Language :: Python',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.3',
                         'Programming Language :: Python :: 3.4',
                         'Development Status :: 2',
                         'Environment :: Console',
                         'Intended Audience :: Systems Administration',
                         'License :: OSI Approved :: GPL',
                         'Topic :: Software Development :: REST SYSTEM COLLECTOR'])

    project.set_property('distutils_commands', ['bdist'])
    project.set_property('distutils_commands', ['sdist'])
    project.get_property('distutils_commands').append('bdist_egg')



