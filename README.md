# Web Crawler Tool

This is a simple web crawler tool designed to extract URL parameters from web pages. It supports filtering parameters based on user-defined criteria and saves the results to a text file.

## Features

- Fetches HTML content from a given URL
- Extracts and filters URL parameters from hyperlinks
- Saves extracted parameters in a structured text file format
- Supports inclusion and exclusion of specific parameters through command-line arguments

## Installation

To run this script, you need Python installed on your system. The required Python packages are listed below:

- `requests`
- `beautifulsoup4`

You can install these packages using pip:

```bash
pip install requests beautifulsoup4
```
## Usage
```bash
python web_crawler.py <url> <output_file> [--include param1,param2] [--exclude param1,param2]
```
### Parameters
-> <url>: The target URL from which to extract parameters.
-> <output_file>: The file where the extracted parameters will be saved.
-> --include: (Optional) Comma-separated list of parameters to include.
-> --exclude: (Optional) Comma-separated list of parameters to exclude.

### Example
To extract parameters from https://www.example.com and include only the q parameter, use:
```bash
python web_crawler.py https://www.example.com output.txt --include q
```
To exclude the session parameter:
```bash
python web_crawler.py https://www.example.com output.txt --exclude session
```
## Code Overview
* `fetch_page`: Fetches the HTML content of a specified URL.
* `extract_url_parameters`: Extracts and optionally filters URL parameters from the fetched content.
* `filter_parameters`: Applies inclusion/exclusion filters to parameters.
* `save_to_text`: Saves the extracted parameters to a text file.
* `parse_args`: Handles command-line arguments for inclusion/exclusion criteria.
* `main`: Main function that orchestrates the tool's workflow.
