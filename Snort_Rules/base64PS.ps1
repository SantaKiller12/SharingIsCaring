$bytes = [System.IO.File]::ReadAllBytes("C:\path\to\input.txt")
$base64 = [System.Convert]::ToBase64String($bytes)
$base64 | Set-Content -Path "C:\path\to\output.txt"