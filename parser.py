import sys

from utils.xml_parser import XMLParser
from utils.csv_parser import CSVParser 
from utils.helper import ( get_format_of_file, get_first_file_name,
                            get_second_file_name, select_all_files,
                            select_all_CSV_files, match_csv_files )



def main():
    file_format = get_format_of_file(sys.argv[1])
    try:
        if file_format == 'xml':
            files = select_all_files()
            if get_first_file_name(sys.argv[2]) in files:
                XMLParser(sys.argv[2])
            else:
                print('File does not exis')
        
        elif file_format == 'csv':
            files = select_all_CSV_files()
            if get_first_file_name(sys.argv[2]) and get_second_file_name(sys.argv[3]) in files:
                if match_csv_files(sys.argv[2],sys.argv[3]) is None:
                    CSVParser(sys.argv[2], sys.argv[3])
                else:
                    print(match_csv_files(sys.argv[2],sys.argv[3]))
            else:
                print('File does not exis')
        
        else:
            print('Not Implemented yet')
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    main()