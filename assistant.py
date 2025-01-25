from typing import Optional
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.tools.youtube_tools import YouTubeTools
from phi.tools.calculator import Calculator
from phi.tools.newspaper4k import Newspaper4k
from phi.playground import Playground, serve_playground_app
from phi.assistant import Assistant
from dotenv import load_dotenv
import typer


# Load environment variables
load_dotenv()

# Configuration
MODEL_ID = "gpt-4o"

def create_specialist(
    name: str,
    role: str,
    tools: list,
    instructions: Optional[list] = None,
    add_sources: bool = False,
    add_tables: bool = False,
) -> Assistant:
    """Factory function to create specialized assistants"""
    base_instructions = [
        "Maintain professional tone",
        "Verify information accuracy",
        "Provide clear explanations"
    ]
    
    if add_sources:
        base_instructions.append("Always cite sources with URLs")
    if add_tables:
        base_instructions.append("Use markdown tables for structured data")
    
    if instructions:
        base_instructions.extend(instructions)
    
    return Assistant(
        name=name,
        role=role,
        model=OpenAIChat(model=MODEL_ID),
        tools=tools,
        instructions=base_instructions,
        show_tool_calls=True,
        markdown=True,
    )

def create_finance_expert() -> Assistant:
    return create_specialist(
        name="Financial Analyst",
        role="Handle financial data and market analysis",
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                company_news=True,
                technical_indicators=True
            )
        ],
        instructions=[
            "Calculate valuations using DCF models",
            "Compare industry multiples",
            "Analyze financial statements"
        ],
        add_sources=True,
        add_tables=True
    )

def create_research_agent() -> Assistant:
    return create_specialist(
        name="Research Specialist",
        role="Conduct web research and data gathering",
        tools=[DuckDuckGo()],
        instructions=[
            "Verify source credibility",
            "Cross-reference information",
            "Identify key trends"
        ],
        add_sources=True
    )

def create_operations_agent() -> Assistant:
    return create_specialist(
        name="Operations Manager",
        role="Handle calculations and logistics",
        tools=[Calculator()],
        instructions=[
            "Double-check calculations",
            "Optimize resource allocation",
            "Suggest efficiency improvements"
        ],
        add_tables=True
    )

def create_media_analyst() -> Assistant:
    return create_specialist(
        name="Media Analyst",
        role="Monitor news and video content",
        tools=[Newspaper4k(), YouTubeTools()],
        instructions=[
            "Summarize key points",
            "Analyze sentiment",
            "Verify facts"
        ],
        add_sources=True
    )

def main():
    """Run the executive assistant with all specialists"""
    executive_assistant = Assistant(
        name="AI Executive Assistant",
        role="Comprehensive personal and business support",
        model=OpenAIChat(model=MODEL_ID),
        team=[
            create_finance_expert(),
            create_research_agent(),
            create_operations_agent(),
            create_media_analyst()
        ],
        instructions=[
            "Coordinate between specialists",
            "Maintain consistent tone",
            "Synthesize information",
            "Provide actionable recommendations"
        ],
        markdown=True,
    )
    
    # Start interactive session
    print("Starting AI Assistant. Type 'exit' to quit.\n")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            executive_assistant.print_response(user_input, stream=True)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    typer.run(main)