#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$pytest_A = "pytest -m mva_ProcessPulseV14 --csv Report1.csv --csv-columns markers_with_args,status,message,duration"



#Executing the Python 3.7.8 version into the VM

Start-Process "cmd.exe"  "/k $pytest_A"
while (!(Test-Path "C:\p4\MVA-API-Test\Report1.csv")){ Start-Sleep 20}

Import-Csv -Path 'C:\p4\MVA-API-Test\Report1.csv' | ForEach-Object {
    If ($_.status -eq 'failed') {
        $_.status = 'Fail'
    }
    $_
} | ForEach-Object {
    If ($_.status -eq 'passed') {
        $_.status = 'Pass'
    }
    $_
} | ForEach-Object {
    
    If (-not($_.markers -eq $null)) {
        $_.markers = $_.markers.trim('mva_ProcessPulseV14,vsts')
    }
    $_
}  | ForEach-Object {
    
    Write-Debug $_.duration
    $_
} | Export-Csv -Path 'C:\p4\MVA-API-Test\Report2.csv' -NoTypeInformation 


$csv = 'C:\p4\MVA-API-Test\Report2.csv'
(Get-Content $csv) -replace '"', '' |
    Set-Content $csv

$csv = 'C:\p4\MVA-API-Test\Report2.csv'
(Get-Content $csv) -replace '`r', '' |
    Set-Content $csv

#quedo el push batoo







#$csvfile |ForEach-Object{$_.markers = $_.markers.Trim("mva_ProcessPulseV14,vsts")}
Write-Host "Done"