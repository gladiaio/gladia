#!/bin/bash
helpFunction()
{
   echo ""
   echo "Usage: $0 -P protocol -h host -p port -d test-directory"
   echo -e "\t-P Protocol http/https"
   echo -e "\t-h host without http nor port"
   echo -e "\t-p port"
   echo -e "\t-t timeout"
   echo -e "\t-d test directory to generate tests into"
   exit 1
}

while getopts "P:h:p:d:t:" opt
do
   case "$opt" in
      P ) protocol="$OPTARG" ;;
      h ) host="$OPTARG" ;;
      p ) port="$OPTARG" ;;
      d ) directory="$OPTARG" ;;
      t ) timeout="$OPTARG" ;;
      ? ) helpFunction ;;
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$protocol" ] || [ -z "$host" ] || [ -z "$port" ] || [ -z "$directory" ] || [ -z "$timeout" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

cd $directory
for test in $(ls);do
    mocha $test --timeout $timeout
done