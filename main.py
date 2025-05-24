from monitor import check_website
from whatsapp import send_whatsapp_message

MAX_MSG_LENGTH = 1600  # Twilio WhatsApp message size limit

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
    "https://amravatiruralpolice.gov.in",
    "https://csn.mahapolice.gov.in",
    "https://nashikruralpolice.gov.in",
    "https://akolapolice.gov.in",
    "https://gadchirolirange.mahapolice.gov.in",
    "https://gadchirolipolice.gov.in",
    "https://puneruralpolice.gov.in",
    "https://maharashtrasrpf.gov.in",
    "https://konkanrange.dreamcaredevelopers.com/api/get-visitors",
    "https://apikolhapurrange.dreamcaredevelopers.com/api/get-visitors",
    "https://api.thanepolice.gov.in/api/get-visitors",
    "https://api.thaneruralpolice.gov.in/api/get-visitors",
    "https://mbvvapi.dreamcaredevelopers.com/api/get-visitors",
    "https://apidharashiv.dreamcaredevelopers.com/api/get-visitors",
    "https://apigondia.dreamcaredevelopers.com/api/get-visitors",
    "https://api.laturpolice.gov.in/api/get-visitors",
    "https://api.sindhudurgpolice.gov.in/api/get-visitors",
    "https://api.punerailwaypolice.gov.in/api/get-visitors",
    "https://api.nashikcitypolice.gov.in/api/get-visitors",
    "https://nandurbarapi.dreamcaredevelopers.com/api/get-visitors",
    "https://api.pcpc.gov.in/api/get-visitors"
]

def chunk_messages(prefix, lines, max_length=1600):
    chunks = []
    current_chunk = prefix
    for line in lines:
        if len(current_chunk) + len(line) + 1 > max_length:
            chunks.append(current_chunk)
            current_chunk = prefix + line + "\n"
        else:
            current_chunk += line + "\n"
    if current_chunk.strip():
        chunks.append(current_chunk)
    return chunks

if __name__ == "__main__":
    down_sites = []

    for url in websites:
        result = check_website(url)
        if not result["is_live"]:
            status = result.get("status", "Error")
            error = result.get("error", "")
            down_sites.append(f"{url} ❌ (Status: {status}) {error}")

    if down_sites:
        chunks = chunk_messages("⚠️ Websites Down:\n", down_sites)
        for msg in chunks:
            send_whatsapp_message(msg)
    else:
        send_whatsapp_message("✅ All websites are live.")
