import requests


class Protocol:
    HTTP = 'http'
    HTTPS = 'https'


def check_connectivity(protocol, url, timeout):
    try:
        requests.get(f'{protocol}://{url}', timeout=timeout).close()
        return True
    except Exception as e:
        s = str(e)
        try:
            if s[s.index("RemoteDisconnected") + 1 + len("RemoteDisconnected"):].strip(")").strip("'") == \
                    'Remote end closed connection without response':
                return True
            else:
                return False
        except:
            return False
