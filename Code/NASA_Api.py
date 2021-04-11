import webbrowser
from nasaapi import Client
nasa = Client('N0ds7kCUd7H81aaP4MinEl1DGTrP4We9jtLtAFfh')

def apod():
    try:
        apod_dict = nasa.apod()
        str = apod_dict['copyright'] + apod_dict['explanation']
        webbrowser.open(apod_dict['url'])
        return str
    except:
        str = 'Could not retrieve Picture of the Day'
        return str
