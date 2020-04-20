"""Модуль для формирования отчетов в файл MS Excel"""

import pandas as pd
import xlsxwriter
class XlsxClass():

    OUT_XLSX_FILE = "отчет.xlsx"

    def __init__(self, obj_list):
        self.obj_list = obj_list
        self.processing()
    
    def transpose(self, l):
        return [list(e) for e in list(zip(*l))]

    def report_processing(self, report_dict):
        """Формирование главного отчета из словаря"""
        subdict1, subdict2 = [report_dict[key] for key in report_dict.keys()]
        sublist1 = []
        
        #Список заголовков
        mainheaders_list = []
        mainsubheaders_list = []
        for student, value in subdict1.items():
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
            
            headers_list.extend(["ИТОГИ", "", ""])
            #Это след этап странности, но мне нужна стат последовательность, что dict.items() сделать не может
            for k, v in {"cert_points" : "Баллы за аттестацию", "total_mark" : "Общая оценка", "total_points" : "Общее кол-во баллов"}.items():
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

            sublist1.append(buf_list)
        
        print(subheaders_list)
        print(mainheaders_list)
        sublist1.insert(0, subheaders_list)
        print(sublist1)
        return mainheaders_list, sublist1


    def converter(self, d_input):
        try:
            return d_input.strftime("%d.%m.%Y")
        except AttributeError:
            return "-"
    
    def processing(self):
        
        c = self.converter
        report_dict = {}
        student_list, work_list, exam_list, cert_list = [[] for _ in range(4)]
        for obj in self.obj_list:
            student_list.append([obj.name, obj.group, obj.course, obj.points, obj.mark])
            
            #Аттестации 
            for cert in obj.cert_obj_list:
                cert_list.append([obj.name, cert.name, cert.points, c(cert.date_begin), c(cert.date_end)])
                
                if report_dict.get(cert.name) == None:
                    report_dict[cert.name] = {}
                report_dict[cert.name][obj.name] = {"info" : {"cert_points" : cert.points, "total_mark" : obj.mark, "total_points" : obj.points}, "works" : []}

                for work in cert.work_obj_list:
                    report_dict[cert.name][obj.name]["works"].append([work.name, work.work_type, work.points, c(work.date_deadline), c(work.date_completed), c(work.date_protected)])
                    work_list.append([obj.name, cert.name, work.name, work.work_type, work.points, c(work.date_deadline), c(work.date_completed), c(work.date_protected)])
        
        for obj in self.obj_list:
            exam_list.append([obj.exam_obj.name, obj.exam_obj.points])
        
        student_list = dict(zip(["ФИО","Группа","Курс","Баллы","Оценка"], self.transpose(student_list)))
        exam_list = dict(zip(["Название", "Баллы"],self.transpose(exam_list)))
        cert_list = dict(zip(["Студент", "Название", "Баллы", "Дата начала", "Дата конца"], self.transpose(cert_list)))
        work_list = dict(zip(["Студент","Аттестация","Название работы", "Тип работы", "Баллы", "Дата дедлайна", "Дата завершения", "Дата защиты"], self.transpose(work_list)))

        headers1, list1 = self.report_processing(report_dict)
        df0 = pd.DataFrame(list1)
        df1 = pd.DataFrame(student_list)
        df2 = pd.DataFrame(work_list)
        df3 = pd.DataFrame(cert_list)
        df4 = pd.DataFrame(exam_list)

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(XlsxClass.OUT_XLSX_FILE, engine='xlsxwriter')

        # Write each dataframe to a different worksheet.
        df0.to_excel(writer, sheet_name='Аттестация 1', index=False, header=headers1)
        #df0.to_excel(writer, sheet_name='Аттестация 2', index=False)
        df1.to_excel(writer, sheet_name='Студенты', index=False)
        df2.to_excel(writer, sheet_name='Работы', index=False)
        df3.to_excel(writer, sheet_name='Аттестации', index=False)
        df4.to_excel(writer, sheet_name='Экзамены', index=False)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        
