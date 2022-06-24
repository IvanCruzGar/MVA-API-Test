#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
$setup = "C:\p4\API_APM_Insights.git\setup.py"
$python= "C:\Users\administrator\AppData\Local\Programs\Python\Python37\python.exe"
$virtual_env = "C:\p4\API_APM_Insights.git\test\Scripts\activate.bat"
$envA_api = "C:\p4\API_APM_Insights.git\envA.bat"
$envB_api = "C:\p4\API_APM_Insights.git\envB.bat"
$pytest_A = "pytest -m mva_ProcessPulseV14 --csv Report1.csv --csv-columns markers_with_args,status,message,duration"
$pytest_B = "pytest -m mtellapm --csv Report2.csv --csv-columns id,status,message,duration"
$reporte = 'python "Reportecsv.py"'


#Executing the Python 3.7.8 version into the VM

Start-Process "cmd.exe"  "/k $pytest_A"
while (!(Test-Path "C:\MVA API Test\Report1.csv")){ Start-Sleep 20}

Import-Csv -Path 'C:\MVA API Test\Report1.csv' | ForEach-Object {
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
} | ForEach-Object {
    If (-not($_.duration -eq $null)) {
        $_.duration = $_.duration.trim('\n')
    }
    $_
}  | Export-Csv -Path 'C:\MVA API Test\Report2.csv' -NoTypeInformation 












#$csvfile |ForEach-Object{$_.markers = $_.markers.Trim("mva_ProcessPulseV14,vsts")}
Write-Host "Done"