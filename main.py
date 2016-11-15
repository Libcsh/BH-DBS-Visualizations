import json
import requests as re

def make_events(input_url):
    response = re.get(input_url)
    response = response.content
    jres = json.loads(response)
    for i in range(len(jres['hits']['hits'])):
        image_url = jres['hits']['hits'][i]['_source']['main_image_url']
        year = jres['hits']['hits'][i]['_source']['PeriodDesc']['En']
        text_title = jres['hits']['hits'][i]['_source']['Header']['En'].encode('utf-8')
        text_text = jres['hits']['hits'][i]['_source']['UnitText1']['En'].encode('utf-8')
# Add each item as an event to the Json file
        events.append({"media": {"url": str(image_url)}, "start_date": {"year": str(year)}, "text": {"headline": str(text_title), "text": str(text_text)}})

# urls_list should be a text file of urls: http://api.dbs.bh.org.il/v1/search?q=cohen // search?from_=15&q=cohen // Etc.
def all_urls_events(urls_list):
    in_f = open(urls_list, 'r')
    for input_url in in_f:
        make_events(input_url)

def main():
    out_f = open('tempp.txt', 'w')
    all_urls_events()
# Join all events list to "title" dict
    tm_json = {"title": {"media": {"url": "https://storage.googleapis.com/bhs-flat-pics/0EB01FB3-F957-499B-B8D9-C8683A330EB0.jpg"}, "text": {"headline": "Synagogues Around the World", "text": "<p>Houston's voice caught the imagination of the world propelling her to superstardom at an early age becoming one of the most awarded performers of our time. This is a look into the amazing heights she achieved and her personal struggles with substance abuse and a tumultuous marriage.</p>"}}, "events": events}
# Make the json
    json.dump(tm_json, out_f)
    print("Done. open tempp.txt")

events = []
if __name__ == '__main__':
    main()