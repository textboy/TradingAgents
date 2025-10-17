# TradingAgents/graph/signal_processing.py

from langchain_openai import ChatOpenAI


class SignalProcessor:
    """Processes trading signals to extract actionable decisions."""

    def __init__(self, quick_thinking_llm: ChatOpenAI):
        """Initialize with an LLM for processing."""
        self.quick_thinking_llm = quick_thinking_llm

    def process_signal(self, full_signal: str, company_name: str = None) -> str:
        """
        Process a full trading signal to extract the core decision.

        Args:
            full_signal: Complete trading signal text
            company_name: Name of the company (optional)
        Returns:
            Extracted decision (BUY, SELL, or HOLD)
        """
        messages = [
            (
                "system",
                f"""You are an efficient assistant designed to analyze paragraphs or financial reports provided by a group of analysts. Your task is to extract the investment decision,
Please extract the following information from the provided analysis report and return it in JSON format:

{{
    "company_name": {company_name},
    "action": "Buy/Hold/Sell",
    "target_price": Number (price, **must be a specific value, cannot be null**),
    "confidence": Number (between 0-1, or 0.7 if not explicitly stated),
    "risk_score": Number (between 0-1, or 0.5 if not explicitly stated),
    "reasoning": "Summary of the main reasons for the decision"
}}

without adding any additional text or information.""",
            ),
            ("human", full_signal),
        ]

        return self.quick_thinking_llm.invoke(messages).content
