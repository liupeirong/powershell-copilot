# Introduction

This is a command line tool that lets you type in natural language and generates PowerShell commands which you can decide to run.
It's inspired by [the Codex Cli sample](https://github.com/microsoft/Codex-CLI/tree/main) and has been refactored
 from deprecated Codex models to GPT models with chat completion APIs.

## How to set it up?

You only need to set it up once.

1. Open PowerShell as an administrator, and run the following command:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. Clone this repo to your machine, to a folder <REPO_ROOT>.
3. Run the following command in <REPO_ROOT>:

```powershell
.\scripts\powershell_setup.ps1
```

4. Edit <REPO_ROOT>\config.ini to put in your Azure OpenAI configuration.
5. Set an environment variable called `AZURE_OPENAI_API_KEY` at each start up of your PowerShell $PROFILE.
6. Install Python 3.8+.
7. Run the following command in <REPO_ROOT>:

```bash
pip install -r .\requirements.txt
```

## How to run?

1. Open a new PowerShell console.
1. Type in `#` followed by your question in natural language in one line. Hit `Ctrl + g` when you are done.

If there's no error, Azure OpenAI will generate a PowerShell command. If you like the command, hit enter to run it.
 Otherwise hit `Ctrl + C` to quit.

## How to customize?

1. You can customize system prompt in `<REPO_ROOT>\contexts\system_prompt.txt`.
1. You can customize few-shot examples in `<REPO_ROOT>\contexts\examples.txt`.

## Limitations

1. Chat history is not yet implemented.