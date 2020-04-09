#import external libraries:
import os
import urllib
from os.path import exists, join

#import html_parser:
from html_parser import is_valid_url, get_all_fits_cutout_links_for_band, get_url_for_galaxy_name

#constants:
BASE_PATH = "D:\\Galaxies\\spin_parity_input_galaxies"

#helper functions:
def _check_if_folder_exists_and_if_not_make_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def _get_path_to_save_fits_file(name,band,base_path,seperate_folders=True):
    file_name = "{}_{}.fits".format(name,band)
    folder = join(base_path,name) if seperate_folders else base_path
    _check_if_folder_exists_and_if_not_make_folder(folder)
    return join(folder,file_name)

def _download_and_save_fits(url,path_to_save):
    urllib.urlretrieve(url,path_to_save)

#functions:
def download_fits_files(name,path=BASE_PATH,seperate_folders=True):
    url = get_url_for_galaxy_name(name)
    band_to_link_dict = get_all_fits_cutout_links_for_band(url)

    for each_band in band_to_link_dict:
        the_path = _get_path_to_save_fits_file(name,each_band,path,seperate_folders)
        the_link = band_to_link_dict[each_band]

        if is_valid_url(the_link):
            _download_and_save_fits(the_link,the_path)

#example:
if __name__ == "__main__":
    name = "IC1683"
    download_fits_files(name)
    
