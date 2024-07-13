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

while getopts m: flag
do
    case "${flag}" in
        m) module=${OPTARG};;
    esac
done

if [ -f "$module.py" ]; then
    echo "$module exists"
else
    echo "$module does not exist"
    exit 0
fi

OUTPUT_FILE_SOURCE=out/$module.ctemplate
OUTPUT_FILE_HEADER=out/$module.htemplate

if [ ! -f $OUTPUT_FILE_SOURCE ]; then
    rm $OUTPUT_FILE_SOURCE
fi

if [ ! -f $OUTPUT_FILE_HEADER ]; then
    rm $OUTPUT_FILE_HEADER
fi

echo "cog $INPUT_FILE_SOURCE -o $OUTPUT_FILE_SOURCE"
cog -d -D MODULE=$module -o $OUTPUT_FILE_SOURCE $INPUT_FILE_SOURCE
echo "cog $INPUT_FILE_HEADER -o $OUTPUT_FILE_HEADER"
cog -d -D MODULE=$module -o $OUTPUT_FILE_HEADER $INPUT_FILE_HEADER 
