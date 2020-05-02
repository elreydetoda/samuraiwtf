#!/usr/bin/env bash

scripts/util/template_alterations.py && time packer build -only=virtualbox-iso -var-file variables.json samurai.json |& tee build.log
