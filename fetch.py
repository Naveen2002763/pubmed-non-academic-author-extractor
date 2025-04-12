import requests
import xmltodict
from typing import List, Dict

API_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str, retmax: int = 100) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }
    response = requests.get(f"{API_BASE}esearch.fcgi", params=params)
    response.raise_for_status()
    return response.json()['esearchresult']['idlist']

def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    ids = ",".join(pubmed_ids)
    params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml"
    }
    response = requests.get(f"{API_BASE}efetch.fcgi", params=params)
    response.raise_for_status()
    return xmltodict.parse(response.content)['PubmedArticleSet']['PubmedArticle']
