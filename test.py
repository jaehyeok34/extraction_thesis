from save_thread import SaveThread
from work_queue import WorkQueue


for _ in range(3):
    WorkQueue.saveQueue.put({
        SaveThread.TITLE_KEY    :       '제목',
        SaveThread.AUTHOR_KEY   :       '저자',
        SaveThread.ACK_KEY      :       '사사',
    })

thread = SaveThread()
thread.work()