cd C:\ShuraRepo\Development\ReportsMonitoring\dataharvester
del dataharvester
del dataharvester.tar.gz
docker image rm dataharvester
docker image build -t dataharvester .
docker image save -o dataharvester dataharvester
tar -cvzf dataharvester.tar.gz dataharvester