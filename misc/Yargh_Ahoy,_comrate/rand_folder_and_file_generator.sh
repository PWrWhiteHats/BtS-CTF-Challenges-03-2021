 #!/bin/bash
function creation() {
random=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
mkdir $random
for dir in */
do
cd $dir
for n in {1..87}; do
    dd if=/dev/urandom of=file$( printf %03d "$n" ).txt bs=$(( ( RANDOM % 1000 )  + 1223 )) count=1
done
#dd if=/dev/urandom of=file$( printf %03d "333").txt bs=$(( ( RANDOM % 1000 )  + 2678 )) count=1
cd <absolute path of script>
done
}

for i in {1..100}; do
creation
done

