from typing import Dict
import csv
from multiprocessing import Process

class MyWorker(Process):
    """Обработчик тасков"""

    def __init__(self, input_q, result_q):
        Process.__init__(self)
        self.input_q = input_q
        self.result_q = result_q

    def run(self):
        while not self.input_q.empty():
            current_file = self.input_q.get()
            processing_result = self.my_counter_new(current_file)
            self.result_q.put(processing_result)

    def my_counter_new(self, file_name: str) -> Dict[str, Dict[str, int]]:
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
