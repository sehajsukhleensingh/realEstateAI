import requests
from bs4 import BeautifulSoup
import random

# URL to scrape fresh proxies
PROXY_SITES = [
    "https://www.sslproxies.org/",
    "https://free-proxy-list.net/",
    "https://www.us-proxy.org/",
    "https://www.proxynova.com/proxy-server-list/"
]

def scrape_proxies():
    """Scrape fresh proxies from the given proxy sites."""
    proxies = []
    headers = {"User-Agent": "Mozilla/5.0"}
    
    for url in PROXY_SITES:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Finding proxies in table rows
            for row in soup.select("table tbody tr"):
                columns = row.find_all("td")
                if len(columns) > 1:
                    ip = columns[0].text.strip()
                    port = columns[1].text.strip()
                    protocol = "http"  # Assume HTTP unless specified otherwise
                    full_proxy = f"{ip}:{port}"
                    proxies.append(full_proxy)

        except Exception as e:
            print(f"Error scraping {url}: {e}")

    return list(set(proxies))  # Remove duplicates

def test_proxy(proxy):
    """Check if the proxy is working."""
    url = "http://ipinfo.io/json"
    proxy_dict = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
    
    try:
        response = requests.get(url, proxies=proxy_dict, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    
    return False

def get_working_proxies(proxies, max_proxies=10):
    """Test proxies and return a list of working ones."""
    working_proxies = []
    
    for proxy in proxies:
        if test_proxy(proxy):
            print(f"✅ {proxy} is working")
            working_proxies.append(proxy)
            if len(working_proxies) >= max_proxies:
                break  # Stop once we get enough working proxies
        else:
            print(f"❌ {proxy} failed")
    
    return working_proxies

# Run the script
print("Scraping fresh proxies...")
proxies = scrape_proxies()

print(f"Testing {len(proxies)} proxies...")
working_proxies = get_working_proxies(proxies)

print("\n✅ Working Proxies:")
print(working_proxies)