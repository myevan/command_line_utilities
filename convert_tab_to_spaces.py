#!/usr/bin/env python
import os
import glob
import fnmatch
import argparse


def convert_tab_to_spaces(file_path, space_count=4):
    data = open(file_path).read()
    open(file_path, 'w').write(data.replace('\t', ' ' * space_count))


if __name__ == '__main__':
    import sys

    def main():
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('file_patterns', type=str, nargs=1, help='file patterns')
        parser.add_argument('-R', '--recursive', action='store_true', help='Recursively convert subdirectories listed')

        args = parser.parse_args()
        if args.recursive:
            for base_path, dir_names, file_names in os.walk('.'):
                for file_pattern in args.file_patterns:
                    for file_name in fnmatch.filter(file_names, file_pattern):
                        file_path = os.path.join(base_path, file_name)
                        print file_path
                        convert_tab_to_spaces(file_path)
        else:
            for file_pattern in args.file_patterns:
                for file_path in glob.glob(file_pattern):
                    print file_path
                    convert_tab_to_spaces(file_path)
        return 0

    sys.exit(main())

