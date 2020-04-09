#import external libraries:
import requests
from bs4 import BeautifulSoup

#constants:
BASE_URL = "https://ps1images.stsci.edu/cgi-bin/ps1cutouts?pos={}"
BANDS = ['g','r','i','z','y']
FITS_CUTOUT_LABEL = 'FITS-cutout'

#helper functions:
def _current_band_from_td_element(td_element):
    '''get waveband from image title'''
    current_band = ""
    for each_element in td_element:
        parsed_name = str(each_element).strip().split(" ")[-1]
        if parsed_name in BANDS:
            return parsed_name
    return ""

def _is_fits_cutout(link):
    '''check if link is to FITS-cutout image'''
    return str(link.string) == FITS_CUTOUT_LABEL

#functions:
def is_valid_url(url):
    '''check if url is valid'''
    request = requests.get(url)
    return request.status_code == 200

def get_url_for_galaxy_name(name):
    '''get url for galaxy name'''
    return BASE_URL.format(name)

def get_all_fits_cutout_links_for_band(url):
    '''return a dict that maps waveband to url to download fits image'''
    #A) initalize dict:
    wave_band_to_link_dict = {}

    #B) try getting links to fits images:
    try:
        
        #B.1) Check if url is valid:
        if is_valid_url(url):
            
            #B.2) Fetch html of website and parse:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            
            #B.3) Find images:
            for td in soup.findAll("th"):
                current_band = _current_band_from_td_element(td)
                
                #B.4) Get downloadable links to images (fits-cutout)
                for link in td.find_all('a', href=True):
                    
                    #B.5) Check if valid waveband and link is correct type:
                    if _is_fits_cutout(link) and current_band in BANDS:

                        #B.6) add to dict if valid:
                        wave_band_to_link_dict.update({current_band:link['href']})
        else:
            print("invalid url: {}".format(url))
    except Exception as e:
        print("error in function get_all_fits_cutout_links_for_band: {}".format(e))

    #C) Return dict containning map from waveband to links:  
    return wave_band_to_link_dict

#example: print all fits-cutout URL's for galaxy 'IC1683'
if __name__ == "__main__":
    URL = get_url_for_galaxy_name("IC1683")
    print(get_all_fits_cutout_links_for_band(URL))
