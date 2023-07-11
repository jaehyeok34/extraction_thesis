# from save_thread import SaveThread
# from work_queue import WorkQueue


# for _ in range(3):
#     WorkQueue.saveQueue.put({
#         SaveThread.TITLE_KEY    :       '제목',
#         SaveThread.AUTHOR_KEY   :       '저자',
#         SaveThread.ACK_KEY      :       '사사',
#     })

# thread = SaveThread()
# thread.work()


# import pytesseract
# from pdf2image import convert_from_path

# pdf_path = './thesis/thesis1.pdf'
# images = convert_from_path(pdf_path)

# print(images)


pages = ['1', '2']
question = ['title', 'author', 'acknowledgements']

print('\n'.join(pages) + '\n' + ', '.join(question) + ' of the paper: ')