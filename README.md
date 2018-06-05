# forza_motorsport
Various utilities to work with data from the Forza Motorsport game's data stream.

## fdp.py
A Python class containing all properties available in the data packets sent by the game's "data out" stream.

## data2tsv.py
A script that will listen on a given port on the local machine and write any incoming packets to a given TSV file whenever the game is in a "race" state. The script runs until it is interrupted (e.g. by the Ctrl-C keyboard combination).

### TSV output example

Say that we want to store our data in a file called `forza_data.tsv`. We can start the Python script as follows, where it will listen on port 1123 and write to the file we want:

```
python data2tsv.py 1123 forza_data.tsv
```

Next, you will have to go into the HUD options in the game and at the bottom set "data out" to "ON", the "data out IP address" to the IP address of your machine (how to find that depends on your system, refer to your user manual), and the "data out IP port" to 1123.

Once you're in a race the script will start writing data to the TSV. To stop the script, hit Ctrl-C.
