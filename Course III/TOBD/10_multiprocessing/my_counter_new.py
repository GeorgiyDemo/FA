from typing import Dict
import csv
def my_counter_new(file_name: str) -> Dict[str, Dict[str, int]]:
    """Считает кол-во и сумму шагов в тегах переданного файла"""
    results_dict = {}
    with open(file_name) as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            r_id, tag, n_steps = row[0].split(";")
            
            if tag not in results_dict:
                results_dict[tag]= {"count": 0,"sum" : 0}
            results_dict[tag]["count"] += 1
            results_dict[tag]["sum"] += int(n_steps)

    return results_dict
