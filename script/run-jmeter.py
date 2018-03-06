#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Vinícius Aires Barros'
__email__ = 'viniciusaires@usp.br'
__copyright__ = "Copyright 2017, University of São Paulo"

import os, sys, shutil, subprocess, platform, time
import datetime
from os.path import expanduser

def run(directory, commands):
    for cmd in commands:
        process = subprocess.Popen(cmd, cwd=directory, shell=True)
        process.wait()
        if (process.returncode != 0):
            msg = 'The command {} did not execute successfully, exit code:{}. Aborting....'.format(cmd, process.returncode)
            print (msg)
            sys.exit(process.returncode)

if __name__ == "__main__":

    '''
    Dicionário de Argumentos de Entrada
    1 = arquivo jmx (rest_api_get_uniform.jmx, rest_api_get_poisson.jmx, rest_api_get_gaussian.jmx)
    2 = número de repetições
    3 = hostname do servidor
    4 = porta do servidor
    5 = tipo do banco de dados (mysql, pgsql, mongo)
    6 = distribuição estatistica (uniform, poisson, gaussian)
    '''
    jmx = sys.argv[1]
    num_repeat = int(sys.argv[2])
    host = sys.argv[3]
    port_number = int(sys.argv[4])
    db_type = sys.argv[5]
    d_stat = sys.argv[6]
 
    user_dir = expanduser("~")
    hostname = platform.node()
    num_threads = [2000, 8000]
    format_type = ["json", "xml"]
    path_url = ["sensor?limit=1000&output_format=json", "sensor?limit=1000&output_format=xml"]
    default_path = "{}".format(os.getcwd())

    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Starting Experiment")
    print(start_time)

    #mkdir outout folders
    print("#create output forder directory")
    for type_f in format_type:
        cmd = "mkdir -p {}/{}/{}/{}".format(default_path, "output_report", hostname, type_f)
        print(cmd)
        run(user_dir, [cmd])

    #json test
    print("\n#json workload test:")
    for n_thread in num_threads:
        csv_file = "jmeter-report-{}-{}-{}-{}-{}-{}.csv".format(hostname, d_stat, n_thread, num_repeat, format_type[0], db_type)
        output_file = "{}/{}/{}/{}/{}".format(default_path, "output_report", hostname, format_type[0], csv_file)
        jmx_curr = "{}/{}".format(default_path, jmx)

        print("\nrun-jmeter")
        now = datetime.datetime.now()
        start_time = now.strftime("%Y-%m-%d %H:%M:%S")
        cmd = "$JMETER_HOME/bin/jmeter -n -t {} -l {} -JThread={} -JRepeat={} -JHost={} -JPort={} -JPath=\'{}\'".format(jmx_curr, output_file, n_thread, num_repeat, host, port_number, path_url[0])
        print(cmd)
        run(user_dir, [cmd])
        now = datetime.datetime.now()
        end_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(start_time + " " + end_time)
        #time.sleep(30)
        print("\n")

    print(20*"-")

    #xml test
    print("\n#xml workload test:")
    for n_thread in num_threads:
        csv_file = "jmeter-report-{}-{}-{}-{}-{}-{}.csv".format(hostname, d_stat, n_thread, num_repeat, format_type[1], db_type)
        output_file = "{}/{}/{}/{}/{}".format(default_path, "output_report", hostname, format_type[1], csv_file)
        jmx_curr = "{}/{}".format(default_path, jmx)
        
        print("\nrun-jmeter")
        now = datetime.datetime.now()
        start_time = now.strftime("%Y-%m-%d %H:%M:%S")
        cmd = "$JMETER_HOME/bin/jmeter -n -t {} -l {} -JThread={} -JRepeat={} -JHost={} -JPort={} -JPath=\'{}\'".format(jmx_curr, output_file, n_thread, num_repeat, host, port_number, path_url[1])
        print(cmd)
        run(user_dir, [cmd])
        now = datetime.datetime.now()
        end_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(start_time + " " + end_time)
        #time.sleep(30)
        print("\n")
