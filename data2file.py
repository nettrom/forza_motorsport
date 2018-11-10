#!/usr/env/python
# -*- coding: utf-8 -*-
'''
Script to listen on a given port for UDP packets sent by a Forza Motorsport 7
"data out" stream and write the data to a TSV file.

Copyright (c) 2018 Morten Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import csv
import logging
import socket

import yaml
import datetime as dt

from fdp import ForzaDataPacket

def to_str(value):
    '''
    Returns a string representation of the given value, if it's a floating
    number, format it.

    :param value: the value to format
    '''
    if isinstance(value, float):
        return('{:f}'.format(value))

    return('{}'.format(value))

def dump_stream(port, output_filename, format='tsv',
                append=False, packet_format='dash', config_file = None):
    '''
    Opens the given output filename, listens to UDP packets on the given port
    and writes data to the file.

    :param port: listening port number
    :type port: int

    :param output_filename: path to the file we will write to
    :type output_filename: str

    :param format: what format to write out, either 'tsv' or 'csv'
    :type format: str

    :param append: if set, the output file will be opened for appending and
                   the header with column names is not written out
    :type append: bool

    :param packet_format: the packet format sent by the game, one of either
                          'sled' or 'dash'
    :type packet_format str

    :param config_file: path to the YAML configuration file
    :type config_file: str
    '''

    if config_file:
        import yaml
        with open(config_file) as f:
            config = yaml.safe_load(f)

        ## The configuration can override everything
        if 'port' in config:
            port = config['port']

        if 'output_filename' in config:
            output_filename = config['output_filename']

        if 'format' in config:
            format = config['format']

        if 'append' in config:
            append = config['append']

        if 'packet_format' in config:
            packet_format = config['packet_format']

    params = ForzaDataPacket.get_props(packet_format = packet_format)
    if config_file and 'parameter_list' in config:
        params = config['parameter_list']

    log_wall_clock = False
    if 'wall_clock' in params:
        log_wall_clock = True

    open_mode = 'w'
    if append:
        open_mode = 'a'

    with open(output_filename, open_mode, buffering=1) as outfile:
        if format == 'csv':
            csv_writer = csv.writer(outfile)
            if not append:
                csv_writer.writerow(params)

        ## If we're not appending, add a header row:
        if format == 'tsv' and not append:
            outfile.write('\t'.join(params))
            outfile.write('\n')
                
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('', port))

        logging.info('listening on port {}'.format(port))

        n_packets = 0
        
        while True:
            message, address = server_socket.recvfrom(1024)
            fdp = ForzaDataPacket(message, packet_format = packet_format)
            if log_wall_clock:
                fdp.wall_clock = dt.datetime.now()

            if fdp.is_race_on:
                if n_packets == 0:
                    logging.info('{}: in race, logging data'.format(dt.datetime.now()))
                
                if format == 'csv':
                    csv_writer.writerow(fdp.to_list(params))
                else:
                    outfile.write('\t'.join([to_str(v) \
                                             for v in fdp.to_list(params)]))
                    outfile.write('\n')

                n_packets += 1
                if n_packets % 60 == 0:
                    logging.info('{}: logged {} packets'.format(dt.datetime.now(), n_packets))
            else:
                if n_packets > 0:
                    logging.info('{}: out of race, stopped logging data'.format(dt.datetime.now()))
                n_packets = 0

def main():
    import argparse

    cli_parser = argparse.ArgumentParser(
        description="script that grabs data from a Forza Motorsport stream and dumps it to a TSV file"
    )

    # Verbosity option
    cli_parser.add_argument('-v', '--verbose', action='store_true',
                            help='write informational output')

    cli_parser.add_argument('-a', '--append', action='store_true',
                            default=False, help='if set, data will be appended to the given file')

    cli_parser.add_argument('-f', '--format', type=str, default='tsv',
                            choices=['tsv', 'csv'],
                            help='what format to write out, "tsv" means tab-separated, "csv" comma-separated; default is "tsv"')

    cli_parser.add_argument('-p', '--packet_format', type=str, default='dash',
                            choices=['sled', 'dash'],
                            help='what format the packets coming from the game is, either "sled" or "dash"')

    cli_parser.add_argument('-c', '--config_file', type=str,
                            help='path to the YAML configuration file')

    cli_parser.add_argument('port', type=int,
                            help='port number to listen on')

    cli_parser.add_argument('output_filename', type=str,
                            help='path to the TSV file we will output')

    args = cli_parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    dump_stream(args.port, args.output_filename, args.format, args.append,
                args.packet_format, args.config_file)

    return()

if __name__ == "__main__":
    main()
    
