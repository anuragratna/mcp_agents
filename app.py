"""
MCP Agents Main Application

This script serves as the main entry point for the MCP Agents platform, providing an interactive
chat interface that connects to various services including web browsing, stock data, and search capabilities.
It uses the Groq LLM for natural language processing and the MCP framework for agent interactions.
"""

import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os

async def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Configure Groq API key from environment variables
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    # Configuration file for browser and other settings
    config_file = "browser_mcp.json"
    
    print("Initializing Chat")
    
    # Initialize MCP client with configuration
    client = MCPClient.from_config_file(config_file)
    
    # Initialize the Groq language model using qwen-qwq-32b
    llm = ChatGroq(model="qwen-qwq-32b")
    
    # Create MCP agent with specified configurations
    agent = MCPAgent(
        llm=llm,          # Language model for processing
        client=client,    # MCP client for service interactions
        max_steps=15,     # Maximum number of steps per interaction
        memory_enabled=True,  # Enable conversation memory
    )
    
    # Display welcome message and usage instructions
    print("\n===== Interactive MCP Chat Terminal mode=====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("==================================\n")

    try:
        # Main chat loop for user interaction
        while True:
            # Get user input from terminal
            user_input = input("\nYou: ")

            # Handle exit commands
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            # Handle conversation history clearing
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            # Process user input and get agent response
            print("\nAssistant: ", end="", flush=True)

            try:
                # Execute agent with user input and get response
                # Memory handling is managed automatically by the agent
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                # Handle and display any errors that occur during processing
                print(f"\nErrorrrr: {e}")

    finally:
        # Cleanup: Ensure all browser sessions are properly closed
        if client and client.sessions:
            await client.close_all_sessions()
    
if __name__ == "__main__":
    # Run the async main function using asyncio
    asyncio.run(main())