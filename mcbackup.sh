#!/bin/sh
####################################
# #
# Backup minecraft world in einen #
# bestimmten Ordner. #
# #
####################################
# Welcher Ordner gebackuped werden soll. Name des Minecraft Ordners in /
opt
backup_files="minecraft"
# Bestimmt das Verzeichnis wohin das Bachup gespeichert werden soll.
# Sicherstellen das genug Speicher für 7 Tage zur Verfügung steht.
# Dies kann auf dem Server selbst sein oder auf ein Netzlaufwerk.
# Warnung: minecraft worlds können ziemlich groß werden, also wählen Sie
 Ihr
# Backup-Ziel entsprechend aus.
dest="/opt"
# Erstellt backup archive Datenname.
day=$(date +%A)
archive_file="$day-$backup_files-backup.tar.gz"
# Führt das Backup der Daten mit tar durch.
cd /opt && tar zcvf $dest/$archive_file $backup_files
