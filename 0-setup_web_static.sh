#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static.

# Installing and updating Nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Will create folders if they don't already exist in the servers
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Creates a fake HTML File (with Simple content)
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Creates a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Giving ownership 
sudo chown -R ubuntu:ubuntu /data/

# Updating Nginx configuration
sudo sed -i 's|listen 80 default_server;|listen 80 default_server;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n|' /etc/nginx/sites-enabled/default

sudo service nginx restart
