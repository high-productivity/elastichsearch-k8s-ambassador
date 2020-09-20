from elasticsearch import Elasticsearch
from mapping import INDEX_SETTINGS, DATA_MAPPING

import re
import requests
import ssl


def main():

    requests.packages.urllib3.disable_warnings()

    ssl._create_default_https_context = ssl._create_unverified_context

    INDEX = 'coins'

    client = Elasticsearch('http://elastic:2635ZPLR23Uu21Q9wcCB6fKT@a5b0f0a5c15584a2d8bec651c60e7319-468481736.ap-southeast-1.elb.amazonaws.com/es')
    if not client.indices.exists(INDEX):
        client.indices.create(INDEX, body={
            'settings': INDEX_SETTINGS,
        })
    client.indices.put_mapping(index=INDEX, doc_type='pair', body=DATA_MAPPING, include_type_name=True)

    with open('./data.json') as json_file:
        data = json.load(json_file)
        for item in data:
            client.index(ELASTIC_INDEX, item)


if __name__ == '__main__':
    import sys
    sys.exit(main())
