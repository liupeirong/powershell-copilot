### 
# PowerShell script to clean up the Copilot settings for PowerShell
#
# File/Content to be removed:
# 1. PowerShell profile (Remove file if the content only has Copilot setup; otherwise, wipe the Copilot setup content)
# 2. OpenAI configuration file (openai_config)
###
$RepoRoot = (Get-Location)

function CleanUpProfileContent() 
{
    if (Test-Path -Path $PROFILE) {
        # RegEx match setup code, replace with empty string.
        (Get-Content -Path $PROFILE -Raw) -replace "(?ms)### Copilot setup - start.*?### Copilot setup - end", "" | Set-Content -Path $PROFILE

        # Delete the file if its content is empty
        if ([String]::IsNullOrWhiteSpace((Get-Content -Path $PROFILE))) {
            Remove-Item $PROFILE
            Write-Host "Removed $PROFILE"
        }
    }
}

CleanUpProfileContent

Write-Host -ForegroundColor Blue "Copilot PowerShell clean up completed. Please close this PowerShell session."