#!/usr/bin/env python
"""Unbackslash.

Instead of creating the expected directory structure, `unzip(1)` baked the
entire path into the file names. I think this was because the source contained
backslash and forward-slash separated paths. So I wrote this script to find 
files with backslashes in their names, replace them for slashes and create the 
missing dir tree.

I only used this once so use with extreme caution, at your own risk, and make
a backup first.
"""
from __future__ import print_function

import argparse
import glob
import os

def unbackslash(path):
    candidates = glob.glob(path + '/*\\*')
    candidate_dirs = glob.glob(path + '/*\\')
    candidates.sort()
    candidate_dirs.sort()
    candidate_files = [c for c in candidates if c not in candidate_dirs]

    print('Performing pre-check.')

    placeholder_to_dir = lambda s: s.replace('\\', '/')[:-1]

    for d in candidate_dirs:
        assert os.path.getsize(d) == 0, 'Aborted: dir placeholder "{0}" contains data'.format(d)

        actual_dir = placeholder_to_dir(d)
        if os.path.exists(actual_dir):
            assert os.path.isdir(actual_dir), 'Aborted: new dir "{0}" is an existing file'.format(actual_dir)

        assert d[:-1] not in candidate_files, 'Aborted: "{0}" would be a file and a dir'.format(d)

    print('Actually making changes. Hope you made a backup!')
    
    for d in candidate_dirs:
        new_dir = placeholder_to_dir(d)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            os.utime(new_dir, (os.path.getatime(d), os.path.getmtime(d)))
        os.remove(d)

    for f in candidate_files:
        os.renames(f, f.replace('\\', '/'))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--path', default='.')
    args = parser.parse_args()
    unbackslash(args.path)

if __name__=='__main__':
    main()

