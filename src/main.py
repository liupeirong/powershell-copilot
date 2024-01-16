#!/usr/bin/env python
# -*- coding: utf-8 -*-

from openai import AzureOpenAI
import sys

from prompt_file import PromptFile
from config import PromptConfig
from commands import get_command_result


if __name__ == '__main__':
    try:
        config = PromptConfig()
        api_version, deployment = config.openai['api_version'], config.deployment
        aoai = AzureOpenAI(api_version=api_version, api_key=config.openai['api_key'],
                           azure_endpoint=config.openai['api_base'], azure_deployment=deployment)

        prompt_file = PromptFile(config)
        prompt_file.init_context()

        user_input = sys.stdin.readline()

        command_result = get_command_result(user_input, config, prompt_file)
        if command_result != "": # executed the command, must restart shell
            print("# Command completed.")
            sys.exit(0)

        user_message = {'role': 'user', 'content': user_input}
        prompt_file.messages.append(user_message)
        response = aoai.chat.completions.create(model=config.deployment, messages=prompt_file.messages, temperature=config.temperature, top_p=1, max_tokens=config.max_tokens, stop="#")
        if response.choices[0].finish_reason == 'stop':
          completion_all = response.choices[0].message.content
          print(completion_all)
        else:
          print("# error: terminated pre-maturely.")

    except Exception as e:
        print('\n\n# Copilot error: Unexpected exception - ' + str(e))
