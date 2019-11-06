#!/usr/bin/env bats

source ./test_functions.sh

@test "dojo-basic.wtf has hosts entry for 127.0.0.1" {
  checkHostEntry dojo-basic.wtf
}

@test "dojo-basic.wtf is listening" {
  checkHostUp dojo-basic.wtf
}

@test "dojo-scavenger.wtf has hosts entry for 127.0.0.1" {
  checkHostEntry dojo-scavenger.wtf
}

@test "dojo-scavenger.wtf is listening" {
  checkHostUp dojo-scavenger.wtf
}

@test "juice-shop.wtf has hosts entry for 127.0.0.1" {
  checkHostEntry juice-shop.wtf
}

@test "juice-shop.wtf is listening" {
  checkHostUp juice-shop.wtf
}

