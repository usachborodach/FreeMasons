cd C:\ShuraRepo\Development\ReportsMonitoring
call dataharvester\BuildImage.bat
cd C:\ShuraRepo\Development\ReportsMonitoring
call dataharvester\DeliverTest.bat
cd C:\ShuraRepo\Development\ReportsMonitoring
nomad job stop --purge --address=http://10.11.21.99:4646 ReportsMonitoring
timeout 1
nomad job run --detach --address=http://10.11.21.99:4646 nomadscripts/chelyabinsk.hcl
start http://10.11.21.99:4646/ui/jobs/ReportsMonitoring