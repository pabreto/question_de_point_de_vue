#!/bin/bash

f="list_cubes.csv"

 zmax=$(cat list_cubes.csv | cut -f3 -d"," | grep -v -  | sort | tail -1)
 ymin=$(cat list_cubes.csv | cut -f2 -d"," | sort -r | tail -5 | head -1)
xmin=$(cat list_cubes.csv | cut -f1 -d"," | grep - | sort | tail -1)
 xmax=$(cat list_cubes.csv | cut -f1 -d"," | grep -v - | sort | tail -1)
zmin=$(cat list_cubes.csv | cut -f3 -d"," | grep  -  | sort | tail -1)

ymax=$(cat list_cubes.csv | cut -f2 -d"," | sort | tail -5 | head -1)

echo "x:" $xmin $xmax "y:" $ymin $ymax "z:" $zmin $zmax
