import os
import time

from pathlib import Path
from config import PromptConfig

def count_tokens_approx(strings):
  count = 0
  for string in strings:
    count += len(string.split())
  return count


class PromptFile:
  current_context_file = ''
  token_count = 0
  config:PromptConfig
  messages = []

  def __init__(self, config: PromptConfig):
    self.current_context_file = os.path.join(os.path.dirname(__file__), "..", "current_context.txt")
    self.config = config
  

  def add_input_output_pair(self, user_query, prompt_response):
    newMessages = [
    {'role': 'user', 'content': user_query},
    {'role': 'assistant', 'content': prompt_response}]
    self.token_count += count_tokens_approx([user_query, prompt_response])
    self.messages.append(newMessages)
  
  
  def dump(self):
    with open(self.current_context_file, 'w') as f:
      for message in self.messages:
        f.write(message['role'] + ':' + message['content'])


  def show(self):
    for message in self.messages:
      print(message['role'] + ":" + message['content'])


  def clear_last_interaction(self):
    m1 = self.messages.pop()
    m2 = self.messages.pop()
    self.token_count -= count_tokens_approx([m1['content'], m2['content']])

  
  def init_context(self):
    self.messages = []    
    self.token_count = 0

    system_message = None
    if os.path.exists(self.config.system_prompt_file):
      with open(self.config.system_prompt_file, 'r') as f:
        lines = f.readlines()
        self.token_count = count_tokens_approx(lines)
      system_message={'role': 'system', 'content': ''.join(lines)}
      with open(self.current_context_file, 'w') as f:
        f.writelines(lines)
    if system_message:
      self.messages.append(system_message)

    if os.path.exists(self.config.examples_file):
      with open(self.config.examples_file, 'r') as f:
        lines = f.readlines()
      for line in lines:
        message = None
        if line.startswith('#'):
          message = {'role': 'user', 'content': line}
        elif len(line.strip()) > 0:
          message = {'role': 'assistant', 'content': line}
        if message:
          self.messages.append(message)
          self.token_count = count_tokens_approx(line)