cd Desktop/CommuterClock/
echo "Waiting 30 seconds to ensure internet is connected"
sleep 30
ping -q -c1 google.com &>/dev/null && echo online || echo offline
sudo python3 main.py
read -p "press return to close window"
