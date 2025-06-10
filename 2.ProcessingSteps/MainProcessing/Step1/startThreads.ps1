# For each .py file, create a PowerShell instance, activate the .venv, and run the Python file
$threads = 29
for ($i = 0; $i -lt $threads; $i++) {
    Write-Host "Starting thread $i"
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "C:\Users\Mariana\Documents\Python\.venv\Scripts\Activate.ps1; Python C:\Users\Mariana\Documents\Python\steps\step1\start_thread.py $i"
}
