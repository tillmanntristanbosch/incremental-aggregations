# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:15:52 2021

@author: Tillmann Tristan Bosch
"""

#systemic imports
import json, shutil, os, time


import create_data as cd
import line_hitting_aggregation as lha
import external_dla as dla
    

if __name__ == "__main__":

    #choose your pathname separator (you can find it looking at pathnames in your system)
    #separator = "\\"
    separator = "/"
    
    #copy parameters.json into the library
    current_dir = os.getcwd()
    up_dir = os.path.dirname(current_dir)
    shutil.copyfile(up_dir + separator + "parameters.json", current_dir + separator + "parameters.json")
    
    #read parameters.json    
    with open("parameters.json") as json_file:
        data = json.load(json_file)
    
    #init process
    if data["aggregation"] == "lha":
        aggregation = lha.Line_Hitting_Aggregation()
    elif data["aggregation"] == "dla":
        aggregation = dla.External_DLA()
    else:
        raise Exception("Invalid aggregation parameter. Enter lha or dla.")
    
    #run process and capture running time
    begin_time = time.time()
    aggregation.run_process(data["cluster_size"] - 1)
    runtime = round(time.time() - begin_time, 2)
    print("runtime: " + str(runtime) + " seconds")
    
    #create and export data (image, information, parameters)
    cd.export_data(aggregation, data, separator, runtime)









