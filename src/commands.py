import os

from prompt_file import PromptFile
from config import PromptConfig

def get_command_result(input: str, config: PromptConfig, context: PromptFile):
  """
  Checks if the input is a command and if so, executes it
  Currently supported commands:
  - show context
  - dump context
  - clear context
  - clear last context

  Returns: command result or "" if no command matched
  """
  # context file commands
  if input.__contains__("context"):
    # show context <n>
    if input.__contains__("show"):
      context.show()
      print('\n')
      return "context shown"
    
    # clear last context
    if input.__contains__("clear last"):
      # temporary saving deleted prompt file
      context.clear_last_interaction()
      return "cleared last interaction"
    
    # clear context
    if input.__contains__("clear"):
      context.clear()
      return "cleared context"
    
    # dump context
    if input.__contains__("dump"):
      context.dump()
      return "dump context"

  return ""