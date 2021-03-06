""" Filter websites based on keywords """
import requests

ALLOWED_DOMAINS = ["zqktlwi4fecvo6ri.onion",
                   "tt3j2x4k5ycaa5zt.onion",
                   "msydqstlz2kzerdg.onion",
                   "3bbaaaccczcbdddz.onion",
                   "donionsixbjtiohce24abfgsffo2l4tk26qx464zylumgejukfq2vead.onion"]

def search(url):
    """
    Search domains for filtering.
    """
    resp = requests.get(url)
    domain_list = []
    for hit in resp.json()["hits"]["hits"]:
        domain = hit["_source"]["domain"]
        if not domain in domain_list:
            domain_list.append(domain)
        #print(hit["_source"].get("title", "").encode("ascii","ignore"))
        if domain not in ALLOWED_DOMAINS:
            print(domain)

def main():
    """
    Search based on key words and filter pages.
    """
    url = "http://localhost:9200/latest-tor/_search?pretty&size=9000&_source=title,domain"
    keywords_list = ['preteen', 'loli', 'lolita', 'jailbait', 'pthc', 'best cp',
                     '"child porn"', '"kid porn"', '"child sex"', '"cp video"',
                     '"nude children"', '"cp porn"', '"free child porn"', 'kinderporn',
                     '"child rape"', '"toddler porn"', '"kids videos"', '"cp videos"',
                     'lolilust', '"pedo porno"', '"pedo content"', 'underage', '"cp pack"',
                     'loliporn', 'pedofamily', '"cp database"', '"pedo webcams"', 'lolitacity']
    url = url + "&q=(" + " OR ".join(keywords_list).replace(" ", "%20")
    url = url + ")%20AND%20(porn%20OR%20porno)"
    search(url)

if __name__ == '__main__':
    main()
