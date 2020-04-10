# pann_starr_fits_helper
Download fits images from [PanSTARRS-1 server](https://ps1images.stsci.edu/cgi-bin/ps1cutouts)

## Requirements:

BeautifulSoup 4

Python 2.7 +

## Set-up:

1) If necessary [install BeautifulSoup 4](https://stackoverflow.com/a/19957214)

2) In download_fits.py update `BASE_PATH`.`BASE_PATH` specifies where the fits images will be downloaded.

3) In run_it.py update `INPUT_FILE_PATH`. `INPUT_FILE_PATH` is a text document containning the names of galaxies.

## Instructions:

1) Verify Set-up has been completed.

2) Run the file run_it.py

## Notes:

For Details about the Fits format and any potential flux scaling [Click Here](https://outerspace.stsci.edu/display/PANSTARRS/PS1+Image+Cutout+Service#PS1ImageCutoutService-ImportantFITSimageformat,WCS,andflux-scalingnotes)

For additional information about downloading fits-cutout images from PanStarr [Click Here](https://outerspace.stsci.edu/display/PANSTARRS/PS1+Image+Cutout+Service#PS1ImageCutoutService-Scriptedimagedownloadsandimagecutoutextractions)
