# Python Defanger Tool by Melisa Nyamukondiwa

This is a simple tool which defangs ips/subnets and urls:

        192.168.1.1/21 turns into 192.168.1.1[/]
   
        https://example/tests/stats.com turns into hxxp://example/tests/stats[.]com 

The purpose of this tool is reduce the time when defanging malicious urls or ip addresses, saving valuable time. In addition, it allows for offline defanging, requiring little interaction from the user. 

There are no dependencies or external libraries needed, just the latest version of python 

How to use
1. Download defanger.py:
   ```
   git https://github.com/cyberwitch966/python_projects/blob/db7924b7a2057a2416958f6d40ab73126e55f486/defangertool/defanger.py
   
3. Open your command prompt/shell and navigate to the directory you saved it
4. Use the command:
   ```bash
   python3 defanger.py
and run it (or the version of python you have installed e.g python defanger.py}

5. How to use if you want to defang an ip address:
   ```bash
   Do you want to defang an ip or url? (I/U): I
Next you will input the ip adress:
   
    Enter the ip address: 172.81.44.11
Then you get your result
   
    Normal: 172.81.44.11
    Defanged: 172[.]81[.]44[.]11
   
6. Start over from step 4 to a defang a url or another ip address. If you wish, you can parse multiple ip addresses and urls by entering a list.

Now go on and try it! 

Use this tool responsibily and ethically please and thank you!
If you have any feedback or questions feel free to let me know!
