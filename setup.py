#!/usr/bin/env python

#  Copyright (c) 2010 Franz Allan Valencia See
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""Setup script for Robot's DatabaseLibrary distributions"""

import sys
from os.path import abspath, dirname, join
sys.path.append(join(dirname(__file__), 'src'))

from ez_setup import use_setuptools
from setuptools import setup

use_setuptools()
version_file = join(dirname(__file__), 'src', 'DatabaseLibrary', 'VERSION.py')
exec(compile(open(version_file).read(), version_file, 'exec'))

def main():
    setup(name         = 'robotframework-databaseslibrary',
          version      = VERSION,
          description  = 'Database utility library for Robot Framework',
          author       = 'qitaos',
          author_email = 'qitaos@gmail.com',
          url          = 'https://github.com/qitaos/Robotframework-Database-Library/',
          package_dir  = { '' : 'src'},
          packages     = ['DatabaseLibrary'],
          package_data={'DatabaseLibrary': ['VERSION']},
          requires     = ['robotframework']
          )
        

if __name__ == "__main__":
    main()
