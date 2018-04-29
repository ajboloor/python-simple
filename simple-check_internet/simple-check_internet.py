def check_internet():
    try:
        import httplib
    except:
        import http.client as httplib

    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        print("Internet access available.")
        return True
    except:
        conn.close()
        print("ERROR: Internet access not available.")
        return False

check_internet()
