from work_queue import WorkQueue
from openpyxl import Workbook, load_workbook

class SaveThread:    
    TITLE_KEY = 'title'
    AUTHOR_KEY = 'author'
    ACK_KEY = 'acknowledgements'
    
    SAVE_PATH = 'thesis_contents.xlsx'

    def work(self):
        while True:
            saveData: dict = WorkQueue.saveQueue.get()            # queue 모니터링(bloking)
            
            # TODO: excel에 saveData 저장하기
            excelFile = None
            try:
                excelFile = load_workbook(SaveThread.SAVE_PATH)
            except FileNotFoundError:
                excelFile = Workbook()
                
            workSheet = excelFile.active
            workSheet.title = 'thesis'

            workSheet.append([
                saveData[SaveThread.TITLE_KEY],
                saveData[SaveThread.AUTHOR_KEY],
                saveData[SaveThread.ACK_KEY],
            ])

            excelFile.save(SaveThread.SAVE_PATH)
