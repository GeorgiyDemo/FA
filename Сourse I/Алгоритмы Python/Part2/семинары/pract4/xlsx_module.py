"""Модуль для формирования отчетов в файл MS Excel"""

import pandas as pd
import xlsxwriter
from task_module import UtilClass

class XlsxClass():

    OUT_XLSX_FILE = "отчет.xlsx"

    def __init__(self, obj_list):
        self.obj_list = obj_list
        self.processing()
    
    def transpose(self, l):
        return [list(e) for e in list(zip(*l))]

    def report_processing(self, report_dict):
        """Формирование главного отчета из словаря"""
        
        report_results_list = []
        for current_cert, subdict in report_dict.items():

            sublist = []
            #Список заголовков
            mainheaders_list = []
            mainsubheaders_list = []
            for student, value in subdict.items():
                buf_list = []
                headers_list = [" "]
                subheaders_list = ["ФИО"]
                
                buf_list.append(student)
                for work in value["works"]:
                    
                    headers_list.append("{} ({})".format(work[0],work[1]))
                    work = work[2:]
                    subheaders_list.extend(["Баллы", "Дата дедлайна", "Дата завершения", "Дата защиты"])
                    headers_list.extend(["" for _ in range(len(work)-1)])
                    buf_list.extend(work)
                
                headers_list.extend(["ИТОГИ", "", "", ""])
                #Это след этап странности, но мне нужна стат последовательность, что dict.items() сделать не может
                for k, v in {"cert_points" : "Баллы за аттестацию", "exam_points" : "Баллы за экзамен", "total_points" : "Общее кол-во баллов", "total_mark" : "Общая оценка"}.items():
                    buf_list.append(value["info"][k])
                    subheaders_list.append(v)
                
                #В случае, если у разных студентов разные хедеры - ориентируемся на того, у кого их больше
                #По-хорошему, тогда надо синхронить столбцы
                if mainheaders_list == []:
                    mainheaders_list = headers_list
                elif len(mainheaders_list) < len(headers_list):
                    mainheaders_list = headers_list

                if mainsubheaders_list == []:
                    mainsubheaders_list = subheaders_list
                elif len(mainsubheaders_list) < len(subheaders_list):
                    mainsubheaders_list = subheaders_list
                sublist.append(buf_list)
            
            sublist.insert(0, subheaders_list)
            report_results_list.append([current_cert, mainheaders_list, sublist])

        return report_results_list
    
    def processing(self):
        
        c = UtilClass.converter
        report_dict = {}
        student_list, work_list, exam_list, cert_list = [[] for _ in range(4)]
        for obj in self.obj_list:
            student_list.append([obj.name, obj.group, obj.course, obj.points, obj.mark])
            
            #Аттестации 
            for cert in obj.cert_obj_list:
                cert_list.append([obj.name, cert.name, cert.points, c(cert.date_begin), c(cert.date_end)])
                
                if report_dict.get(cert.name) == None:
                    report_dict[cert.name] = {}
                report_dict[cert.name][obj.name] = {"info" : {"cert_points" : cert.points, "exam_points": obj.exam_obj.points , "total_points" : obj.points, "total_mark" : obj.mark}, "works" : []}

                for work in cert.work_obj_list:
                    report_dict[cert.name][obj.name]["works"].append([work.name, work.work_type, work.points, c(work.date_deadline), c(work.date_completed), c(work.date_protected)])
                    work_list.append([obj.name, cert.name, work.name, work.work_type, work.points, c(work.date_deadline), c(work.date_completed), c(work.date_protected)])
        
        for obj in self.obj_list:
            exam_list.append([obj.exam_obj.name, obj.exam_obj.points])
        
        student_list = dict(zip(["ФИО","Группа","Курс","Баллы","Оценка"], self.transpose(student_list)))
        exam_list = dict(zip(["Название", "Баллы"],self.transpose(exam_list)))
        cert_list = dict(zip(["Студент", "Название", "Баллы", "Дата начала", "Дата конца"], self.transpose(cert_list)))
        work_list = dict(zip(["Студент","Аттестация","Название работы", "Тип работы", "Баллы", "Дата дедлайна", "Дата завершения", "Дата защиты"], self.transpose(work_list)))

        cert1, cert2 = self.report_processing(report_dict)
        df1 = pd.DataFrame(cert1[2])
        df2 = pd.DataFrame(cert2[2])
        df3 = pd.DataFrame(student_list)
        df4 = pd.DataFrame(work_list)
        df5 = pd.DataFrame(cert_list)
        df6 = pd.DataFrame(exam_list)

        writer = pd.ExcelWriter(XlsxClass.OUT_XLSX_FILE, engine='xlsxwriter')

        df1.to_excel(writer, sheet_name=cert1[0], index=False, header=cert1[1])
        df2.to_excel(writer, sheet_name=cert2[0], index=False, header=cert2[1])
        df3.to_excel(writer, sheet_name='Студенты', index=False)
        df4.to_excel(writer, sheet_name='Работы', index=False)
        df5.to_excel(writer, sheet_name='Аттестации', index=False)
        df6.to_excel(writer, sheet_name='Экзамены', index=False)

        writer.save()