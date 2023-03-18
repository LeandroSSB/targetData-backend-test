from elasticsearch import Elasticsearch


def connect_elasticsearch(**kwargs):
    _es_hosts = ["localhost:9200"]
    if 'hosts' in kwargs.keys():
        _es_hosts = kwargs['hosts']
    _es_obj = None
    _es_obj = Elasticsearch(hosts=_es_hosts, timeout=10)
    if _es_obj.ping():
        print("connected")
    else:
        print("not connected")
    return _es_obj


es = connect_elasticsearch()
