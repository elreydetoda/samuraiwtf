#!/usr/bin/env bats

source ./test_functions.sh

@test "sakura is executable and in the path" {
  checkCommand sakura
}

@test "firefox is executable and in the path" {
  checkCommand firefox
}

@test "google-chrome is executable and in the path" {
  checkCommand google-chrome
}

@test "burp is executable and in the path" {
  checkCommand burp
}

@test "zaproxy is executable and in the path" {
  checkCommand zaproxy
}

@test "w3af is executable and in the path" {
  checkCommand w3af
}

@test "nmap is executable and in the path" {
  checkCommand nmap
}

@test "sqlmap is executable and in the path" {
  checkCommand sqlmap
}

@test "nikto is executable and in the path" {
  checkCommand nikto
}

