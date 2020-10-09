#Запуск перегенерации данных
python3 generator.py
echo "---"
mkdir -p analytics
for i in {1..10}
do
   echo "Переместили данные магазина №$i"
   cp ../shop${i}/out.txt ../analytics/store${i}_out.txt
   cp ../shop${i}/in.txt ../analytics/store${i}_in.txt
done