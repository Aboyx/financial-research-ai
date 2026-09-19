def get_company(ticker: str) -> dict:
    return {
        "ticker": ticker.upper(),
        "company_name": "Unknown",
    }


if __name__ == "__main__":
    print(get_company("msft"))

    