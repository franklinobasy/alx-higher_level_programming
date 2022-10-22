#!/usr/bin/python3
'''
A Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
'''


if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    url, email = sys.argv[1:3]
    value = {"email": email}

    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
