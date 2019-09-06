#!/bin/bash

sudo amazon-linux-extras install ansible2
git clone --depth=1 --single-branch --branch amazon-linux https://github.com/SamuraiWTF/samuraiwtf.git
cd samuraiwtf
ansible-playbook -K install/amazon-linux/samuraiwtf.yml

