# Full-auto-sorting-v1.1
Automatic sorting app



Schedule your script powershell :

:> $action = New-ScheduledTaskAction -Execute "python.exe" -Argument "C:\Users\nmkoninn\source\repos\PythonApplication4\Sorting "
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 9:00AM
$principal = New-ScheduledTaskPrincipal -UserId "NT AUTHORITY\SYSTEM" -RunLevel Highest
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "Sort" -Principal $principal 

You will need to define the path of the .py on your machine


OR 
![description](https://github.com/user-attachments/assets/2d972831-75d6-4a81-a868-47b07e83c7bc)
