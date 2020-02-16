import urllib.request


def main():
    webUrl = urllib.request.urlopen("http://www.google.com")

    print("response code:", webUrl.getcode())
    print("response body:", webUrl.read())


if __name__ == "__main__":
    main()
