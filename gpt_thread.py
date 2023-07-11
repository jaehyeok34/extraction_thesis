from work_queue import WorkQueue
from model_controller import ModelController
from model_event import ModelEvent
from save_thread import SaveThread
import openai
from config import *

class GptThread:
    def __init__(self) -> None:
        openai.api_key = API_KEY

    def work(self):
        while True:
            # TODO: GPT Queue를 모니터링 하고, 값이 들어오면 GPT API를 이용해 데이터 분류
            #       성공 시, Thread Model에게 분류한 데이터를 전달 후 event set
            #       실패 시, Thread Model에게 논문 추가 데이터 요청 후 event set
            datas = WorkQueue.gptQueue.get()
            frontPages: list = datas[0][:1]
            backPages: list = datas[0][2:]
            event: ModelEvent = datas[1]



            # TODO: GPT API를 통해 데이터 분류
            response = self.get_paper_details(frontPages)

            # TODO: GPT 분류 성공
            # 다음과 같은 형식의 dict를 전달해야 함
            # { SaveThread.TITLE_KEY: "제목", SaveThread.AUTHOR_KEY: "저자", SaveThread.ACK_KEY: "사사" }
            # if (title is not None) and (authors is not None) and (acknowledgements is not None):
            #     event.set({
            #         SaveThread.TITLE_KEY    :       title,
            #         SaveThread.AUTHOR_KEY   :       authors,
            #         SaveThread.ACK_KEY      :       acknowledgements,
            #     })

            # TODO: GPT 분류 실패
            # else:
            event.set(ModelController.SIGNAL)       # GPT 분류 실패
                
    def get_paper_details(
            self, 
            pages:list, 
            question: list = ['Title', 'Author', 'Acknowledgements']
    ):      
        print('gpt 요청')
        response = openai.Completion.create(
            engine="text-davinci-003", # 현재 가장 성능이 좋은 모델 사용
            prompt = ('\n'.join(pages) + '\n\n' + ', '.join(question) + ' of the paper: '),
            temperature=0.3,
            max_tokens=60
        )
        rsp = response.choices[0].text.strip()
        print('==============================================')
        print(rsp)
        print('==============================================')


        return rsp   