#This is the configuration file for the server.It contains the configuration directives that give the server its instructions.
#config file with DocumentRoot,
#log file name,
#max simulateneous connections 4;
#Way to stop and restart the server.
#Way to stop the server by Ctrl + C on the Command line.
#and to restart the server we have not implemented it. It does not support to restart the server.
#log file format : %t(time) IP address of client, referring Url, method, portno
#Works on port 8080
import configparser
import parser

config = configparser.ConfigParser()
config.read('serverconfig.ini')
port = config.get('settings','PORT')
host = config.get('settings','HOST')
max = config.get('settings','MAX connections')
buffer_size = config.get('settings','Buffer size')
logfile_name = config.get('settings','logfile name')
config['settings'] = {
    'HOST': host,
    'PORT': port,
    'MAX connections' : max,
    'Buffer size': buffer_size,
    'logfile name': logfile_name,
}
with open('./serverconfig.ini', 'w') as f:
    config.write(f)

