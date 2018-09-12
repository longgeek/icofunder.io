#!/bin/bash
cd /opt/icofunder/etc/ssl/
python acme_tiny.py --account-key ./account.key --csr ./domain.csr --acme-dir /var/www/challenges/ > ./signed.crt || exit
service nginx reload
