# execution
(update API key in .env)
cdtrading
conda activate tradingcn
python -m cli.main
python unit_test.py > unit_test.log 2>&1

# git update
git add .
git commit -m "xxx"
git push origin mk

# coding trace
TradingAgentsGraph < trading_graph."Initialize LLMs" + trading_graph.setup_graph < setup.create_social_media_analyst < social_media_analyst
in setup.py, only create_research_manager & create_risk_manager use deep_thinking_llm, others are all quick_thinking_llm
bull_researcher.memory.get_memories < memory.client.embeddings.create < model: text-embedding-3-small
select model < utils
portfolio manager (final) < trading_graph.process_signal < signal_processing.py
market_analyst.tools.get_indicators < news_data_tools | technical_indicators_tools < interface.route_to_vendor < category = interface.TOOLS_CATEGORIES (e.g.'news_data'); method = interface.TOOLS_CATEGORIES.tools (e.g. 'get_global_news'); interface.VENDOR_METHODS
