[alerts.txt](https://github.com/user-attachments/files/29182571/alerts.txt)# Python Intrusion Detection System (IDS)
This project is a basic IDS written in Python. The script will analyze system log files, identify failed login attempts, and any other suspicious activity by looking for predefined patterns using (re).
The goal of this project is to demonstrate how Python can be used to perform a basic log analysis and detect potetial threats found in SSH  logs.

Features:
Reads and SSH log files
Identifies filed password attempts
Detects invalid user login attempts
Detects authentication failures
Detects failed connections
Displays Detected events in console
Generates and Alert.txt file to report findings

What You'll Need:
Python 3.3.14 (or other version)
Jupyter Notebook
Visual Studio Code (or VSCode alternative)

How to use:
Download from this repository
Open in chosen prerequesite
Run cells

To analyze real SSH logs:

1. locate the system auth log: ubuntu
(/var/log/auth.log)
:redhat/fedora
(/var/log/secure)
2. Modify the line:
logs = read_log("sample_log.txt")
To:
logs = read_log("/var/log/auth.log")
3. Run the Program

Project files:
[IDS_Project (1).ipynb](https://github.com/user-attachments/files/29182561/IDS_Project.1.ipynb)
[alerts.txt](https://github.com/user-attachments/files/29182590/alerts.txt)
[sample_log.txt](https://github.com/user-attachments/files/29182573/sample_log.txt)

Future Improvements:
1. Monitoring live SSH logs
2. Detecting Brute force login attempts
3. Extracting attacker IP addresses
4. Sending notification to user of suspicious activity


