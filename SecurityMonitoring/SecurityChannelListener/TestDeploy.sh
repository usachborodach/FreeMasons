#!/bin/bash
START=$(date +%s)
rm -r /tmp/SecurityMonitoring/*
ansible-playbook /home/agorbov/SecurityMonitoring/SecurityChannelListener/FetchScriptFromWorkplace.yml
ansible-playbook /home/agorbov/SecurityMonitoring/SecurityChannelListener/BuildArtifact.yml
cd /tmp/SecurityMonitoring/
zip -r SecurityChannelListener.zip SecurityChannelListener
ansible-playbook /home/agorbov/SecurityMonitoring/SecurityChannelListener/UploadToChelDeploymentRepo.yml
rm -r /tmp/SecurityMonitoring/*
python3.9 /home/agorbov/SecurityMonitoring/SecurityChannelListener/StopAllocChelLkps1.py
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "TestDeployTime: $DIFF seconds"