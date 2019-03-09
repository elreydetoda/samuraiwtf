#!/bin/bash

export JUICE_SHOP_PATH=$(find /opt/targets/ -name 'juice-shop_*')
cd $JUICE_SHOP_PATH
sudo npm start &
