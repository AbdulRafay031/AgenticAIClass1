    #    {   Agent Level And Runner Level   }

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

gemini_api_key = "AIzaSyDYoUbMPegc3MUmm0RUGRB4bBhFfkVl1ww"

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

Friends = Agent(
    name = "Friends",
    instructions = "you are my asistant for helping me."
)

result = Runner.run_sync(Friends,"how are you", run_config=config)
print(result.final_output)


#       {  Global Level  }

from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

gemini_api_key = "AIzaSyDYoUbMPegc3MUmm0RUGRB4bBhFfkVl1ww"
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

Friends = Agent(
    name = "Assistant",
    instructions = "You are my assistant for helping me",
     model="gemini-2.0-flash" 
)

result = Runner.run_sync(Friends,"Hello how are you")
print(result.final_output)

