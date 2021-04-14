import webbrowser
from nasaapi import Client

nasa = Client('N0ds7kCUd7H81aaP4MinEl1DGTrP4We9jtLtAFfh')  # Uses API Key


def apod():  # Gives the description of the picture of the day and opens it on a browser
    try:
        apod_dict = nasa.apod()
        apod_desc = apod_dict['copyright'] + apod_dict['explanation']
        webbrowser.open(apod_dict['url'])
        return apod_desc
    except:
        apod_desc = 'Could not retrieve the Picture of the Day'
        return apod_desc
