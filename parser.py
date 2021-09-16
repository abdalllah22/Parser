from utils.helper import get_format_of_file
import sys


def main():
    file_format = get_format_of_file(sys.argv[1])
    try:
        if file_format == 'csv':
            pass
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    main()