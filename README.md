# extraction_thesis

# 전체 동작
1. input queue에 PDF가 들어오면, thread pool에게 thread 할당 요청
2. thread pool에서 할당된 thread는 PDF 텍스트 추출([1번째, n - 1번째, n번째] 페이지, 총 3페이지)
    - 텍스트 기반 논문: PyPDF2 모듈로 텍스트 추출
    - 이미지 기반 논문: Google Cloud Vision API 등을 이용한 이미지 텍스트 추출(계획)
3. 추출한 텍스트 및 thread 정보(event)를 GPT queue에 전달 후 event 대기
4. GPT thread는 GPT queue에 있는 데이터 가공(제목, 저자, 사사 분류화)
    - 분류 성공: 분류된 데이터 반환 후 event 세트
    - 분류 실패: SIGNAL 반환(남아있는 논문 텍스트 재요청) 후 event 세트
5. thread pool은 event가 세트 되면, 분류 성공 여부를 판단
    - 분류 성공: save queue에 데이터 넣고 thread 반환
    - 분류 실패: 남은 PDF 페이지 텍스트를 재추출해 GPT queue에 전달 후 event 대기
6. save thread는 save queue의 데이터를 excel에 저장