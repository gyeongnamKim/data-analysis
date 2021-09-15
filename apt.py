import pandas as p
#소수점 제한두기
p.options.display.float_format = '{:.2f}'.format
#파일 가져오기 (encoding="cp949"는 엑셀파일 불러올때 한글이 안깨진다)
csv_read = p.read_csv('./data/apt.csv', encoding="cp949")
#자료 수
print('자료 수\t\t행 수 :',len(csv_read.index))
print('\t\t\t열 수 :',len(csv_read.columns))

#자료 파악하기
print('이 자료는 지역별 아파트 거래의 세부내용을 담은 파일이다.')

#특정 열 (지역) 출력하기
print('\n\n지역 정보 출력')
print(csv_read.iloc[:,0])

#면적 130이상 가격 1억5천 미만 아파트 출력하기
print('\n\n면적 130이상 가격 1억5천 미만 아파트 단지명 출력하기')
area_csv = csv_read['면적'] >= 130
area_csv = csv_read[area_csv]
value_csv = area_csv['가격'] < 13000
value_csv = area_csv[value_csv]
print(value_csv['아파트'])

#4억원 이상으로 거래된 아파트 출력하기
print('\n\n 4억원 이상으로 거래된 아파트 출력하기')
sort_price = csv_read['가격'] >= 40000
print(csv_read[sort_price])

#가격 면적 단가 10개 출력하기
print('\n\n 가격 면적 단가 10개 출력하기')
csv_read['단가'] = csv_read['가격'] / csv_read['면적']
print(csv_read[['가격','단가','면적']].head(10))

#가격 오름차순 정렬하기
print('\n\n 가격 오름차순 정렬하기')
sort_csv = csv_read.sort_values(by='가격',ascending=True,inplace=False)
print(sort_csv[['지역', '번지', '본번', '부번', '아파트', '면적', '계약년월', '계약일', '단가', '층', '건축년도',
       '도로명', '가격']])

#25억 넘는 아파트만 출력하기
print('\n\n 25억 넘는 아파트만 출력하기')
price25_csv = csv_read['가격'] >= 250000
price25_csv = csv_read[price25_csv]
print(price25_csv[['지역', '번지', '본번', '부번', '아파트', '면적', '계약년월', '계약일', '단가', '층', '건축년도',
       '도로명', '가격']])

#강릉 아파트만 출력
print('\n\n 강릉 아파트만 출력')
gang_csv = csv_read['지역'].str.contains('강릉',na=False)
print(csv_read[gang_csv])

#강릉 아파트만 출력하여 각 변수 평균 출력
print('\n\n 강릉 아파트만 출력하여 각 변수 평균 출력')
gangreng_csv = csv_read[gang_csv]
print(gangreng_csv.mean())




