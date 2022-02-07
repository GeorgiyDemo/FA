#Запуск перегенерации данных
echo "---"
mkdir -p ../analytics
for i in {1..10}
do
   echo "Переместили данные магазина №$i"
   cp ../shop${i}/out.txt ../analytics/store${i}_out.txt
   cp ../shop${i}/in.txt ../analytics/store${i}_in.txt
   cp ../shop${i}/price.txt ../analytics/store${i}_price.txt
done
