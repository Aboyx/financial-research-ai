from financial_research_ai.main import get_company


def test_get_company_returns_microsoft():
    company = get_company("MSFT")

    assert company["ticker"] == "MSFT"
    assert company["company_name"] == "MICROSOFT CORP"
    assert company["cik"] == 789019
    