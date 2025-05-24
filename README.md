# MCP Agents

A powerful AI agents platform that enables automated interactions with various services and APIs, including web browsing, stock market data retrieval, and more.

## Features

- **Web Browsing Automation**: Automated browser control using Playwright
  - Navigate websites
  - Handle forms and interactions
  - Take screenshots
  - Manage multiple tabs
  - Handle cookies and dialogs

- **Financial Data Integration**: 
  - Stock market data retrieval using yfinance
  - Historical price data
  - Real-time market information

- **Search Capabilities**:
  - Web search functionality
  - DuckDuckGo integration for privacy-focused searches

## Prerequisites

- Python 3.x
- Virtual Environment (recommended)
- Node.js (for Playwright)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp_agents
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install
```

## Usage

### Web Automation
```python
# Example of browser automation
await page.goto('https://www.example.com')
await page.click('button#submit')
await page.type('input#search', 'query')
```

### Stock Market Data
```python
# Example of retrieving stock data
stock_history = get_stock_history(
    symbol="AAPL",
    period="1mo",
    interval="1d"
)
```

### Web Search
```python
# Example of performing a web search
search_results = duckduckgo_search(
    query="your search query",
    safe_search="moderate"
)
```

## Project Structure

```
mcp_agents/
├── .venv/                 # Virtual environment
├── src/                   # Source code
│   ├── browser/          # Browser automation modules
│   ├── finance/          # Financial data modules
│   └── search/           # Search functionality modules
├── tests/                # Test files
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Playwright](https://playwright.dev/) for web automation
- [yfinance](https://github.com/ranaroussi/yfinance) for financial data
- [DuckDuckGo](https://duckduckgo.com/) for search functionality
