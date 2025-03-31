import httpx

def get_response(URL, headers, LIMIT, params=None):
    response = httpx.get(URL, headers=headers, params=None)

    if response.status_code == 200:
        json_response = response.json()
        metadata = json_response.get("meta")
        results = json_response.get("results")

        countries = [{"id": result.get("id"), "name": result.get("name")} for result in results]

        return metadata, countries


def page_count(total, limit):
    return total - limit


BASE_URL: str = "https://api.openaq.org/v3"
API_KEY: str = "9ef389e4242cbe4c0842bbbf1e1ddf02e6a3f867e1be2dec5b8ff1181757ca53"

URL: str = BASE_URL + "/countries"

headers: dict = {"X-API-Key": API_KEY}
LIMIT: int = 100

countries = []
diff = 1

metadata, results = get_response(URL, headers, LIMIT)
countries.extend(results)

if page_count(int(metadata.get("found")), LIMIT) > 1:
    for _ in range(2, pa):



