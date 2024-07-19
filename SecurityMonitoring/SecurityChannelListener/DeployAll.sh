#!/bin/bash
START=$(date +%s)
rm -r /tmp/SecurityMonitoring/*
ansible-playbook /home/agorbov/SecurityMonitoring/SecurityChannelListener/FetchScriptFromWorkplace.yml
ansible-playbook /home/agorbov/SecurityMonitoring/SecurityChannelListener/BuildArtifact.yml
cd /tmp/SecurityMonitoring/
zip -r SecurityChannelListener.zip SecurityChannelListener
ansible-playbook /home/agorbov/SecurityMonitoring/SecurityChannelListener/UploadToLinuxDeploymentRepos.yml
ansible-playbook /home/agorbov/SecurityMonitoring/SecurityChannelListener/UploadToWinDeploymentRepos.yml
rm -r /tmp/SecurityMonitoring/*
python3.9 /home/agorbov/SecurityMonitoring/SecurityChannelListener/StopAllAllocs.py
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "AllDeployTime: $DIFF seconds"