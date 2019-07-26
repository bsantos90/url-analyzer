import lxml.html
import requests
from newspaper import Article


def get_text_from_url(url):
    if not url.startswith("http://"):
        url = "http://" + url
    a = Article(url)
    a.download()
    a.parse()
    return a.text


def get_urls_from_url(url):
    urls = []
    if not url.startswith("http://"):
        url = "http://" + url
    res = requests.get(url)
    if res.status_code == 200:
        document = lxml.html.fromstring(res.text)
        for a_tag in document.xpath("//a"):
            try:
                urls.append(
                    {
                        "text": a_tag.xpath("./text()")[0],
                        "url": a_tag.xpath("./@href")[0],
                    }
                )
            except IndexError:
                pass
    return urls
