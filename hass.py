import config # mengambil konfigurasi
import requests # library python untuk melakukan http request

def call(intent) :
    url = config.hass_host + '/api/events/' + intent # membuat url
    headers = {
        'Authorization': 'Bearer ' + config.hass_key, # memasuian api_key ke header
        'content-type': 'application/json',
    }

    response = requests.post(url, headers=headers)
    return(response.json()['message']) # mengirim nilai balikan berupa response dari hass.io