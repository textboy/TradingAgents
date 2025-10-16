# execution
(update API key in .env)
conda activate tradingcn
python -m cli.main
python unit_test.py

# git update
git add .
git commit -m "xxx"
git push origin mk

# coding trace
TradingAgentsGraph < trading_graph."Initialize LLMs" + trading_graph.setup_graph < setup.create_social_media_analyst < social_media_analyst
in setup.py, only create_research_manager & create_risk_manager use deep_thinking_llm, others are all quick_thinking_llm
bull_researcher.memory.get_memories < memory.client.embeddings.create < model: text-embedding-3-small