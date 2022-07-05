#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$pytest_A = "pytest -m mva_ProcessPulseV14 --csv Report1.csv --csv-columns markers_with_args,function,status,duration"

Start-Process "cmd.exe"  "/k $pytest_A"
while (!(Test-Path ".\Report1.csv")){ Start-Sleep 20}

Import-Csv -Path '.\Report1.csv' | ForEach-Object {
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
}| ForEach-Object {
    
   #Write-Host $_.duration.GetType().FullName
    $_
}  | Export-Csv -Path '.\Report2.csv' -NoTypeInformation 


$csv = '.\Report2.csv'
(Get-Content $csv) -replace "markers", "id" |
    Set-Content '.\Report2.csv'
$csv = '.\Report2.csv'
(Get-Content $csv) -replace "function", "Description" |
    Set-Content '.\Report2.csv'
$csv = '.\Report2.csv'
(Get-Content $csv) -replace "status", "Result" |
    Set-Content '.\Report2.csv'
$csv = '.\Report2.csv'
(Get-Content $csv) -replace '"', "" |
    Set-Content '.\Report3.csv'
while (!(Test-Path ".\Report3.csv")){ Start-Sleep 20}

#quedo el push batoo




