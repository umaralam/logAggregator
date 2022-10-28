"""
path finder class
"""
import logging
from datetime import datetime
from pathlib import Path
from webbrowser import get
from path_initializer import LogPathFinder


class LogFileFinder():
    """
    transaction and daemon log path finder class
    """
    def __init__(self, input_date, initializedPath_object):
        self.input_date = input_date
        self.initializedPath_object = initializedPath_object
        self.is_prism_billing_tlog_path = False
        # self.is_tomcat_path
    
    def prism_billing_tlog_path(self):
        
        log_path = self.initializedPath_object
        # log_path.initialize_prism_path()

        prism_tlog_path = f"{log_path.prism_log_path_dict[log_path.prism_tlog_log_path]}/BILLING"
        path = Path(rf"{prism_tlog_path}")
        # prism_tlog_path = f"{log_path.prism_log_path_dict[log_path.prism_tlog_log_path]}/BILLING"
        # path = Path(rf"{prism_tlog_path}")

        if path.exists():
            logging.debug('Prism BILLING tlog path exists.')
            self.set_prism_billing_path(True)
        else:
            self.set_prism_billing_path(False)
            logging.error('Prism BILLING tlog path does not exists')
    

    def prism_billing_tlog_files(self, input_trans_date):
        """
        function to find prism tlog file path
        """
        tlog_files = []
        
        logPath_object = self.initializedPath_object
        # log_path.initialize_prism_path()

        prism_tlog_path = f"{logPath_object.prism_log_path_dict[logPath_object.prism_tlog_log_path]}/BILLING"
        path = Path(rf"{prism_tlog_path}")

        try:
            billing_tlog_files = [p for p in path.glob(f"TLOG_BILLING_{input_trans_date}*.*")]
            if bool(billing_tlog_files):
                for prism_billing_files in billing_tlog_files:
                    tlog_files.append(prism_billing_files)
                    return tlog_files
            else:
                logging.error('Prism billing tlog directory does not have %s dated files', input_trans_date)

        except ValueError as error:
            logging.exception(error)
        except Exception as error:
            logging.exception(error)
        
        return None

    def prism_daemonlog_file(self):
        """
        function to find prism daemon log file path
        """
        logPath_object = self.initializedPath_object
        prism_daemon_log_path = f"{logPath_object.prism_log_path_dict[logPath_object.prism_daemon_log_path]}"
        

        if prism_daemon_log_path:
            return prism_daemon_log_path
        else:
            logging.error('Prism daemon log path does not exists')
        return None
    
    def prism_rootlog_file(self):
        logPath_object = self.initializedPath_object
        prism_root_log_path = f"{logPath_object.prism_log_path_dict[logPath_object.prism_root_log_path]}"

        if prism_root_log_path:
            return prism_root_log_path
        else:
            logging.error('Prism root log path does not exists')
        return None

    def prism_daemonlog_backup_file(self):
        logPath_object = self.initializedPath_object
        prism_daemon_log_backup = f"{logPath_object.prism_log_path_dict[logPath_object.prism_daemon_log_backup_path]}"
        
        backup_date = self.input_date
        date = self.get_backup_date(backup_date)
        prism_daemon_log_backup_path = f"{prism_daemon_log_backup}{date[0]}-{date[1]}/prismD-{date[0]}-{date[1]}-{date[2]}*.gz"

        if prism_daemon_log_backup_path:
            return prism_daemon_log_backup_path
        else:
            logging.error('Prism daemon backup log path does not exists')
        return None

    def prism_rootlog_backup_file(self):
        logPath_object = self.initializedPath_object
        prism_root_log_backup = f"{logPath_object.prism_log_path_dict[logPath_object.prism_root_log_backup_path]}"
        
        backup_date = self.input_date
        date = self.get_backup_date(backup_date)
        
        prism_root_log_backup = "/PRISM/prismD/PRISMD_LOGS/log4j/backup/"
        prism_root_log_backup_path = f"{prism_root_log_backup}{date[0]}-{date[1]}/root-{date[0]}-{date[1]}-{date[2]}*.gz"

        if prism_root_log_backup_path:
            return prism_root_log_backup_path
        else:
            logging.error('Prism root backup log path does not exists')
        return None

    def get_backup_date(self, input_date):
        dts = datetime.strptime(input_date, "%Y%m%d")
        dtf = dts.strftime("%Y-%m-%d")
        date_formated = dtf.split("-")
        return date_formated

    def set_prism_billing_path(self, is_prism_billing_tlog_path):
        self.is_prism_billing_tlog_path = is_prism_billing_tlog_path

    def get_prism_path(self):
        return self.is_prism_billing_tlog_path