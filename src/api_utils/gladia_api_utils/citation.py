import json

import requests
from lxml import objectify


def get_doi(doi: str) -> dict:
    crossref_url = f"http://api.crossref.org/works/{doi}"
    req = requests.get(crossref_url)
    if req.status_code == 200:
        return json.loads(req.content)
    else:
        return dict()


def get_arxiv(arxiv_id: str) -> dict:
    arxiv_url = f"http://export.arxiv.org/api/query?search_query={arxiv_id}&start=0&max_results=1"
    req = requests.get(arxiv_url)
    if req.status_code == 200:
        return objectify.fromstring(req.content)
    else:
        return dict()
