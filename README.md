# forza_motorsport
Various utilities to work with data from the Forza Motorsport and Forza Horizon games' data stream.

## fdp.py
A Python class containing all properties available in the data packets sent by the game's "data out" stream. This class supports packets for the original "sled" format in Forza Motorsport, the newer "dash cam" format, as well as the format in Forza Horizon 4.

## data2file.py
A script that will listen on a given port on the local machine and write any incoming packets to a given output file whenever the game is in a "race" state. The script runs until it is interrupted (e.g. by the Ctrl-C keyboard combination).

### TSV output example

Say that we want to store our data in a file called `forza_data.tsv`. We can start the Python script as follows, where it will listen on port 1123 and write to the file we want:

```
python data2file.py 1123 forza_data.tsv
```

Next, you will have to go into the HUD options in the game and at the bottom set "data out" to "ON", the "data out IP address" to the IP address of your machine (how to find that depends on your system, refer to your user manual), and the "data out IP port" to 1123.

Once you're in a race the script will start writing data to the TSV. To stop the script, hit Ctrl-C.

### File formats supported

The script supports writing out tab-separated or comma-separated values. Supply the `-f` or `--format` parameter to the script to control the format. It writes out tab-separated values by default.

Say you want to write out a comma-separated file to import into Excel, add the format parameter:

```
python data2file.py -f csv 1123 forza_data.csv
```

### Overwrite or append to the output file

By default the script will overwrite an existing file, and start the file by writing out a row with the names of all the data properties found in the data packets transmitted by the game. If you instead want to append data to an existing file, supply the `-a` parameter:

```
python data2file.py -a 1123 forza_data.tsv
```

When appending, the header row is not written out as it is expected to already be present in the file.

### Write output in the older "sled" format

By default the script expects data packets to use the current "dash cam" format of Forza Motorsport 7. However, we still support the first version of the data out feature, the so-called "sled" format. If you want to use that format, supply the `-p` parameter to the script with a value of "sled", like this:

```
python data2file.py -p sled 1123 forza_data.tsv
```

We also support the Forza Horizon 4 data format, which we've labelled "fh4":

```
python data2file.py -p fh4 1123 forza_data.tsv
```

### Specify a configuration file

The utility script can read in a YAML configuration file, which allows you to specify what data you want logged, rather than have it log all available data. If you want to use a configuration file, supply the `-c` parameter to the script, with a value of the name of the configuration file, for example:

```
python data2file.py -c example_configuration.yaml 1123 forza_data.tsv
```

For more information about the configuration file format and the possible options, see the [configuration file documentation](configuration_file.md).

### Command line help

If you want to know what command line parameters you can use with the script, start it with `-h`. The script will then output some helpful information and how it works.

### Contributions are welcome

If you know Python and wish to contribute code, please don't hesitate to submit a pull request! There are always ways to improve, be it adding features or fixing bugs.
