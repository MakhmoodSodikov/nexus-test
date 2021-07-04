import os
from logging import getLogger

logger = getLogger('main logger')


def write_lines_to_file(text: list, filepath: str) -> int:
    """
    :param text: Text to be written to the file
    :param filepath: Path to the file
    :return: 1 if Done correctly, -1 otherwise
    """
    try:
        with open(filepath, 'w') as f:
            f.writelines(text)
            return 1
    except FileExistsError as e:
        logger.error("File doesn't exist!")
        return -1
    except EOFError as e:
        logger.error("File EOF error!")
        return -1
    except Exception as e:
        logger.error(e)
        return -1


def get_extension(file_path: str) -> str:
    """
    :param file_path: Path to the file
    :return: Extension of input file
    """
    return os.path.splitext(file_path)[1]
