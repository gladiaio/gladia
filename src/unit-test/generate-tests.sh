#!/bin/bash
helpFunction()
{
   echo ""
   echo "Usage: $0 -P protocol -h host -p port -d test-directory"
   echo -e "\t-P Protocol http/https"
   echo -e "\t-h host without http nor port"
   echo -e "\t-p port"
   echo -e "\t-d test directory to generate tests into"
   exit 1
}

while getopts "P:h:p:d:" opt
do
   case "$opt" in
      P ) protocol="$OPTARG" ;;
      h ) host="$OPTARG" ;;
      p ) port="$OPTARG" ;;
      d ) directory="$OPTARG" ;;
      ? ) helpFunction ;;
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$protocol" ] || [ -z "$host" ] || [ -z "$port" ] || [ -z "$directory" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi


wget -O openapi.json $protocol://$host:$port/openapi.json
oatts generate --host $host:$port -s openapi.json -w $directory