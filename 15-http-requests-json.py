import urllib.request
import json

def printResults(data):
    # parse string to json
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print("metadata.title:", theJSON["metadata"]["title"])
        print("#earthquakes recorded in the past 24h:", theJSON["metadata"]["count"])

    for feature in theJSON["features"]:
        print(feature["properties"]["place"], "(magnitude %2.1f)" % feature["properties"]["mag"])


def main():
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
  
  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))

  if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
  else:
    print ("Received an error from server", str(webUrl.getcode()))


if __name__ == "__main__":
    main()
