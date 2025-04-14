import asyncio
import os
from agents import Agent, ModelSettings, function_tool, Runner
from dotenv import load_dotenv
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in .env file")
async def main():
    agent = Agent(
        name="Math Tutor",
        instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
    )
    result = await Runner.run(agent,"what is algebra.",)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())