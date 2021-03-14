#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
target_dir="$DIR/../html/cages"
images_dir="$DIR/../html/images"

gallery_img_nr=3
random_name_lenght="20"

while getopts ":t:i:f" opt; do         # note the leading colon
    case $opt in
        t) target_dir=${OPTARG} ;;
        i) images_dir=${OPTARG} ;;
        f) 
          echo "Force specified. Deleting content of $target_dir"
          rm -rf $target_dir/*
          ;;
        :) if [[ $OPTARG == "t" ]]; then
               : # Default values already set
           fi
           ;;
    esac
done
shift $((OPTIND-1))


create_html_gallery () {
# Generates simple HTML gallery
# for each entry that consists from html href path and img src
# separeted by ',' sign 
# Arg: "<href_path>,<img_src>"

cat << EOF
<html>
<head>
<style>

div.gallery {
  border: 1px solid #ccc;
  display: flex;
  margin: 5px auto;
  border: 1px solid #ccc;
  position: absolute;
  top: 30%;
  left: 25%;

}

div.gallery a:hover {
  border: 1px solid #777;
}
div.gallery a {
    margin-right: 10%;
}

div.gallery img {
  width: 100%;
  height: auto;
  margin-top: 20%;
}

</style>
</head>
<body>

<div class="gallery">
EOF


  for paths in "$@"
  do
      paths_array=($(echo $paths | tr "," "\n"))

      htmlPath=${paths_array[0]}
      imgPath=${paths_array[1]}
      echo "
      <a  href=\"$htmlPath\">
          <img src=\"$imgPath\">
      </a>
      "
  done

cat << EOF
</div>
</body>
</html>
EOF
}



get_random_file_from_dir () {
  dir=$1
  files=($(ls $1))
  files_amount="${#files[@]}"
  
  if [[ $files_amount -gt 0 ]]
  then
    random_nr=$((RANDOM % $files_amount))
    file="${files[$random_nr]}"
    # Get another random file, until no references to file found in $dir
    while [[ $(grep -rnw $dir/* -e $file ) ]]; 
    do 
      random_nr=$((RANDOM % $files_amount))
      file="${files[$random_nr]}"
    done

  else # default action
    file="index.html"
  fi
  echo "$file"
}

images=($(ls $images_dir))
img_amount="${#images[@]}"

echo "Generating HTML files"
echo "Target image: $target_dir"
echo "Src images: $images_dir. Image amount: $img_amount"

i=0
while [ "$i" -le "${#images[@]}" ]
do
  img1="../images/${images[$i]}"
  img2="../images/${images[$((i+1))]}"
  img3="../images/${images[$((i+2))]}"

  file1="$(get_random_file_from_dir $target_dir)"
  file2="$(get_random_file_from_dir $target_dir)"
  file3="$(get_random_file_from_dir $target_dir)"

  random_name="$(tr -dc A-Za-z0-9 </dev/urandom | head -c $random_name_lenght)"

  if [[ "$i" -gt $((${#images[@]} - 3)) ]]
  then
    img2="../images/${images[$((i-1))]}"
    img3="../images/${images[$((i-2))]}"
    # Last files
    echo "Generating index.html file"
    create_html_gallery "$file1,$img1" "$file2,$img2" "$file3,$img3" > "$target_dir/index.html"
  elif [[  $img1 && ${img1-x} && $img2 && ${img2-x} && $img3 && ${img3-x} ]]
  then
    create_html_gallery "$file1,$img1" "$file2,$img2" "$file3,$img3" > "$target_dir/$random_name.html"
  fi

  i=$(($i+3))
done

htmlFiles=($(ls $target_dir))
echo "Created ${#htmlFiles[@]} html files"