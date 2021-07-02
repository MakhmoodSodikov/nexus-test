import os


def write_lines_to_file(text, filepath):
    with open(filepath, 'w') as f:
        f.writelines(text)


def get_extension(file_path):
    return os.path.splitext(file_path)[1]
