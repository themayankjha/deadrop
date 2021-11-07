# Deadrop

Deploy your own Online deaddrops in seconds!

## Overview

A dead drop or dead letter box is a method of espionage tradecraft used to pass items or information between two individuals (e.g., a case officer and an agent, or two agents) using a secret location. By avoiding direct meetings, individuals can maintain operational security. This method stands in contrast to the live drop, so-called because two persons meet to exchange items or information.

Spies and their handlers have been known to perform dead drops using various techniques to hide items (such as money, secrets or instructions) and to signal that the drop has been made. Although the signal and location by necessity must be agreed upon in advance, the signal may or may not be located close to the dead drop itself. The operatives may not necessarily know one another or ever meet.

<img src="https://raw.githubusercontent.com/themayankjha/deadrop/main/img/logo.png" alt="logo" width="200"/>

## Installation

Getting your own deaddrop is very easy but make sure you have the following.

- A domain name where you can change the DNS records.
- A Server, I deployed mine using using Linode with Ubuntu 20.04 LTS.
- Some pixie magic and a bit of linux command line.

### Cloning and Setting Up

To Automate Setting up your deaddrop we will use the install script.

- Clone the Repo :- ``` git clone https://github.com/themayankjha/deadrop.git ```
- Change directory to the cloned folder :- ``` cd deadrop ```
- Make the script executable :- ``` chmod +x install.sh ```
- Run the script as root :- ```sudo ./install.sh```

### Enabling HTTPS

Enabling https is crucial as it helps us encrypt the traffic coming to and leaving the server as enyone else can easily snoop in and intercept our Dead Drops.
But we don't want that do we now?

- Use certbot to generate a SSL certificate :-
``` sudo certbot certonly --manual --manual-auth-hook /etc/letsencrypt/auth.py --preferred-challenges dns --debug-challenges -d \*.example.com -d example.com ```

Make sure to change example.com to your domain.
It will promt you to add a CNAME to your DNS. After Adding the Record Press Enter.
If it fails due just wait a few minutes and run the command again. It is likely due to dns replication timings.

- Make sure your port 443 is open and port 80 is closed:-

-- ```iptables -I INPUT -p tcp -m tcp --dport 443 -j ACCEPT```
-- ```iptables -I INPUT -p tcp -m tcp --dport 80 -j REJECT```

This will allow https requests to your server.

- Now add nginx configuration file ``` sudo nano /etc/nginx/conf.d/deadrop.conf ```

Make sure your configuration file looks like this :- <https://gist.githubusercontent.com/themayankjha/db4e67521d830ebae9c83ece0779ba0b/raw/85d8c1427b0847b8c96a00c63237520f1c9894b3/deadrop.conf>

and change example.com to your domain.

- restart nginx ``` sudo systemctl restart nginx ```

Violla your deaddrop is now live!

Goto your domain and exchange some deaddrops!

## How It Works

- The program starts a gunicorn webserver and makes it host a flask application on port 8081 which is not accessible.
- The nginx webserver acts as a reverse proxy so the requests made to it are forwarded to the gunicorn server.
- Certbot is used for generating SSL certificate that is used to enable ssl with nginx web server.
- The files uploaded are stored in /opt/deaddrop/deaddropname/static/uploads and can be easily transferred to different machine via scp.
- To take the deaddrop down, just copy your files and delete the server.

## License

License - [GNU GPL v3](LICENSE)
