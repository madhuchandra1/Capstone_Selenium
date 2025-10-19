import requests
from urllib.parse import urljoin

def check_broken_links(driver, base_url):
    links = driver.find_elements("tag name", "a")
    broken = []
    known_broken = ["/status_codes/500"]  # Ignore intentional broken links

    for link in links:
        href = link.get_attribute("href")
        if href and href.startswith("http"):
            # Skip known broken links
            if any(kb in href for kb in known_broken):
                continue
            try:
                # Disable SSL verification for testing
                res = requests.head(href, timeout=5, verify=False)
                if res.status_code >= 400:
                    broken.append((href, res.status_code))
            except Exception as e:
                broken.append((href, str(e)))
    return broken