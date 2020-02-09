
## Simple python password generator

pswrdgen is a simple password generator that accepts command line argument as its input:
 
 - l : lowercase 
 - u : uppercase 
 - s : symbols
 - n : numbers to be included.

After the options a single or multiple integers may be given, and the 
script will generate passwords with the appropriate lenghts, such as 

```python 
pswrdgen.py -lu 20 10 
```

will generate 2 passwords with only lowercase and uppercase characters 
and in lenght of 20 and 10.



##Dockerfile

Included is a Dockerfile for building a container with the script inside. 
To build the image use 

```bash
docker build -t passwordgen .
```

Then to run it with all options enabled and length of 15

```bash
docker run passwordgen -luns 15
```
 




