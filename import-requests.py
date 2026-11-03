import html as html_lib
import requests
from bs4 import BeautifulSoup
import os
import subprocess

def fetch_peptide_prices(url, selectors):
    """
    Fetch peptide prices from a given URL based on CSS selectors.

    Args:
        url (str): The URL of the peptide vendor's page.
        selectors (dict): Dictionary with keys 'product' and 'price' for CSS selectors.

    Returns:
        list of dict: A list of dictionaries containing product names and prices.
    """
    response = requests.get(url, timeout=30)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = soup.select(selectors['product'])
    prices = soup.select(selectors['price'])

    data = []
    for product, price in zip(products, prices):
        data.append({
            'Product': product.get_text(strip=True),
            'Price': price.get_text(strip=True)
        })
    
    return data

def generate_html(data):
    """
    Generate an HTML page to display peptide prices.

    Args:
        data (list of dict): The peptide price data.

    Returns:
        str: HTML content as a string.
    """
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Peptide Prices</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Peptide Prices</h1>
    <table>
        <tr>
            <th>Product</th>
            <th>Price</th>
        </tr>
"""
    for row in data:
        # Scraped text is someone else's: escape it, or a vendor page could put
        # <script> on the published site.
        html += f"<tr><td>{html_lib.escape(str(row['Product']))}</td><td>{html_lib.escape(str(row['Price']))}</td></tr>"
    html += """
    </table>
</body>
</html>
"""
    return html

def save_html_to_github(repo_path, file_name, html_content):
    """
    Save the HTML content to a local file in the GitHub repository and push changes.

    Args:
        repo_path (str): Path to the local GitHub repository.
        file_name (str): Name of the HTML file.
        html_content (str): HTML content to save.
    """
    file_path = os.path.join(repo_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"HTML content saved to {file_path}.")

    # Automate git commit and push
    try:
        subprocess.run(['git', '-C', repo_path, 'add', file_name], check=True)
        subprocess.run(['git', '-C', repo_path, 'commit', '-m', 'Update peptide prices'], check=True)
        subprocess.run(['git', '-C', repo_path, 'push'], check=True)
        print("Changes pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")

if __name__ == "__main__":
    # Example configuration
    peptide_vendors = [
        {
            'url': 'https://example-peptide-vendor.com/products',
            'selectors': {
                'product': '.product-name',
                'price': '.product-price'
            }
        }
    ]

    aggregated_data = []
    for vendor in peptide_vendors:
        data = fetch_peptide_prices(vendor['url'], vendor['selectors'])
        aggregated_data.extend(data)

    # Generate HTML content
    html_content = generate_html(aggregated_data)

    # Save HTML to GitHub repository
    repo_path = "path/to/your/github/repo"  # Replace with the local path to your GitHub repository
    file_name = "index.html"  # Replace with the desired HTML file name
    save_html_to_github(repo_path, file_name, html_content)
    
    print("Peptide prices HTML generated successfully!")
