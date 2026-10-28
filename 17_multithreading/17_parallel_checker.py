import time
from concurrent.futures import ThreadPoolExecutor, as_completed

URLS = [
    "https://a.example/home", "https://b.example/api", "https://c.example/bad-link",
    "https://d.example/status", "https://e.example/bad-gateway", "https://f.example/docs",
    "https://g.example/login", "https://h.example/search",
]

def check(url):
    time.sleep(0.2 + (len(url) % 5) * 0.1)        # stands in for a network request
    if "bad" in url:
        raise ConnectionError("connection refused")
    return 200

def run_sequential():
    out = {}
    for url in URLS:
        try:
            out[url] = check(url)
        except ConnectionError as e:
            out[url] = f"FAIL ({e})"
    return out

def run_parallel(workers):
    out = {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(check, url): url for url in URLS}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                out[url] = fut.result()
            except ConnectionError as e:
                out[url] = f"FAIL ({e})"
    return out

for label, runner in (("sequential", run_sequential),
                      ("4 workers", lambda: run_parallel(4)),
                      ("8 workers", lambda: run_parallel(8))):
    start = time.perf_counter()
    out = runner()
    print(f"{label:<11}{time.perf_counter() - start:5.2f} s")

print()
for url in URLS:
    print(f"{url:<34}{out[url]}")