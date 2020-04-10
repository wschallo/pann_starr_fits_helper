#import external libraries:
import os
import urllib
from os.path import exists, join

#import html_parser:
from html_parser import is_valid_url, get_all_fits_cutout_links_for_band, get_url_for_galaxy_name

#constants:
BASE_PATH = "D:\\Galaxies\\spin_parity_input_galaxies"

#helper functions:
def _print_downloading_galaxy(galaxy_name,to_print=False):
    '''print verbose download message'''
    if to_print:
        print("downloading {} galaxy".format(galaxy_name))

def _print_galaxy_error(galaxy_name,galaxy_link):
    '''print error message'''
    print("error downloading {} galaxy, could not find fits from url: {}".format(galaxy_name,galaxy_link))

def _check_if_folder_exists_and_if_not_make_folder(folder):
    '''create folder if does not exist'''
    if not os.path.exists(folder):
        os.makedirs(folder)

def _get_path_to_save_fits_file(name,band,base_path,seperate_folders=True):
    '''get path to save file'''
    file_name = "{}_{}.fits".format(name,band)
    folder = join(base_path,name) if seperate_folders else base_path
    _check_if_folder_exists_and_if_not_make_folder(folder)
    return join(folder,file_name)

def _download_and_save_fits(url,path_to_save):
    '''download fits'''
    urllib.urlretrieve(url,path_to_save)

#functions:
def download_fits_files(name,path=BASE_PATH,seperate_folders=True,verbose=True):
    '''download fits-cutout image for galaxy with a given name, and save it'''
    url = get_url_for_galaxy_name(name)
    band_to_link_dict = get_all_fits_cutout_links_for_band(url)

    for each_band in band_to_link_dict:
        the_path = _get_path_to_save_fits_file(name,each_band,path,seperate_folders)
        the_link = band_to_link_dict[each_band]

        if is_valid_url(the_link):
            _print_downloading_galaxy(name,verbose)
            _download_and_save_fits(the_link,the_path)
        else:
            _print_galaxy_error(name,the_link)

#example: download fits images for galaxy 'IC1683'
if __name__ == "__main__":
    name = "IC1683"
    download_fits_files(name)
    
