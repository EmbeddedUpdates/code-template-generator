#!/bin/bash

# process_common_template.sh
# Called example:
#   process_common_template.sh -m Timer_RP2040
#
#   Generates a module specific c/h file for the give module
#   uses the rules from the provided module (e.g. /Timer_RP2040/Timer_RP2040.py)
#   That module is responsible for providing information like:
#       FileName            - Timer_RP2040.c/h
#       Function Prototypes - Std_ErrorCode Timer_RP2040_Init ( void );

INPUT_FILE_SOURCE=common_template_source.cog
INPUT_FILE_HEADER=common_template_header.cog

while getopts "m:p:" flag
do
    case "${flag}" in
        m) module=${OPTARG};;
        p) path_to_module=${OPTARG};;
    esac
done

if [ -f "$module.py" ]; then
    echo "$module exists"
    modulepy=$module.py
else
    if [ -f "$path_to_module/$module.py" ]; then
      echo "$path_to_module/$module.py exists"
      modulepy=$path_to_module
    else
        echo "$module does not exist"
        exit 0
    fi
fi

OUTPUT_FILE_SOURCE=out/$module.ctemplate
OUTPUT_FILE_HEADER=out/$module.htemplate

if [ ! -f $OUTPUT_FILE_SOURCE ]; then
    rm $OUTPUT_FILE_SOURCE
fi

if [ ! -f $OUTPUT_FILE_HEADER ]; then
    rm $OUTPUT_FILE_HEADER
fi

echo "cog $INPUT_FILE_SOURCE -D ADDPATH=$path_to_module -o $OUTPUT_FILE_SOURCE"
cog -d -D MODULE=$module -D ADDPATH=$path_to_module -o $OUTPUT_FILE_SOURCE $INPUT_FILE_SOURCE
echo "cog $INPUT_FILE_HEADER -D ADDPATH=$path_to_module -o $OUTPUT_FILE_HEADER"
cog -d -D MODULE=$module -D ADDPATH=$path_to_module -o $OUTPUT_FILE_HEADER $INPUT_FILE_HEADER 
