#!/usr/bin/env bash

set -exuo pipefail

sudo apt install -y python3-pip dirmngr

sudo pip3 install -U pip

sudo pip3 install ansible
