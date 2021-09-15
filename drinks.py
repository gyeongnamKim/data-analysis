import pandas as pd

#파일 읽어오기
file_drinks = pd.read_csv('./data/drinks.csv')

#continent의 Nan 값 OT로 교체
file_drinks.continent = file_drinks.continent.fillna('OT')

#대륙별 beer_servings 컬럼 생성
continent_beer_mean = file_drinks.groupby('continent').mean()['beer_servings'].to_frame()
continent_beer_mean.rename(columns={'beer_servings':'beer_survings_cont_avg'},inplace=True)
file_drinks = pd.merge(file_drinks,continent_beer_mean,how='inner',on='continent')
print(file_drinks[['country','beer_servings','continent','beer_survings_cont_avg']].sample(5))
print()

#국가별 total_serveings 컬럼을 만들어서 병합하시오
file_drinks['total_servings'] = file_drinks['beer_servings'] + file_drinks['spirit_servings'] + file_drinks['wine_servings']
print(file_drinks[['country','beer_servings','spirit_servings','wine_servings','total_servings']])

#전체 평균보다 적은 알코올을 섭취하는 대륙 중에서, sprit을 가장 많이 마시는 국가를 구하시오
alcohol_mean = file_drinks['total_litres_of_pure_alcohol'].mean()
continent_alcohol_mean = file_drinks.groupby('continent').mean()['total_litres_of_pure_alcohol'].to_frame()
continent_alcohol_down = continent_alcohol_mean[continent_alcohol_mean.total_litres_of_pure_alcohol < alcohol_mean]
continent_alcohol = pd.merge(file_drinks,continent_alcohol_down,how='inner',on='continent')
country_spirit_best = continent_alcohol.sort_values(by='spirit_servings',ascending=False)
print('전체 평균보다 적은 알코올을 섭취하는 대륙 중에서, sprit을 가장 많이 마시는 국가는 : ',country_spirit_best.iloc[0,0])

#술 소비량 대비 알콜 비율 구하고 대한민국 순위를 구하시오.
file_drinks['alcohol_percent'] = file_drinks['total_litres_of_pure_alcohol'] / file_drinks['total_servings']
file_drinks['alcohol_percent']  = file_drinks['alcohol_percent'].fillna(0)
file_drinks['alcohol_percent_rate'] = file_drinks['alcohol_percent'].rank(ascending=False)
file_drinks['alcohol_percent_rate'] = file_drinks.alcohol_percent_rate.fillna(0)
file_drinks['alcohol_percent_rate'] = file_drinks['alcohol_percent_rate'].apply(int)
korea = file_drinks[file_drinks.country == 'South Korea']
print(file_drinks[['country','alcohol_percent','alcohol_percent_rate']])
print('술 소비량 대비 알콜 비율 구하고 대한민국 순위 :',korea.iloc[0,-1])
print()

#대륙별 술 소비량 대비 알콜 비율을 구하시오
alcohol_cont_rate = file_drinks.groupby('continent').total_litres_of_pure_alcohol.sum() / file_drinks.groupby('continent').total_servings.sum()
alcohol_cont_rate = alcohol_cont_rate.to_frame()
alcohol_cont_rate.rename(columns={0:'alcohol_rate_continent'},inplace=True)
alcohol_continent = pd.merge(file_drinks,alcohol_cont_rate,how='inner',on='continent')
print(alcohol_continent[['country','continent','alcohol_rate_continent']].sample(5))