import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

def processResults(stringValues):
    skills_directory = "./skills"

    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()

    kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

    recommendation = kernel.import_semantic_skill_from_directory(skills_directory, "ChatGPT")

    ans = recommendation["recs"]

    inputStrings = ','.join(stringValues)
    resultJSON = ans(inputStrings)

    return resultJSON

