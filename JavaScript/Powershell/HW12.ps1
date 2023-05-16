$date = Get-Date

write-host "hi todays date is $($date.tostring('dddd, MMMM, dd, yyyy'))"

$processName = "notepad"
$process = Get-Process $processName -ErrorAction SilentlyContinue

pause

if ($process) {
    Write-Host "Stopping process $processName..."
    Stop-Process -Id $process.Id -Force
    Write-Host "Process $processName stopped."
}
else {
    Write-Host "Process $processName is not running."
}

pause

$file = "C:\Program Files\Mozilla Firefox\firefox.exe"

if (Test-Path $file) {
    Write-Host "File $file exists."
}
else {
    Write-Host "File $file does not exist."
}

pause

$vpnConnectionName = "My VPN Connection"
$vpnServerAddress = "vpn.example.com"

Add-VpnConnection -Name $vpnConnectionName -ServerAddress $vpnServerAddress -TunnelType "SSTP" -EncryptionLevel "Required" -AuthenticationMethod MSChapv2 -SplitTunneling $false -RememberCredential -PassThru
