import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import sys
from collections import defaultdict

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_url_parameters(html, include_params=None, exclude_params=None):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', href=True)
    results = []

    for link in links:
        href = link['href']
        parsed_url = urlparse(href)
        query_params = parse_qs(parsed_url.query)
        if filter_parameters(query_params, include_params, exclude_params):
            results.append({'url': href, 'parameters': query_params})

    return results

def filter_parameters(params, include, exclude):
    if include:
        for key in include:
            if key in params:
                return True
        return False
    if exclude:
        for key in exclude:
            if key in params:
                return False
    return True

def save_to_text(parameters, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for param in parameters:
            file.write(f"URL: {param['url']}\n")
            file.write("Parameters:\n")
            for key, values in param['parameters'].items():
                file.write(f"  {key}: {', '.join(values)}\n")
            file.write("\n")

def parse_args(args):
    include_params = []
    exclude_params = []
    if "--include" in args:
        include_index = args.index("--include") + 1
        include_params = args[include_index].split(',')
    if "--exclude" in args:
        exclude_index = args.index("--exclude") + 1
        exclude_params = args[exclude_index].split(',')
    return include_params, exclude_params

def main():
    if len(sys.argv) < 3:
        print("Usage: python web_crawler.py <url> <output_file> [--include param1,param2] [--exclude param1,param2]")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]
    include_params, exclude_params = parse_args(sys.argv)

    html = fetch_page(url)
    if html:
        parameters = extract_url_parameters(html, include_params, exclude_params)
        save_to_text(parameters, output_file)
        print(f"Parameters saved to {output_file}")
    else:
        print("Failed to retrieve data or no parameters found.")

if __name__ == "__main__":
    main()
