#!/bin/bash

# Path to the directory containing the CER files
cer_dir=/home/$USER/xml2json/py

# Path to the keystore file
keystore_file=//home/$USER/xml2json/cacerts

# Password for the keystore
keystore_password=changeit

# Alias prefix for the certificates
alias_prefix=certificate

# Loop through each CER file in the directory and import it into the keystore
for cer_file in $cer_dir/*.cer; do
    # Extract the alias from the filename
    alias=$(basename "${cer_file%.cer}")

    # Import the certificate into the keystore
    keytool -importcert -noprompt -trustcacerts -alias "$alias_prefix-$alias" -file "$cer_file" -keystore "$keystore_file" -storepass "$keystore_password"
done
