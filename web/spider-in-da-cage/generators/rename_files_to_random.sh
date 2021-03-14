#!/bin/bash
# 
# This script renames files in directory with given 
# extension to random strings

dirname=$1
random_name_lenght="20"

if [ ! -d "$dirname" ]; then
  echo "$dirname is not a directory"
  exit 1
fi

extension="jpg"
find $dirname -type f -iname "*.$extension" -print0 | while IFS= read -r -d $'\0' file; do
    
    random_name="$(tr -dc A-Za-z0-9 </dev/urandom | head -c $random_name_lenght)"
    echo "$file"
    
    cp $file "$(dirname $file)/$random_name.$extension"
    mv $file "$file.backup"
    
    #ls -l "$file"    
done


