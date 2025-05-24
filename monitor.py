# monitor.py
import requests

# Check a single website
def check_website(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "*/*"}, timeout=10)
        status_code = response.status_code
        is_live = 200 <= status_code < 300

        return {
            "status": status_code,
            "is_live": is_live
        }

    except requests.exceptions.RequestException as e:
        return {
            "status": "Error",
            "is_live": False,
            "error": str(e)
        }

# Check all websites from the list
def check_all_websites():
    websites = [
        "https://www.thanepolice.gov.in",
        "https://sindhudurgpolice.gov.in",
        "https://punerailwaypolice.gov.in",
        "https://nashikcitypolice.gov.in",
        "https://nandurbar.mahapolice.gov.in",
        "https://pcpc.gov.in",
        "https://solapurpolice.gov.in",
        "https://dhulepolice.gov.in",
        "https://ahmednagardistpolice.gov.in",
        "https://satarapolice.gov.in/",
        "https://amravatiruralpolice.gov.in",
        "https://csn.mahapolice.gov.in",
        "https://csnrailway.mahapolice.gov.in",
        "https://nashikruralpolice.gov.in",
        "https://solapurcitypolice.gov.in",
        "https://buldhanapolice.gov.in",
        "https://akolapolice.gov.in",
        "https://hingolipolice.gov.in",
        "https://gadchirolirange.mahapolice.gov.in",
        "https://gadchirolipolice.gov.in",
        "https://puneruralpolice.gov.in",
        "https://maharashtrasrpf.gov.in",
        "https://konkanrange.dreamcaredevelopers.com",
        "https://apikolhapurrange.dreamcaredevelopers.com",
        "https://api.thanepolice.gov.in",
        "https://api.thaneruralpolice.gov.in",
        "https://mbvvapi.dreamcaredevelopers.com",
        "https://apidharashiv.dreamcaredevelopers.com",
        "https://navi-mumbai-backend-new-production.up.railway.app",
        "https://apigondia.dreamcaredevelopers.com/api/get-visitors",
        "https://api.laturpolice.gov.in/api/get-visitors",
        "https://api.sindhudurgpolice.gov.in/api/get-visitors",
        "https://api.punerailwaypolice.gov.in/api/get-visitors",
        "https://api.nashikcitypolice.gov.in/api/get-visitors",
        "https://nandurbarapi.dreamcaredevelopers.com/api/get-visitors",
        "https://api.pcpc.gov.in"
    ]
    
    status_dict = {}
    for url in websites:
        result = check_website(url)
        status_dict[url] = result

        if result["status"] == "Error":
            print(f"❌ {url}: {result['error']}")
        else:
            emoji = "✅" if result["is_live"] else "❌"
            print(f"{emoji} {url}: {result['status']}")

    return status_dict

# To run directly
if __name__ == "__main__":
    check_all_websites()
