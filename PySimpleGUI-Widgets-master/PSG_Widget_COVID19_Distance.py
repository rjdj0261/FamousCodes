"""
  COVID-19 Distance Tracking Widget
  Display distances from your zipcode to the known cases of COVID-19 in your area
  BE SAFE EVERYONE!
  Don't panic but do protect yourself
  The data acquisition and processing portion of this code (i.e. the hard stuff) was provided
  by Isael Dryer that can be executed online - https://repl.it/@IsraelDryer/Covid-19-Distance
  Oh, also grabbed some of his Weather Widget code to create the window.
  https://github.com/israel-dryer/Weather-App

  Copyright 2020 PySimpleGUI.com
  Learn more about PySimpleGUI http://www.PySimpleGUI.org GitHub http://www.PySimpleGUI.com

  Requires geopy and PySimpleGUI... both are pip installable

  The data source is:
  2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE
  https://github.com/CSSEGISandData/COVID-19

  EDUCATE YOURSELF - Read sources that are up to date and known to be solid, ubiased outlets
  https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
"""

import pandas as pd
import geopy
from geopy.distance import distance
from geopy.geocoders import Nominatim
import PySimpleGUI as sg
import json
from os import path
from os import remove
import datetime
import webbrowser

sg.theme('Dark Red')
# sg.theme('Light Green 6')     # If you want a slightly more upbeat color theme
TXT_COLOR = sg.theme_text_color()
BG_COLOR = sg.theme_background_color()
ALPHA = 1.0
REFRESH_RATE_IN_MINUTES = 5
NUM_DATA_LINES = 5      # Lines of data to display.  First line is the header
DEFAULT_SETTINGS = {'zipcode': 'New York, NY', 'country': 'United States', 'units': 'miles'}

SETTINGS_FILE = path.join(path.dirname(__file__), r'C19-widget.cfg')

def load_settings():

    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
    except:
        sg.popup_quick_message('No settings file found... will create one for you', keep_on_top=True)
        settings = change_settings(DEFAULT_SETTINGS)
        zipcode = settings['zipcode']
        if not zipcode:
            sg.popup_error('Aborting', auto_close=True, auto_close_duration=2)
            exit(69)
        save_settings(settings)

    return settings

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)

def change_settings(settings):
    layout = [[sg.T('Zipcode OR City, State for your location')],
              [sg.I(settings.get('zipcode', ''), size=(15,1), key='-ZIP-')],
              [sg.T('Country')],
              [sg.I(settings.get('country', 'United States'), size=(15,1), key='-COUNTRY-')],
              [sg.T('Distance'),
               sg.R('Miles', 1, default=True if settings.get('units') == 'miles' else False, key='-MILES-'),
               sg.R('Kilometers', 1, default=True if settings.get('units') == 'kilometers' else False, key='-KILOMETERS-'), ],
              [sg.B('Ok', border_width=0, bind_return_key=True), sg.B('Cancel', border_width=0)],]

    event, values = sg.Window('Settings', layout, keep_on_top=True, border_depth=0).read(close=True)

    if event == 'Ok':
        settings['zipcode'] = values['-ZIP-']
        settings['country'] = values['-COUNTRY-']
        settings['units'] = 'miles' if values['-MILES-'] else 'kilometers'

    return settings


def distance_list(settings, window):
    # Setup the geolocator
    geopy.geocoders.options.default_user_agent = 'my_app/1'
    geopy.geocoders.options.default_timeout = 7
    geolocator = Nominatim()

    # Find location based on my zip code
    try:
        # location = geolocator.geocode({'postalcode' : '42420', 'country':settings['country']})      # type: geopy.location.Location
        location = geolocator.geocode(f'{settings["zipcode"]} {settings["country"]}')      # type: geopy.location.Location
        myloc = (location.latitude, location.longitude)
        window['-LOCATION-'].update(location.address)
        window['-LATLON-'].update(myloc)
    except Exception as e:
        sg.popup_error(f'Exception computing distance. Exception {e}', 'Deleting your settings file so you can restart from scratch', keep_on_top=True)
        remove(SETTINGS_FILE)
        exit(69)

    # Download Covid-19 data
    file_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
    df = pd.read_csv(file_url)

    def distance_in_miles(row):
      """ Calculate the distance between my location and the other locations in the dataset """
      rowloc = (row.Lat, row.Long)
      miles = distance(myloc, rowloc).miles
      return miles

    df['DistanceInMiles'] = df.apply(distance_in_miles, axis=1)

    return df.sort_values('DistanceInMiles').head(NUM_DATA_LINES)


def nearest(distances):
    return distances.values[0][-1]


def update_display(window, distances, settings):
    if distances is not None:
        values = distances.values[0:NUM_DATA_LINES - 1]
        out = [f'{"Location":27} {"Country":4}    {"Miles":6} {"Kilometers":8}']
        for data in values:
            out.append(f'{data[0]:30} {data[1]:4} {data[-1]:8.2f} {data[-1] * 1.61:8.2f}')
        for i, line in enumerate(out):
            window[i].update(line)
        window['-ZIP-'].update(settings['zipcode'])
        if settings.get('units') == 'kilometers':
            window['-NEAREST-'].update(f'{nearest(distances)*1.61:.2f} Kilometers')
        else:
            window['-NEAREST-'].update(f'{nearest(distances):.2f} Miles')
    window['-UPDATED-'].update('Updated: ' + datetime.datetime.now().strftime("%B %d %I:%M:%S %p"))


def create_window():
    """ Create the application window """
    PAD = (0,0)

    main_data_col = [[sg.T(size=(58,1), font='Courier 12', key=i, background_color=sg.theme_text_color(), text_color=sg.theme_background_color(), pad=(0,0))] for i in range(NUM_DATA_LINES)]

    layout = [[sg.T('COVID-19 Distance', font='Arial 35 bold', pad=PAD),
               sg.T('×', font=('Arial Black', 16), pad=((110,5),(0,0)), enable_events=True, key='-QUIT-')],
              [sg.T(size=(15,1), font='Arial 35 bold', key='-ZIP-', pad=PAD)],
              [sg.T(size=(18,1), font='Arial 30 bold', key='-NEAREST-', pad=PAD)],
              [sg.T(size=(70,2), key='-LOCATION-')],
              [sg.T(size=(40,1), key='-LATLON-')],
              [sg.Col(main_data_col, pad=(0,0))],
              [sg.T(size=(40,1), font='Arial 8', key='-UPDATED-')],
              [sg.T('Settings', key='-SETTINGS-', enable_events=True),
               sg.T('        Latest Statistics', key='-MOREINFO-',enable_events=True),
               sg.T('        Refresh', key='-REFRESH-',enable_events=True)],]

    window = sg.Window(layout=layout, title='COVID Distance Widget', margins=(0, 0), finalize=True, keep_on_top=True, no_titlebar=True, grab_anywhere=True, alpha_channel=ALPHA)

    for key in ['-SETTINGS-', '-MOREINFO-', '-REFRESH-', '-QUIT-']:
        window[key].set_cursor('hand2')

    return window


def main():
    settings = load_settings()

    window = create_window()

    distances = distance_list(settings, window)
    update_display(window, distances, settings)

    while True:
        event, values = window.read(timeout=REFRESH_RATE_IN_MINUTES * 60 * 1000)
        if event in (None, 'Exit', '-QUIT-'):
            break
        elif event == '-SETTINGS-':
            settings = change_settings(settings)
            save_settings(settings)
        elif event == '-MOREINFO-':
            webbrowser.open(r'https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')

        if settings['zipcode']:
            distances = distance_list(settings, window)
            update_display(window, distances, settings)
    window.close()

if __name__ == '__main__':
    main()