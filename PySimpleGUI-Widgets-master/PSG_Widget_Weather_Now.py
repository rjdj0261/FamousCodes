import PySimpleGUI as sg
import datetime
import base64
from urllib import request
import json
from json import load as jsonload
from json import dump as jsondump

from os import path

"""
    A Current Weather Widget
    
    Adapted from the weather widget originally created and published by Israel Dryer that you'll find here:
    https://github.com/israel-dryer/Weather-App
    
    BIG THANKS goes out for creating a good starting point for other widgets to be build from.
    
    A true "Template" is being developed that is a little more abstracted to make creating your own
    widgets easy.  Things like the settings window is being standardized, the settings file format too.
    
    You will need a key (APPID) from OpenWeathermap.org in order to run this widget. It's free, it's easy:
    https://home.openweathermap.org/
    
    Your initial location is determined using your IP address and will be used if no settings file is found
    
    This widget is an early version of a PSG Widget so it may not share the same names / constructs as the templates. 
        
    Copyright 2020 PySimpleGUI - www.PySimpleGUI.com
    
"""

# If no settings file is found, then these values will be used as the default values in the settings window
DEFAULT_SETTINGS = {'location': 'New York, NY', 'api key': 'PASTE YOUR API KEY HERE!!!'}

SETTINGS_FILE = path.join(path.dirname(__file__), r'weather-now-widget.cfg')

API_KEY = ''            # Set using the "Settings" window and saved in your config file


sg.ChangeLookAndFeel('Light Green 6')
ALPHA = 0.8

BG_COLOR = sg.theme_text_color()
TXT_COLOR = sg.theme_background_color()

APP_DATA = {
    'City': 'Pittsboro',
    'Country': 'US',
    'Postal': 27312,
    'Description': 'clear skys',
    'Temp': 101.0,
    'Feels Like': 72.0,
    'Wind': 0.0,
    'Humidity': 0,
    'Precip 1hr': 0.0,
    'Pressure': 0,
    'Updated': 'Not yet updated',
    'Icon': None,
    'Units': 'Imperial'
}


def load_settings():
    global API_KEY

    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = jsonload(f)
            API_KEY = settings['api key']
    except:
        sg.popup_quick_message('No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white', auto_close_duration=3, non_blocking=False)
        settings = change_settings(DEFAULT_SETTINGS)
        save_settings(settings)
    return settings


def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        jsondump(settings, f)


def change_settings(settings, window_location=(None, None)):
    global APP_DATA, API_KEY

    layout = [[sg.T('Enter Zipcode or City for your location')],
              [sg.I(settings.get('location', ''), size=(15,1), key='location')],
              [sg.I(settings['api key'], size=(32,1), key='api key')],
              [sg.B('Ok', border_width=0, bind_return_key=True), sg.B('Cancel', border_width=0)],]

    window = sg.Window('Settings', layout, location=window_location, no_titlebar=True, keep_on_top=True, border_depth=0)
    event, values = window.read()
    window.close()

    if event == 'Ok':
        new_city = settings['location'] = values['location']
        API_KEY = settings['api key'] = values['api key']

        if new_city is not None:
            if new_city.isnumeric() and len(new_city) == 5 and new_city is not None:
                APP_DATA['Postal'] = new_city
                APP_DATA['City'] = ''
            else:
                APP_DATA['City'] = new_city
                APP_DATA['Postal'] = ''
        save_settings(settings)

    return settings


def update_weather():
    if APP_DATA['City']:
        request_weather_data(create_endpoint(2))
    elif APP_DATA['Postal']:
        request_weather_data(create_endpoint(1))


def create_endpoint(endpoint_type=0):
    """ Create the api request endpoint
    {0: default, 1: zipcode, 2: city_name}"""
    if endpoint_type == 1:
        try:
            endpoint = f"http://api.openweathermap.org/data/2.5/weather?zip={APP_DATA['Postal']},us&appid={API_KEY}&units={APP_DATA['Units']}"
            return endpoint
        except ConnectionError:
            return
    elif endpoint_type == 2:
        try:
            endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={APP_DATA['City'].replace(' ','%20')},us&APPID={API_KEY}&units={APP_DATA['Units']}"
            return endpoint
        except ConnectionError:
            return
    else:
        return


def request_weather_data(endpoint):
    """ Send request for updated weather data """
    global APP_DATA

    if endpoint is None:
        sg.popup_error('Could not connect to api.  endpoint is None', keep_on_top=True)
        return
    else:
        try:
            response = request.urlopen(endpoint)
        except request.HTTPError:
            sg.popup_error('ERROR Obtaining Weather Data',
                           'Is your API Key set correctly?',
                           API_KEY, keep_on_top=True)
            return
    
    if response.reason == 'OK':
        weather = json.loads(response.read())
        APP_DATA['City'] = weather['name'].title()
        APP_DATA['Description'] = weather['weather'][0]['description']
        APP_DATA['Temp'] = "{:,.0f}°F".format(weather['main']['temp'])
        APP_DATA['Humidity'] = "{:,d}%".format(weather['main']['humidity'])
        APP_DATA['Pressure'] = "{:,d} hPa".format(weather['main']['pressure'])
        APP_DATA['Feels Like'] = "{:,.0f}°F".format(weather['main']['feels_like'])
        APP_DATA['Wind'] = "{:,.1f} m/h".format(weather['wind']['speed'])
        APP_DATA['Precip 1hr'] = None if not weather.get('rain') else "{:2} mm".format(weather['rain']['1h'])
        APP_DATA['Updated'] = 'Updated: ' + datetime.datetime.now().strftime("%B %d %I:%M:%S %p")
        APP_DATA['Lon'] = weather['coord']['lon']
        APP_DATA['Lat'] = weather['coord']['lat']

        icon_url = "http://openweathermap.org/img/wn/{}@2x.png".format(weather['weather'][0]['icon'])
        APP_DATA['Icon'] = base64.b64encode(request.urlopen(icon_url).read())


def metric_row(metric):
    """ Return a pair of labels for each metric """
    return [sg.Text(metric, font=('Arial', 10), pad=(15, 0), size=(9, 1)),
            sg.Text(APP_DATA[metric], font=('Arial', 10, 'bold'), pad=(0, 0), size=(9, 1), key=metric)]

def create_window():
    """ Create the application window """
    col1 = sg.Column(
        [[sg.Text(APP_DATA['City'], font=('Arial Rounded MT Bold', 18), pad=((10, 0), (50, 0)), size=(18, 1), background_color=BG_COLOR, text_color=TXT_COLOR, key='City')],
        [sg.Text(APP_DATA['Description'], font=('Arial', 12), pad=(10, 0), background_color=BG_COLOR, text_color=TXT_COLOR, key='Description')]],
            background_color=BG_COLOR, key='COL1')

    col2 = sg.Column(
        [[sg.Text('×', font=('Arial Black', 16), pad=(0, 0), justification='right', background_color=BG_COLOR, text_color=TXT_COLOR, enable_events=True, key='-QUIT-')],
        [sg.Image(data=APP_DATA['Icon'], pad=((5, 10), (0, 0)), size=(100, 100), background_color=BG_COLOR, key='Icon')]],
            element_justification='center', background_color=BG_COLOR, key='COL2')

    col3 = sg.Column(
        [[sg.Text(APP_DATA['Updated'], font=('Arial', 8), background_color=BG_COLOR, text_color=TXT_COLOR, key='Updated')]],
            pad=(10, 5), element_justification='left', background_color=BG_COLOR, key='COL3')

    col4 = sg.Column(
        [[sg.Text('click to change city', font=('Arial', 8, 'italic'), background_color=BG_COLOR, text_color=TXT_COLOR, enable_events=True, key='-CHANGE-')]],
            pad=(10, 5), element_justification='right', background_color=BG_COLOR, key='COL4')

    top_col = sg.Column([[col1, col2]], pad=(0, 0), background_color=BG_COLOR, key='TopCOL')

    bot_col = sg.Column([[col3, col4]], pad=(0, 0), background_color=BG_COLOR, key='BotCOL')

    lf_col = sg.Column(
        [[sg.Text(APP_DATA['Temp'], font=('Haettenschweiler', 90), pad=((10, 0), (0, 0)), justification='center', key='Temp')]],
            pad=(10, 0), element_justification='center', key='LfCOL')

    rt_col = sg.Column(
        [metric_row('Feels Like'), metric_row('Wind'), metric_row('Humidity'), metric_row('Precip 1hr'), metric_row('Pressure')],
            pad=((15, 0), (25, 5)), key='RtCOL')

    layout = [[top_col],
              [lf_col, rt_col],
              [bot_col]]

    window = sg.Window(layout=layout, title='Weather Widget', margins=(0, 0), finalize=True,
        element_justification='center', keep_on_top=True, no_titlebar=True, grab_anywhere=True, alpha_channel=ALPHA)

    for col in ['COL1', 'COL2', 'TopCOL', 'BotCOL', '-QUIT-']:
        window[col].expand(expand_y=True, expand_x=True)

    for col in ['COL3', 'COL4', 'LfCOL', 'RtCOL']:
        window[col].expand(expand_x=True)

    window['-CHANGE-'].set_cursor('hand2')
    window['-QUIT-'].set_cursor('hand2')

    return window


def update_metrics(window):
    """ Adjust the GUI to reflect the current weather metrics """
    metrics = ['City', 'Temp', 'Feels Like', 'Wind', 'Humidity', 'Precip 1hr',
               'Description', 'Icon', 'Pressure', 'Updated']
    for metric in metrics:
        if metric == 'Icon':
            window[metric].update(data=APP_DATA[metric])
        else:
            window[metric].update(APP_DATA[metric])


def main(refresh_rate):
    """ The main program routine """
    timeout_minutes = refresh_rate * 60 * 1000


    # Try to get the current users ip location in case no config file found
    try:
        postal = json.loads(request.urlopen('http://ipapi.co/json').read())['postal']
        DEFAULT_SETTINGS['location'] = postal
    except ConnectionError:
        pass

    # Load settings from config file. If none found will create one
    settings = load_settings()
    location = settings['location']
    if location is not None:
        if location.isnumeric() and len(location) == 5 and location is not None:
            APP_DATA['Postal'] = location
            APP_DATA['City'] = ''
        else:
            APP_DATA['City'] = location
            APP_DATA['Postal'] = ''
        update_weather()
    else:
        sg.popup_error('Having trouble with location', 'Application data:', APP_DATA)
        exit()

    window = create_window()

    while True:     # Event Loop
        event, values = window.read(timeout=timeout_minutes)
        if event in (None, '-QUIT-'):
            break
        if event == '-CHANGE-':
            x,y = window.current_location()
            settings = change_settings(settings, (x+405,y) )
        elif event != sg.TIMEOUT_KEY:
            sg.Print(event, values)

        update_weather()
        update_metrics(window)
    window.close()

if __name__ == '__main__':
    main(refresh_rate=5)