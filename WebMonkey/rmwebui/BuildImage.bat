cd C:\ShuraRepo\Development\ReportsMonitoring\rmwebui
del rmwebui
del rmwebui.tar.gz
docker image rm rmwebui
docker image build -t rmwebui .
docker image save -o rmwebui rmwebui
tar -cvzf rmwebui.tar.gz rmwebui