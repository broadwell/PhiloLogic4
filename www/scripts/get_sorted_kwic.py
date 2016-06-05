#!/usr/bin/env python

import os
import unicodedata
from wsgiref.handlers import CGIHandler

from philologic.DB import DB
from philologic.app import page_interval, kwic_hit_object

from philologic.app import WebConfig
from philologic.app import WSGIHandler
import simplejson


def get_sorted_kwic(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'application/json; charset=UTF-8'), ("Access-Control-Allow-Origin", "*")]
    start_response(status, headers)
    config = WebConfig(os.path.abspath(os.path.dirname(__file__)).replace('scripts', ''))
    db = DB(config.db_path + '/data/')
    input_object = simplejson.loads(environ['wsgi.input'].read())
    all_results = input_object['results']
    query_string = input_object['query_string']
    sort_keys = [i for i in input_object["sort_keys"] if i]
    environ['QUERY_STRING'] = query_string.encode('utf8')
    request = WSGIHandler(environ, config)
    sorted_hits = get_sorted_hits(all_results, sort_keys, request, config, db, input_object['start'],
                                  input_object['end'])
    yield simplejson.dumps(sorted_hits)


def get_sorted_hits(all_results, sort_keys, request, config, db, start, end):
    hits = db.query(request["q"], request["method"], request["arg"], **request.metadata)
    start, end, n = page_interval(request.results_per_page, hits, start, end)
    kwic_object = {
        "description": {"start": start,
                        "end": end,
                        "results_per_page": request.results_per_page},
        "query": dict([i for i in request])
    }

    kwic_results = []

    def smash_accents(char):
        try:
            return [i for i in unicodedata.normalize("NFKD", char) if not unicodedata.combining(i)]
        except TypeError:
            return [i for i in unicodedata.normalize("NFKD", char.decode('utf8')) if not unicodedata.combining(i)]

    def make_sort_key(d):
        key = [smash_accents(d[f]) for f in sort_keys]
        return key

    all_results.sort(key=make_sort_key, reverse=False)
    for index in all_results[start:end]:
        hit = hits[index["index"]]
        kwic_result = kwic_hit_object(hit, config, db)
        kwic_results.append(kwic_result)

    kwic_object['results'] = kwic_results
    kwic_object['results_length'] = len(hits)
    kwic_object["query_done"] = hits.done

    return kwic_object


if __name__ == "__main__":
    CGIHandler().run(get_sorted_kwic)