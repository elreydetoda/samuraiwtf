#!/usr/bin/env #!/usr/bin/env bash

checkHostEntry() {
  local -r hostname="$1"
  result="$(cat /etc/hosts | grep $hostname | cut -d ' ' -f 1)"
  [ "$result" == "127.0.0.1" ]
}

checkHostUp() {
  local -r hostname="$1"
  result="$(curl $hostname -f -s)"
  [ result ]
}

checkCommand() {
  hash $1 2>/dev/null
}
