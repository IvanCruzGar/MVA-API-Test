#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
$setup = "C:\p4\API_APM_Insights.git\setup.py"
$python= "C:\Users\administrator\AppData\Local\Programs\Python\Python37\python.exe"
$virtual_env = "C:\p4\API_APM_Insights.git\test\Scripts\activate.bat"
$envA_api = "C:\p4\API_APM_Insights.git\envA.bat"
$envB_api = "C:\p4\API_APM_Insights.git\envB.bat"
$pytest_A = "pytest -m mtellapi --csv Report1.csv --csv-columns id,status,message,duration"
$pytest_B = "pytest -m mtellapm --csv Report2.csv --csv-columns id,status,message,duration"
$reporte = 'python "Reportecsv.py"'


#Executing the Python 3.7.8 version into the VM



if(Test-Path $python){
    Write-Host "Python 3.7.8 exist"


    python $setup install


}else{
Write-Host "Doesn't exist"

}

Start-Process "cmd.exe"  "/k $virtual_env && $envA_api && $pytest_A"
while (!(Test-Path "C:\p4\API_APM_Insights.git\Report1.csv")){ Start-Sleep 20}
Start-Process "cmd.exe"  "/k $virtual_env && $envB_api && $pytest_B"
while (!(Test-Path "C:\p4\API_APM_Insights.git\Report2.csv")){ Start-Sleep 20}
Start-Process "cmd.exe" "/k $reporte"
while (!(Test-Path "C:\p4\API_APM_Insights.git\Test_results.csv")){ Start-Sleep 20}

Write-Host "Done"


