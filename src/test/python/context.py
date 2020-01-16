# test helper context, to be required by each test file
from os import path, environ
import sys

import_paths = [
    path.abspath(
        path.join(
            path.dirname(__file__), '..', '..', 'src', 'main', 'python'))
]

[sys.path.insert(0, import_path) for import_path in import_paths]
