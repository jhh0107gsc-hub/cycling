import json
from pathlib import Path

print("현재 작업 디렉터리:", Path.cwd())

json_path = Path(
    "data/raw/033874ce-e20d-44ba-9cc9-125030b6662f/"
    "{033874ce-e20d-44ba-9cc9-125030b6662f}.json"
)

with json_path.open("r", encoding="utf-8") as file:
    cycling_data = json.load(file)

print("전체 자료형:", type(cycling_data))
print("최상위 항목:", cycling_data.keys())

print("RIDES 자료형:", type(cycling_data["RIDES"]))
print("전체 운동 수:", len(cycling_data["RIDES"])) # 731

athlete = cycling_data["ATHLETE"]
rides = cycling_data["RIDES"]

# 첫 번째 라이드 확인
first_ride = rides[0]

print("\n데이터 버전:", cycling_data["VERSION"])
print("라이더 정보:", athlete)

print("\n첫 번째 운동의 항목:", first_ride.keys())
print("운동 날짜:", first_ride["date"])
print("센서 종류:", first_ride["data"])
print("운동 종류:", first_ride["sport"])

metrics = first_ride["METRICS"]

print("METRICS 개수:", len(metrics)) # 86개의 라이드 지표
print("METRICS head:", list(metrics.keys())[:10])

sport_counts = {}

for ride in rides:
    sport = ride["sport"]

    if sport not in sport_counts:
        sport_counts[sport] = 0

    sport_counts[sport] += 1

print("\n운동 종류별 개수:", sport_counts) # Bike: 592, total: 731

bike_rides = [ride for ride in rides if ride["sport"] == "Bike"]

print("\n자전거 운동 수:", len(bike_rides))

# 주요 센서 - 파워, 심박 센서 여부 확인
power_count = 0
heart_rate_count = 0
power_and_heart_rate_count = 0

for bike_ride in bike_rides:
    data = bike_ride["data"]

    if "P" in data:
        power_count += 1

    if "H" in data:
        heart_rate_count += 1

    if "P" in data and "H" in data:
        power_and_heart_rate_count += 1

print("파워가 있는 자전거 운동:", power_count)
print("심박수가 있는 자전거 운동:", heart_rate_count)
print("파워와 심박수가 모두 있는 운동:", power_and_heart_rate_count)

# 자전거 운동 수: 592
# 파워가 있는 자전거 운동: 469
# 심박수가 있는 자전거 운동: 465
# 파워와 심박수가 모두 있는 운동: 373

complete_ride = None

for bike_ride in bike_rides:
    data = bike_ride["data"]

    if "P" in data and "H" in data:
        complete_ride = bike_ride
        break

print("\n선택한 운동 날짜:", complete_ride["date"])
print("선택한 운동 센서:", complete_ride["data"])

complete_metrics = complete_ride["METRICS"]

important_metrics = [
    "workout_time",
    "time_riding",
    "total_distance",
    "average_power",
    "max_power",
    "average_hr",
    "max_heartrate",
    "elevation_gain",
    "coggan_tss",
    "coggan_if",
]

for metric_name in important_metrics:
    print(metric_name, ":", complete_metrics.get(metric_name))

# 선택한 운동 날짜: 2007/05/13 05:20:15 UTC
# 선택한 운동 센서: TDSPHC-A-L-----
# workout_time : 30275.00000
# time_riding : 30090.00000
# total_distance : 175.16700
# average_power : ['190.12172', '6055.00000']
# max_power : 590.00000
# average_hr : ['144.94682', '6055.00000']
# max_heartrate : 184.00000
# elevation_gain : 3232.00000
# coggan_tss : 674.50390
# coggan_if : ['0.89557', '30275.00000']

# 매칭되는 CSV 파일을 확인하여 각 지표들의 단위를 확인할 수 있다.
# 약 8시간 20분에 달하는 라이딩 임에도 0.9에 가까운 IF 값과, 그에 비해 비교적 낮은 145bpm의 평균 심박으로 보아
# 단순히 자전거 라이드를 선택하는 것이 아닌 유효한 라이드 데이터를 구분해야 함을 확인하였다.
# 따라서 이후 라이드 데이터 분석은 결과 분석의 편의를 위해 notebooks/ 에서 로컬 주피터 노트북에서 이어가고자 한다.