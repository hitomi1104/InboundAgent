import requests

def test_fmcsa_api():
    # Test with a known valid MC number 
    mc_number = "123456"
    api_key = "cdc33e44d693a3a58451898d4ec9df862c65b954"
    
    # Try different URL formats
    urls = [
        f"https://mobile.fmcsa.dot.gov/qc/services/carriers/snapshot?mcNumber={mc_number}&webKey={api_key}",
        f"https://mobile.fmcsa.dot.gov/qc/services/carriers/{mc_number}/snapshot?webKey={api_key}",
        f"https://mobile.fmcsa.dot.gov/qc/services/carriers/{mc_number}?webKey={api_key}",
        f"https://mobile.fmcsa.dot.gov/qc/services/carriers?mcNumber={mc_number}&webKey={api_key}"
    ]
    
    for i, url in enumerate(urls):
        print(f"\nTrying URL format {i+1}: {url}")
        try:
            response = requests.get(url)
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text[:100]}...")  # Print first 100 chars
        except Exception as e:
            print(f"Error: {str(e)}")


''' f"https://mobile.fmcsa.dot.gov/qc/services/carriers?mcNumber={mc_number}&webKey={api_key}"'''

if __name__ == "__main__":
    test_fmcsa_api()