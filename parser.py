import sys

from utils.xml_parser import XMLParser
from utils.csv_parser import CSVParser 
from utils.helper import Helpers



def main():
    
    helpers = Helpers()
    xml_parser = XMLParser()
    csv_parser = CSVParser()
    
    if(len(sys.argv) < 2):
        print('Enter Arguments correctly !!')
        return
    
    file_format = helpers.get_format_of_file(sys.argv[1])
    try:
        if file_format == 'xml':
            files = helpers.select_all_xml_files()
            
            if helpers.get_file_name(sys.argv[2]) in files:
                xml_parser.get_data_from_xml(sys.argv[2])
            else:
                print('File does not exis')
        
        elif file_format == 'csv':
            files = helpers.select_all_CSV_files()
            
            if helpers.get_file_name(sys.argv[2]) and helpers.get_file_name(sys.argv[3]) in files:
                if helpers.match_csv_files(sys.argv[2],sys.argv[3]) is None:
                    csv_parser.get_data_from_csv(sys.argv[2], sys.argv[3])
                else:
                    print(helpers.match_csv_files(sys.argv[2],sys.argv[3]))
            else:
                print('File does not exis')
        
        else:
            print('Not Implemented yet')
    
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    main()