#!/usr/bin/env bash

# Function definitions

addHost() {
  cat >>./targets.bats <<EOL
@test "$1 has hosts entry for 127.0.0.1" {
  checkHostEntry $1
}

@test "$1 is listening" {
  checkHostUp $1
}

EOL
}

addTool() {
  cat >>./tools.bats <<EOL
@test "$1 is executable and in the path" {
  checkCommand $1
}

EOL
}

# Statements for execution

echo Generating targets.bats stub

cat >./targets.bats <<EOL
#!/usr/bin/env bats

source ./test_functions.sh

EOL

echo Generating tools.bats stub

cat >./tools.bats <<EOL
#!/usr/bin/env bats

source ./test_functions.sh

EOL

echo Genertaing individual host tests
for host in $(cat targets.txt | cut -d " " -f 1)
do
  echo "Adding test for $host"
  addHost $host
done

echo Extrapolating tool list from menu config, generating individual tests
for tool in $(grep execute ../config/menu.xml | sed -n 's/^.*\<execute\>\(.*\)\<\/execute.*$/\1/p')
do
  echo "Adding test for $tool"
  addTool $tool
done

for tool in $(grep x-terminal-emulator ../config/menu.xml | sed -n 's/^.*\bash -c \\"\(.*\) .*/\1/p')
do
  echo "Adding test for $tool"
  addTool $tool
done

echo Generating individual tool tests
# for tool in $(cat tools.txt | cut -d " " -f 1)
# do
#  echo "Adding test for $tool"
#  addTool $tool
# done

echo "All done!"
