
"""

Download a group of jpeg files from Biodiversity Heritage Library (BHL). Download the highest resolution
versions available. The user is prompted for the name of a file containing a list of BHL page ids, one page id per line.
Output filenames are optional. If supplied, the output filename follows the page id, separated by a comma.
Code is written in Python 3.

"""

import urllib.request


def get_input_file():
    """
    Prompt the user for the name of an input file containing BHL pageids and optionally output filenames.
    If output filenames are not supplied, output files are named <BHL page id>.jpg
    """

    while True:  # Loop until a valid filename is entered or the user types 'exit'
        infile = input('Enter filename of input file or exit: ')

        if infile == 'exit':
            exit()
        try:
            inhand = open(infile)
            break
        except:
            print('The file could not be opened. Please try again.')

    return inhand



def getimage(pageid,outfn):
    """
    Use the pageid to build the URL for a high-resolution image within Biodiversity Heritage Library (BHL). Use the second parameter,
    outfn, as the filename for a file on the local system.
    :param pageid:
    :param outfn:
    :return:
    """
    base_URL = 'https://biodiversitylibrary.org/pageimage/'
    current_URL = base_URL+pageid
    print(current_URL)  # Keep user informed of progress by printing the image URL
    img = urllib.request.urlopen(current_URL).read()  # Read the image into memory
    print(outfn)
    fhand = open(outfn, 'wb')
    fhand.write(img)  # Write image to a file on the local system.
    fhand.close()
    return

def main():

    input_hand = get_input_file()  # Get filename of file containing page ids and open it.


    for row in input_hand:  # Process every row in the input file. Each row identifies an image to download.

        cells = row.split(',')  # First cell contains the page id. The second cell, if present, gives the output filename.
        if len(cells) == 1:  # Output filename specified?
            ofn = cells[0].strip()+'.jpg'  #  No, use page id for output filename.
            print('output: '+ofn)
        else:
            ofn = cells[1].strip()  # Yes, use user-specified output filename.
        getimage(cells[0],ofn)  # Call code that pulls and saves images
    input_hand.close()

if __name__ == "__main__":
    main()



