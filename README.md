# stega_project

## Requierment :

Python 3 with the following package :
 - PIL
 - cryptocode
 - wmi (on windows)


## Installation :

Linux :
```git clone https://github.com/4Pi-R2/stega_project.git```

Windows : Simply download the zip and unzip it.

## Usage :

Run the projet_stega.py script with a .jpg image in the stega_project folder.

#### low security :
  Code the text in the first bytes of the image, on the red, green or red part of each pixels
  
#### medium security :
  Code the text on random pixels (less identifiable)
  
#### High security :
  Change occurs on all the pixels, the text is coded using an algorithm started with a key and stored into a file named key.txt . 
  Moreover, this key is encoded using the processor id.
  The only way to decode is to use the same computer.
