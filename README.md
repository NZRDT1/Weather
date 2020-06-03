# Weather
Enviro+ python all except PM, feeds to adafruit.io

Python script for linking the data displayed by the Enviro+ phat from Pimoroni to the free adafruit.io dashboard. 

To install and run:
1. git clone https://github.com/NZRDT1/Weather.git
2. cd Weather
3. python3 senddata.py

You will need to edit senddata.py in a editor and enter your adafruit IO key and username. 
If you want to change the text on the display replace the text "Dashboard URL"

Required hardware/accounts:
Buy the phat here: https://shop.pimoroni.com/products/enviro?variant=31155658457171
Set up your free adafruit.io account here: https://io.adafruit.com/

Required additonal software: 
1. git clone https://github.com/pimoroni/enviroplus-python
2. cd enviroplus-python
3. sudo ./install.sh
4. pip3 install adafruit-io
5. sudo apt install python3
