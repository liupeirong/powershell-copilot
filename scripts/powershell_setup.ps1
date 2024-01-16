### 
# PowerShell script to setup Copilot for PowerShell
###
param
(
    [Parameter()]
    [System.IO.FileInfo]
    [ValidateScript( {
            if (-Not ($_ | Test-Path) ) {
                throw "Copilot folder does not exist." 
            }
            return $true
        })]
    [string]$RepoRoot = (Get-Location)
)

$plugInScriptPath = Join-Path $RepoRoot -ChildPath "scripts\powershell_plugin.ps1"
$copilotQueryPath = Join-Path $RepoRoot -ChildPath "src\main.py"

# The major version of PowerShell
$PSMajorVersion = $PSVersionTable.PSVersion.Major

# Create new PowerShell profile if doesn't exist. The profile type is for current user and current host.
# To learn more about PowerShell profile, please refer to 
# https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles
if (!(Test-Path -Path $PROFILE)) {
    New-Item -Type File -Path $PROFILE -Force 
} else {
    # Clean up the content before append new one. This allow users to setup multiple times without running cleanup script
    (Get-Content -Path $PROFILE -Raw) -replace "(?ms)### Copilot setup - start.*?### Copilot setup - end", "" | Set-Content -Path $PROFILE
    Write-Host "Removed previous setup script from $PROFILE."
}

# Add our plugin script into PowerShell profile. It involves these steps:
# 1. Read the plugin script content,
# 3. Add the plugin script to the content of PowerShell profile.
(Get-Content -Path $plugInScriptPath) -replace "{{copilot_query_path}}", $copilotQueryPath | Add-Content -Path $PROFILE
Write-Host "Added plugin setup to $PROFILE."

Write-Host -ForegroundColor Blue "Copilot PowerShell (v$PSMajorVersion) setup completed. Please open a new PowerShell session, type in # followed by your natural language command and hit Ctrl+G!"