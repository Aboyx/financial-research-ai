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

def get_company_facts(cik: int) -> dict:
    formatted_cik = str(cik).zfill(10)

    url = (
        f"https://data.sec.gov/api/xbrl/companyfacts/"
        f"CIK{formatted_cik}.json"
    )

    response = httpx.get(url, headers=HEADERS)
    response.raise_for_status()

    return response.json()

def get_annual_revenue(facts: dict) -> list[dict]:
    revenue = facts["facts"]["us-gaap"][
        "RevenueFromContractWithCustomerExcludingAssessedTax"
    ]

    annual_revenue_by_end = {}

    for item in revenue["units"]["USD"]:
        if item["form"] == "10-K" and item["fp"] == "FY":
            annual_revenue_by_end[item["end"]] = item

    results = []

    for end_date, item in annual_revenue_by_end.items():
        results.append(
            {
                "fiscal_year": int(end_date[:4]),
                "revenue": item["val"],
                "period_end": end_date,
            }
        )

    return results


if __name__ == "__main__":
    company = get_company("MSFT")
    facts = get_company_facts(company["cik"])
    revenue = get_annual_revenue(facts)

    print(company["company_name"])
    print(revenue[-3:])