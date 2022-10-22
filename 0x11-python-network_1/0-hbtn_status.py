#!/usr/bin/python3
'''
A Python script that fetches https://alx-intranet.hbtn.io/status
'''

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        content = resp.read()

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
