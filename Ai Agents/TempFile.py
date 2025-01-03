
import os
import subprocess

# PowerShell script to delete temp files
powershell_script = '''
$ErrorActionPreference = 'SilentlyContinue'
Remove-Item -Path $env:TEMP\\* -Recurse -Force
Remove-Item -Path 'C:\\Windows\\Temp\\*' -Recurse -Force
'''

# Save the PowerShell script to a file
with open("delete_temp_files.ps1", "w") as file:
    file.write(powershell_script)

# Execute the PowerShell script
subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "delete_temp_files.ps1"])

