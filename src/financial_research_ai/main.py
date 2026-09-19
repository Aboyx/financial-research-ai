import httpx

SEC_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"

HEADERS = {
    "User-Agent": "financial-research-ai aboyx@outlook.com"
}


def get_company(ticker: str) -> dict:
    response = httpx.get(SEC_TICKERS_URL, headers=HEADERS)
    response.raise_for_status()

    companies = response.json()

    for company in companies.values():
        if company["ticker"].upper() == ticker.upper():
            return{
    "ticker": company["ticker"],
    "company_name": company["title"],
    "cik": company["cik_str"],
}

    return {"error": "Ticker not found"}


if __name__ == "__main__":
    print(get_company("MSFT"))