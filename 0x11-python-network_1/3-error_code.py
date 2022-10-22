#!/usr/bin/python3
'''
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
'''


if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode('UTF-8'))
    except urllib.error.HTTPError as er:
        print('Error code:', er.code)
