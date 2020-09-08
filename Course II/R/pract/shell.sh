#cd 1 && echo "1,2,3,4,5,6,7,8 " > 

for _ in 1 .. 5
do
	echo $(( ( RANDOM % 10 )  + 1 ))
done