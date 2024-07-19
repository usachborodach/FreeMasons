rm /tmp/antivorovator/*
ansible-playbook /home/agorbov/antivorovator/PullLogs/FetchLogsFromRemoteToController.yml
cd /tmp/antivorovator/
unzip "/tmp/antivorovator/*.zip"
rm /tmp/antivorovator/*.zip
zip ./files.zip ./*
ansible-playbook /home/agorbov/antivorovator/PullLogs/UploadArchiveFromControllerToWorkplace.yml
rm /tmp/antivorovator/*