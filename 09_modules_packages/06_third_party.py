import sys

try:
    import requests
except ModuleNotFoundError:
    sys.exit("requests is not installed. Run: python -m pip install requests")

print("requests", requests.__version__)

try:
    r = requests.get("https://example.com", timeout=10)
    print(r.status_code, r.headers.get("content-type"), len(r.text))
except requests.RequestException as e:
    print("Network problem:", e)