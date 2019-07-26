import argparse
import datetime
import json
import logging
import os

import lxml.html
import requests
from newspaper import Article

logger = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="input a url to analyze", type=str, default=None)
parser.add_argument(
    "--output_file", help="output file write results to", type=str, default=None
)


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


def main(args):
    if not args.get("url"):
        logger.warning(" You must provide a url")
        return
    output = {
        "url": args["url"],
        "date_scraped": datetime.datetime.now().strftime("%c"),
    }

    output["text"] = get_text_from_url(args["url"])
    output["urls"] = get_urls_from_url(args["url"])

    output_as_string = json.dumps(output)
    if args.get("output_file"):
        with open(args["output_file"], "w") as f:
            f.write(output_as_string)

    return output_as_string


if __name__ == "__main__":
    args = vars(parser.parse_args())
    output = main(args)

    if output:
        print(output)
