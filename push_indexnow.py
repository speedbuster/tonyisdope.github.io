import urllib.request
import json

def notify_indexnow(urls_to_submit):
    endpoint = "https://api.indexnow.org/IndexNow"
    payload = {
        "host": "www.tonyisdope.com.ng",
        "key": "0cb7ff1b944c4853b0257fcc855086fa",
        "keyLocation": "https://www.tonyisdope.com.ng/0cb7ff1b944c4853b0257fcc855086fa.txt",
        "urlList": urls_to_submit
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        endpoint, 
        data=data, 
        headers={'Content-Type': 'application/json; charset=utf-8'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status in (200, 202):
                print(f"Successfully submitted {len(urls_to_submit)} URLs to IndexNow!")
            else:
                print(f"IndexNow returned status code: {response.status}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    sample_urls = [
        "https://www.tonyisdope.com.ng/facebook-ads-landing-page.html",
        "https://www.tonyisdope.com.ng/google-ads-landing-page.html"
    ]
    notify_indexnow(sample_urls)