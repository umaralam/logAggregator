"""
importing required modules
"""
import logging
from pathlib import Path
import re
from daemon_log import DaemonLog
from tlog_tag import TaskType, TlogErrorTag

class TDLogParser:
    """
    Parse the daemon log based on tlog input
    """
    def __init__(self, input_date, dictionary_of_tlogs, dictionary_of_search_value, worker_log_recod_list, initializedPath_object, is_tomcat, is_prism):
        self.input_date = input_date
        self.initializedPath_object = initializedPath_object
        self.dictionary_of_tlogs = dictionary_of_tlogs
        self.dictionary_of_search_value = dictionary_of_search_value
        self.worker_log_recod_list = worker_log_recod_list
        self.is_tomcat = is_tomcat
        self.is_prism = is_prism
        self.__initial_index = 0
        self.__final_index = 0
        self.__task_type = ""
        self.out_file = Path()/"final.txt"

    def parse(self):
        """
        Parse dictionary of tlogs to get the search value.
        """
        logging.debug('Parsing daemon log')
        for key, value in self.dictionary_of_tlogs.items():
            for k, v in self.dictionary_of_tlogs[key].items():
                for status in TlogErrorTag:
                    if re.search(r"\b{}\b".format(str(status.value)), v):
                        for search_key, search_value in self.dictionary_of_search_value.items():
                            self.dictionary_of_search_value[search_key] = self.dictionary_of_tlogs[key][search_key]
        self.get_serched_log()

    def get_serched_log(self):
        """
        Get daemon log for the given thread
        """
        # target = Path()/"out.txt"
        logging.debug('Getting daemon log for the issue thread : %s', self.dictionary_of_search_value["THREAD"])
        daemonLog_object = DaemonLog(self.input_date, self.worker_log_recod_list, self.dictionary_of_search_value["THREAD"], self.initializedPath_object)

        task = ""
        if self.is_tomcat:
            daemonLog_object.get_tomcat_log()
            if daemonLog_object.target.exists():
                for status in TlogErrorTag:
                    with open(daemonLog_object.target, "r") as read_file:
                        for i, line in enumerate(read_file):
                            if re.search(r"\b{}\b".format(str(status.value)), line):
                                self.set_initial_index(i)
                                task = status.name
                                break
            
                for ttype in TaskType:
                    with open(daemonLog_object.target, "r") as read_file:
                        for i, line in enumerate(read_file):
                            if task == ttype.name:
                                self.set_task_type(ttype.value)
                                break

                with open(daemonLog_object.target, "r") as read_file:
                    serach_string = f'-process handler params for task {self.get_task_type()} for subType:{self.dictionary_of_search_value["SUB_TYPE"]}'

                    for i, line in enumerate(read_file):
                        if re.search(r"{}".format(str(serach_string)), line):
                            self.set_final_index(i)
                            break
                
                with open(daemonLog_object.target, "r") as read_file:
                    for i, line in enumerate(read_file):
                        if self.get_final_index() <= i < self.get_initial_index() + 1:
                            with open(self.out_file, "a") as write_file:
                                write_file.writelines(line)
            else:
                logging.error("Tomcat daemon log doesn't exist for the issue thread %s : ", self.dictionary_of_search_value["THREAD"])
        
        if self.is_prism:
            daemonLog_object.get_prism_log()
            if daemonLog_object.target.exists():
                for status in TlogErrorTag:
                    with open(daemonLog_object.target, "r") as read_file:
                        for i, line in enumerate(read_file):
                            if re.search(r"\b{}\b".format(str(status.value)), line):
                                self.set_initial_index(i)
                                task = status.name
                                break
            
                for ttype in TaskType:
                    with open(daemonLog_object.target, "r") as read_file:
                        for i, line in enumerate(read_file):
                            if task == ttype.name:
                                self.set_task_type(ttype.value)
                                break

                with open(daemonLog_object.target, "r") as read_file:
                    serach_string = f'-process handler params for task {self.get_task_type()} for subType:{self.dictionary_of_search_value["SUB_TYPE"]}'

                    for i, line in enumerate(read_file):
                        if re.search(r"{}".format(str(serach_string)), line):
                            self.set_final_index(i)
                            break
                
                with open(daemonLog_object.target, "r") as read_file:
                    for i, line in enumerate(read_file):
                        if self.get_final_index() <= i < self.get_initial_index() + 1:
                            with open(self.out_file, "a") as write_file:
                                write_file.writelines(line)
            else:
                logging.error("Prism daemon log doesn't exist for the issue thread %s : ", self.dictionary_of_search_value["THREAD"])

    def get_initial_index(self):
        """
        Get initial index from target file.
        """
        return self.__initial_index


    def set_initial_index(self, initial_index):
        """
        Setting initial index from
        """
        self.__initial_index = initial_index

    def get_final_index(self):
        """
        Get initial index from target file.
        """
        return self.__final_index


    def set_final_index(self, final_index):
        """
        Setting initial index from
        """
        self.__final_index = final_index

    def get_task_type(self):
        """
        Getting failure task type.
        """
        return self.__task_type


    def set_task_type(self, t_type):
        """
        Setting setting failure task type
        """
        self.__task_type = t_type