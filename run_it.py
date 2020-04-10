#import download_fits:
from download_fits import download_fits_files

#constants:
INPUT_FILE_PATH = "D:\\Galaxies\\spin_parity_input_galaxies\\spin_parity_input_galaxies.txt"

#helper functions:
def _should_ignore_line(the_line):
    '''ignore empty lines or lines that start with # (comment)'''
    return len(the_line.strip()) == 0 or the_line.strip()[0] == '#'

def _get_name_from_line(the_line):
    '''get name from line'''
    #NOTE: does not support galaxies with a space in name
    to_parse = the_line.strip()
    if " " in to_parse:
        return to_parse.split(" ")[0]
    else:
        return to_parse

#functions:
def read_galaxy_names_from_text_file(file_path):
    '''read galaxy names from input file'''
    galaxy_names = []
    
    with open(file_path) as f:
        for each_line in f.readlines():
            if not _should_ignore_line(each_line):
                galaxy_names.append(_get_name_from_line(each_line))
    return galaxy_names

def download_list_of_galaxies(list_of_galaxy_names,verbose=True):
    '''download fits images for all galaxies in the list'''
    for each_galaxy in list_of_galaxy_names:
        download_fits_files(each_galaxy,verbose=verbose)
                                    

#example: get galaxy names from file INPUT_FILE_PATH, and dowload all fits images to BASE_PATH (see: download_fits.py)
if __name__ == "__main__":
    galaxy_names = read_galaxy_names_from_text_file(INPUT_FILE_PATH)
    download_list_of_galaxies(galaxy_names)
