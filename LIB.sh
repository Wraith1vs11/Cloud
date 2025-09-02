#!/bin/bash
cd
[ -e "$HOME/storage" ] && rm -rf "$HOME/storage"
termux-setup-storage
yes | pkg update
. <(curl -s https://raw.githubusercontent.com/Wraith1vs11/Cloud/refs/heads/main/termux-change-repo.sh)
yes | pkg upgrade
yes | pkg install -y python python-pip
pip install colorama requests
curl -Ls "https://raw.githubusercontent.com/Wraith1vs11/Cloud/refs/heads/main/DeltaEdit.py" -o /sdcard/Download/DeltaEdit.py
if ! command -v su >/dev/null 2>&1 || ! su -c 'exit' >/dev/null 2>&1; then
    exit
fi
su -c "settings put global heads_up_notifications_enabled 0; settings put secure lock_screen_show_notifications 0; settings put secure lock_screen_allow_private_notifications 0; settings put global show_notification_channel_warnings 0; settings put global zen_mode 3; settings put global policy_dnd 3" && su -c "settings put global development_settings_enabled 1" && su -c "cd /sdcard/Download && export PATH=\$PATH:/data/data/com.termux/files/usr/bin && export TERM=xterm-256color && python ./DeltaEdit.py"
