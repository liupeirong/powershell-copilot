
import os
import configparser
from pathlib import Path

class PromptConfig:
    openai={}
    deployment=''
    temperature=0
    max_tokens=300
    system_prompt_file=''
    example_file=''

    def __init__(self):
        config = configparser.ConfigParser()
        config_ini = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "config.ini")
        config.read(config_ini)

        self.openai = {
            'api_type': 'azure',
            'api_base': config['openai']['api_base'].strip('"').strip("'"),
            'api_key': os.getenv("AZURE_OPENAI_API_KEY"),
            'api_version': config['openai']['api_version'].strip('"').strip("'")
        }
        self.deployment = config['openai']['deployment'].strip('"').strip("'")
        self.temperature = float(config['model']['temperature'].strip('"').strip("'"))
        self.max_tokens = int(config['model']['max_tokens'].strip('"').strip("'"))
        self.system_prompt_file = Path(os.path.join(os.path.dirname(__file__), "..", "contexts", "system_prompt.txt"))
        self.examples_file = Path(os.path.join(os.path.dirname(__file__), "..", "contexts", "examples.txt"))
