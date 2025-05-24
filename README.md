# MCP Agents

A powerful AI agents platform that enables automated interactions with various services and APIs, including web browsing, stock market data retrieval, and more.

## Architecture

### MCP Server Components

- **Core Server**:
  - Handles agent coordination and task management
  - Implements async communication patterns
  - Manages service integrations

- **Service Integrations**:
  1. **Browser MCP**:
     - Playwright-based web automation
     - Multi-tab browser management
     - Screenshot and PDF capabilities
     - Form interaction handling
  
  2. **Finance MCP**:
     - Stock market data integration (yfinance)
     - Historical and real-time data processing
  
  3. **Airbnb MCP**:
     - Property search and filtering
     - Listing details retrieval
     - Booking information handling
  
  4. **Search MCP**:
     - DuckDuckGo integration
     - Web search capabilities

### Agent System

- **MCPAgent Class**:
  - Manages conversation state
  - Handles tool selection and execution
  - Implements memory management
  - Coordinates with LLM for decision making

- **MCPClient Class**:
  - Manages service connections
  - Handles configuration loading
  - Implements session management
  - Provides unified API access

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

- **Airbnb Integration**:
  - Search for listings with customizable filters
  - Get detailed property information
  - Support for:
    - Check-in/check-out dates
    - Number of guests (adults, children, infants)
    - Price ranges
    - Location-based search
    - Pet-friendly options

- **Search Capabilities**:
  - Web search functionality
  - DuckDuckGo integration for privacy-focused searches

## Prerequisites

- Python 3.x
- Virtual Environment (recommended)
- Node.js and NPX (for Playwright and browser automation)
- Groq API key (for LLM integration)

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

4. Install Playwright using NPX:
```bash
# Install Playwright browsers using NPX
npx playwright install --with-deps

# For specific browsers only
npx playwright install chromium
npx playwright install firefox
npx playwright install webkit
```

5. Configure environment:
```bash
# Create .env file
touch .env

# Add required API keys
echo "GROQ_API_KEY=your_groq_api_key" >> .env
```

## Development Tools

### NPX Commands

The project uses NPX for various development and testing tasks:

```bash
# Run Playwright tests
npx playwright test

# Run Playwright in debug mode
npx playwright test --debug

# Show Playwright test report
npx playwright show-report

# Start Playwright Inspector
npx playwright codegen
```

## Usage

### Initialize MCP Client
```python
from mcp_use import MCPClient, MCPAgent
from langchain_groq import ChatGroq

# Initialize client with configuration
client = MCPClient.from_config_file("browser_mcp.json")

# Initialize LLM
llm = ChatGroq(model="qwen-qwq-32b")

# Create agent
agent = MCPAgent(
    llm=llm,
    client=client,
    max_steps=15,
    memory_enabled=True
)
```

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

### Airbnb Search
```python
# Example of searching Airbnb listings
airbnb_results = airbnb_search(
    location="Miami, FL",
    checkin="2024-06-01",
    checkout="2024-06-07",
    adults=2,
    children=0,
    max_price=300
)

# Get detailed information about a specific listing
listing_details = airbnb_listing_details(
    id="listing_id",
    checkin="2024-06-01",
    checkout="2024-06-07",
    adults=2
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
│   ├── airbnb/           # Airbnb integration modules
│   └── search/           # Search functionality modules
├── tests/                # Test files
│   └── playwright/       # Playwright test scripts
├── playwright.config.js  # Playwright configuration
├── browser_mcp.json      # Browser MCP configuration
├── package.json          # Node.js dependencies
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Configuration

### browser_mcp.json
```json
{
  "browser": {
    "headless": true,
    "viewport": {
      "width": 1280,
      "height": 720
    }
  },
  "services": {
    "airbnb": {
      "enabled": true
    },
    "finance": {
      "enabled": true
    },
    "search": {
      "enabled": true
    }
  }
}
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
- [Groq](https://groq.com/) for LLM capabilities
