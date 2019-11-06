#!/usr/bin/env bash

grep execute ../config/menu.xml | sed -n 's/^.*\<execute\>\(.*\)\<\/execute.*$/\1/p'
grep x-terminal-emulator ../config/menu.xml | sed -n 's/^.*\bash -c \\"\(.*\) .*/\1/p'
