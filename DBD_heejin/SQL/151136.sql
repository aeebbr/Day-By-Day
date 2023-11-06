/* [Programmers] 151136. 평균 일일 대여 요금 구하기 */

SELECT round(avg(DAILY_FEE), 0) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';