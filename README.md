Welcome to the Simulation of the Line Hitting Aggregation and External DLA!

### MASTER THESIS ###

Subject:	Fractal Dimension of Incremental Aggregations
Author: 	Tillmann Tristan Bosch
Professor: 	Steffen Winter
University: 	Institute of Technology, Karlsruhe (KIT)
Date:		09.03.2021


### HOW TO RUN THE SIMULATION ###

## SET PARAMETERS ##

open parameters.txt and enter values there. 

aggregation:			Enter "lha" to simulate the line hitting aggregation
                        	Enter "dla" to simulate external dla

cluster_size: 			Enter an integer to specify how big the cluster shall get. At the end the cluster will contain exactly cluster_size points. 

background_color:		Enter a color in HEX representation as a string
                        	Examples: 
                        	"ffffff" (white)
                        	"000000" (black)

particle_color:			Enter a list of colors in HEX representation as strings. If you enter more than one color into the list, with the next parameter
                        	color_generation_size you can specify after how many iterations the next color shall be used to render the particles. This will 
                        	create a color layering on the particles and gives an insight in which order the particles where added to the cluster. 
                        	Examples: 
                        	["ffffff"] (single color white)
                        	["000000"] (single color black)
                        	["2b1c8f", "cc0000"] (double color)
                        	["ffff00", "ff8000", "ff0000", "ff0080", "ff00ff", "8000ff", "0000ff", "0080ff", "00ffff", "00ff80", "00ff00", "80ff00"] 
				(rainbow palette)

color_generation_size:		Enter an integer which specifies after how many iterations the color of particles shall change. 
                        	This wont have any effect if you choose only one color in "particle_color". 

fractal_calculation_range:	Enter a list of this format: [a,b] with 0<a<b<1. The values a and b specify in which range the fractal dimension values 
				will be calculated. For more information read the mathematical paper. 

image_width:			Enter an integer to specify the pixel width of the image. 

image_height:			Enter an integer to specity the pixel height of the image. 


## INSTALL DEPENDENCIES AND RUN ##

You need to have Python (3.7.* or higher) installed. You furthermore need to be able to run a shell script. Open a shell like git bash and execute the following: 

#Change to the directory of this repo:
cd repo-directory

#install dependencies
pip install -r requirements.txt
(or pip3 install -r requirements.txt)

#run script
bash run.sh

PROBLEM WITH PYTHON:
If you have a problem running this, in run.sh you maybe have to replace "python" with "python3" or "py".

PROBLEM WITH PATHNAME SEPARATORS:
Depending on the system you are in, you might encounter a problem with the separator types in path names. In main.py we set the separator to "\\". You might have to change it to "/", "//" or "\". Look at a path name in your system, there you can see which separator your system uses. 


## OUTPUT ##

The appearing numbers in the shell let you know about how many iterations are finished already. In the simulation of "lha" the print "line missed cluster" indicates 
that a randomly chosen line according to the definitions in the paper missed the cluster and a new line had to be chosen. 

When calculation is over, you can find an image, a json file about cluster information and a json file containing the parameters in the exports folder.
The created filenames will have the following format:
{CURRENT SYSTEM TIME}__{FILE INFORMATION}__{LHA OR DLA}__{CLUSTER SIZE}.{PNG OR JSON}
Example:
2021_01_24_19_14_59__image__lha__5000.png
2021_01_24_19_14_59__information__lha__5000.json
2021_01_24_19_14_59__parameters__lha__5000.json
These three files where created at 2021_01_24_19_14_59 (format: year_month_day_hour_minute_second) after a simulation of lha using 5000 cluster points. 

The "2021_01_24_19_14_59__information__lha__5000.json" file contains some calculated values of the simulation.
In this file you will find the following information:

time:				the system time when the calculation of the process had finished (format: year_month_day_hour_minute_second)

runtime:			the running time of the calculation of the process on your machine in seconds

linear_reg_paramters:		linear regression parameters of the ansatz for the approximation of the fractal dimension, as described in the paper

last_fractal_dimension_value: 	last fractal dimension value (log(n)/log(radius of the cluster at n) if n is the number of particles)

volumina_ratio:			the empirical volume ratio of the cluster inside balls containg the cluster, as described in the paper

particles:			list of all particles 


## Enjoy the beautiful pictures and have fun! ## 
