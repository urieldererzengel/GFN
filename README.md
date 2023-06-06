# GFN
GFN-Homepage-Tools
#!/bin/bash
# Drop ICMP echo-request Nachrichten, welche über Broadcast oder
 Multicast Adressen gesendet werden
echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts
# Drop Quell-geroutete-Pakete
echo 0 > /proc/sys/net/ipv4/conf/all/accept_source_route
# Aktiviert den TCP-SYN-Cookie-Schutz vor SYN-Floods
echo 1 > /proc/sys/net/ipv4/tcp_syncookies
# Keine Akzeptierung von ICMP-Weiterleitungsnachrichten
echo 0 > /proc/sys/net/ipv4/conf/all/accept_redirects
# Keine Sendung von ICMP-Weiterleitungsnachrichten
echo 0 > /proc/sys/net/ipv4/conf/all/send_redirects
# Spoofing-Schutz der Quelladresse aktivieren
echo 1 > /proc/sys/net/ipv4/conf/all/rp_filter
# Pakete mit unmöglichen Quelladressen protokollieren
echo 1 > /proc/sys/net/ipv4/conf/all/log_martians
# Flush aller chains
/sbin/iptables --flush
# Unbegrenzten Datenverkehr auf der Loopback-Schnittstelle zulassen
/sbin/iptables -A INPUT -i lo -j ACCEPT
/sbin/iptables -A OUTPUT -o lo -j ACCEPT
# Standardrichtlinen setzen
/sbin/iptables --policy INPUT DROP
/sbin/iptables --policy OUTPUT DROP
/sbin/iptables --policy FORWARD DROP
# Zuvor initiierte und akzeptierte Austauschvorgänge umgehen die
 Regelprüfung
# Unbegrenzten ausgehenden Datenverkehr zulassen
/sbin/iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
/sbin/iptables -A OUTPUT -m state --state NEW,ESTABLISHED,RELATED -j
 ACCEPT
# Ratelimit SSH zum Schutz vor Angriffen
/sbin/iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent
 --update --seconds 60 --hitcount 4 -j DROP
/sbin/iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent
 --set
/sbin/iptables -A INPUT -p tcp --dport 22 -m state --state NEW -j ACCEPT
# Zulassen von bestimmten Ports, die von außen zugänglich sind
/sbin/iptables -A INPUT -p tcp --dport 25565 -m state --state NEW -j
 ACCEPT
#Minecraft
/sbin/iptables -A INPUT -p tcp --dport 8123 -m state --state NEW -j
 ACCEPT
#Dynmap plugin
# Andere Regeln für die zukünftige Verwendung, falls erforderlich.
 Entkommentiere zum Aktivieren
# /sbin/iptables -A INPUT -p tcp --dport 80 -m state --state NEW -j
 ACCEPT
# http
# /sbin/iptables -A INPUT -p tcp --dport 443 -m state --state NEW -j
 ACCEPT
# https
# UDP-Paketregel. Dies ist nur ein Beispiel, eine zufällige UDPPaketregel
# /sbin/iptables -A INPUT -p udp --dport 5021 -m state --state NEW -j
 ACCEPT
# Erlauben von Ping auf den Server
/sbin/iptables -A INPUT -p icmp --icmp-type 8 -m state --state
 NEW,ESTABLISHED,RELATED -j ACCEPT
 # Drop allen anderen Datenverkehr
/sbin/iptables -A INPUT -j DROP
# Druckt die aktivierten Regeln auf der Konsole aus, wenn das Skript
 abgeschlossen ist
/sbin/iptables -nL

##NEW

#!/bin/bash
/sbin/iptables -F
/sbin/iptables -X
/sbin/iptables -t nat -F
/sbin/iptables -t nat -X
/sbin/iptables -t mangle -F
/sbin/iptables -t mangle -X
# Die Regeln erlauben es, die Verbindung wiederherzustellen, indem der
 gesamten Datenverkehr geöffnet wird
/sbin/iptables -P INPUT ACCEPT
/sbin/iptables -P FORWARD ACCEPT
/sbin/iptables -P OUTPUT ACCEPT
# Druckt alle Regeln auf der Konsole aus, nachdem diese Datei ausgeführt
 wurde
/sbin/iptables -nL


##NEW2
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
