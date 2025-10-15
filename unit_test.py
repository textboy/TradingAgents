import os
from dotenv import load_dotenv
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

load_dotenv()
print(f'OPENAI_API_KEY---------:{os.environ.get("OPENAI_API_KEY")}')

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openrouter"
config["backend_url"] = "https://openrouter.ai/api/v1"
config["deep_think_llm"] = "deepseek/deepseek-chat-v3-0324:free"  # Use a different model
config["quick_think_llm"] = "meta-llama/llama-4-scout:free"  # Use a different model
config["max_debate_rounds"] = 1  # Increase debate rounds

# Configure data vendors (default uses yfinance and Alpha Vantage)
config["data_vendors"] = {
    "core_stock_apis": "yfinance",           # Options: yfinance, alpha_vantage, local
    "technical_indicators": "yfinance",      # Options: yfinance, alpha_vantage, local
    "fundamental_data": "alpha_vantage",     # Options: openai, alpha_vantage, local
    "news_data": "alpha_vantage",            # Options: openai, alpha_vantage, google, local
}

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)