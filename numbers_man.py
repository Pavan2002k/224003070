from flask import Flask, jsonify, request
import requests

app = Flask("number_management_service")

def is_valid_url(url):
    try:
        response = requests.head(url, timeout=0.5)
        return response.status_code == 200 and 'application/json' in response.headers.get('content-type', '')
    except requests.RequestException:
        return False

def fetch_and_sort_numbers_from_url(url):
    try:
        response = requests.get(url, timeout=0.5)
        response.raise_for_status()
        data = response.json()
        numbers = data.get("numbers", [])
        sorted_numbers = sorted(numbers)
        return sorted_numbers
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {str(e)}")
        return []

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    merged_numbers = set()

    for url in urls:
        if is_valid_url(url):
            numbers = fetch_and_sort_numbers_from_url(url)
            merged_numbers.update(numbers)

    sorted_numbers = sorted(merged_numbers)

    return jsonify({"numbers": sorted_numbers})

if __name__ == '__main__':
    app.run(host='localhost', port=8008)
