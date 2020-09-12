import codecs
import os.path
import pickle
import requests
import time
import json

from django.core.exceptions import ValidationError


def populate_series_item(series_obj):
    try:
        info = api_get_info(series_obj)
    except Exception as e:
        raise ValidationError(repr(e))

    series_obj.title = info['title']['romaji']
    series_obj.title_eng = info['title']['english'] if (info['title']['english'] is not None) else ''
    series_obj.api_id = int(info['id'])
    series_obj.series_type = info['type']

    series_obj.synopsis = info['description']
    series_obj.cover_link = info['coverImage']['large']
    series_obj.ani_link = 'https://anilist.co/{0!s}/{1!s}'.format(str(series_obj.series_type), str(series_obj.api_id))
    if info['idMal'] is not None:
        series_obj.mal_link = 'https://myanimelist.net/{0!s}/{1!s}'.format(str(series_obj.series_type).lower(),
                                                                           str(info['idMal']))


def api_get_info(series_obj):
    query = '''
    query ($id: Int) { # Define which variables will be used in the query (id)
      Media (id: $id) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        idMal
        title {
            romaji
            english
        }
        type
        description
        coverImage {
            large
        }
      }
    }
    '''
    variables = {'id': series_obj.api_id}

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})

    return json.loads(response.content.decode("utf-8"))['data']['Media']
