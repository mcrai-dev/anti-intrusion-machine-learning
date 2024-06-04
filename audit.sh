#!/bin/bash



# Exécution de  chkrootkit et enregistrement les résultats
sudo chkrootkit > /home/mcrai/Desktop/ENI/CyberSec/antispyware/autmation/log/chkrootkit.log

# Exécution de  lynis et enregistrement les résultats
sudo lynis audit system --logfile /home/mcrai/Desktop/ENI/CyberSec/antispyware/autmation/log/lynis.log

# Exécution de  rkhunter et enregistrement les résultats
sudo rkhunter --check --logfile /home/mcrai/Desktop/ENI/CyberSec/antispyware/autmation/log/rkhunter.log
