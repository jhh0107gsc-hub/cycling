# Data

## 데이터 출처

- GoldenCheetah OpenData
- https://github.com/GoldenCheetah/OpenData

## 사용 목적

공개된 사이클링 훈련 기록을 이용하여 데이터 분석과
머신러닝 학습을 진행한다.

## 데이터 관리

다운로드한 원본 데이터는 `data/raw/`에 저장한다.
원본 데이터는 GitHub에 업로드하지 않는다.

정제한 데이터는 `data/processed/`에 저장한다. 원본과 정제 데이터 폴더는
`.gitignore`에 포함되어 있으므로 GitHub에 업로드하지 않는다. 분석 코드를
실행하여 같은 파일을 다시 생성할 수 있도록 노트북만 버전 관리한다.

## 정제 데이터

- 파일: `data/processed/goldencheetah_bike_rides_cleaned.csv`
- 생성 노트북: `notebooks/01_goldencheetah_exploration.ipynb`
- 데이터 크기: 592행, 63열
- 대상: GoldenCheetah 공개 데이터의 자전거 라이드

정제 데이터에는 원본 주요 지표, 분석용 파생 지표, 계산 가중치, 품질
검토 라벨과 분석 목적별 사용 가능 여부가 포함된다. 라이드 전체를 일괄
삭제하지 않고 `*_is_usable` 열을 이용해 목적에 맞는 기록을 선택한다.

CSV를 다시 불러올 때는 날짜 열을 함께 변환한다.

```python
cleaned_rides_df = pd.read_csv(
    "data/processed/goldencheetah_bike_rides_cleaned.csv",
    parse_dates=["date"],
)
```
