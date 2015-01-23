import urlparse
import requests

from lateral.doc import LateralDoc


class LateralAPI():
    base = None

    def __init__(self, key):
        self.key = key

    def _post(self, endpoint, data={}):
        return self._request('post', endpoint, data)

    def _get(self, endpoint, data={}):
        return self._request('get', endpoint, data)

    def _request(self, method, endpoint, data={}):
        data['subscription-key'] = self.key
        url = urlparse.urljoin(self.base, endpoint)
        resp = getattr(requests.api, method)(url, params=data)
        if resp.status_code != 200:
            resp.raise_for_status()
        return resp


class LateralRecommender(LateralAPI):
    base = 'https://api.lateral.io/recommender/'

    def add_doc(self, text, doc_id=None):
        if doc_id is None:
            doc_id = hash(text)

        data = {
            'document_id': doc_id,
            'text': text
        }

        self._post('add/', data)
        return doc_id

    def delete_doc(self, doc_id):
        self._post('delete/', {'document_id': doc_id})

    def delete_all_docs(self):
        self._post('delete-all/')

    def fetch_doc(self, doc_id):
        resp = self._get('fetch/', {'document_id': doc_id})
        return LateralDoc(resp.json())

    def list_doc_ids(self):
        resp = self._get('list/')
        return resp.json()

    def _recommend(self, query, num_results=None, doc_ids=None):
        if num_results is not None:
            query['results'] = num_results
        if doc_ids is not None:
            query['select_from'] = doc_ids
        resp = self._post('recommend-by-id/', data=query)
        return resp.json()

    def recommend_by_id(self, doc_id, num_results=None, doc_ids=None):
        return self._recommend({'document_id': doc_id}, num_results, doc_ids)

    def recommend_by_text(self, text, num_results=None, doc_ids=None):
        return self._recommend({'text': text}, num_results, doc_ids)

    def update_doc(self, doc_id, text='', meta={}):
        if text:
            data = {
                'document_id': doc_id,
                'text': text
            }
            self._post('update-text/', data)
        if meta:
            data = {
                'document_id': doc_id,
                'meta': meta
            }
            self._post('update-meta/', data)
