# Weather
Enviro+ python all except PM, feeds to adafruit.io

Python script for linking the data displayed by the Enviro+ phat from Pimoroni to the free adafruit.io dashboard. 

To install and run:
- git clone https://github.com/NZRDT1/Weather.git
- cd Weather
- python3 senddata.py

You will need to edit senddata.py in a editor and enter your adafruit IO key and username. 
If you want to change the text on the display replace the text "Dashboard URL"

Required hardware/accounts:
- Buy the phat here: https://shop.pimoroni.com/products/enviro?variant=31155658457171
- Set up your free adafruit.io account here: https://io.adafruit.com/

Required additonal software: 
- git clone https://github.com/pimoroni/enviroplus-python
- cd enviroplus-python
- sudo ./install.sh
- pip3 install adafruit-io
- sudo apt install python3
