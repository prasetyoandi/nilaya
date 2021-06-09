sudo apt-get update
sudo apt-get install flac
sudo pip3 install SpeechRecognition
sudo pip3 install requests
sudo pip3 install gtts
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
sudo apt-get install nodejs
sudo npm i -g pm2
sudo pm2 start main.py --interpreter="python3"
sudo pm2 startup
sudo pm2 save
sudo reboot