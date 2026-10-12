# Dữ liệu

| Mục | Thông tin |
|---|---|
| File | `traffic_accidents.zip` (nén từ `traffic_accidents.csv`, 51.081.134 byte) |
| Tên dataset | Traffic Accidents |
| Link | https://www.kaggle.com/datasets/oktayrdeki/traffic-accidents |
| Tác giả đăng trên Kaggle | Oktay Ördekçi (cập nhật 20/01/2025) |
| Nguồn gốc | Dữ liệu tai nạn giao thông của thành phố Chicago (Mỹ), bộ *Traffic Crashes – Crashes* trên cổng dữ liệu mở [data.cityofchicago.org](https://data.cityofchicago.org/d/85ca-t3if) |
| Giấy phép | Kaggle ghi *Other (specified in description)* nhưng phần mô tả không nêu cụ thể. Dữ liệu gốc do thành phố Chicago công bố công khai (xem Terms of Use của cổng dữ liệu) |
| Kích thước | 209.306 dòng × 24 cột |
| Thời gian | 2015 – 01/2025 |

## Nhóm cột

- **Thời gian:** `crash_date`, `crash_hour`, `crash_day_of_week`, `crash_month`
- **Điều kiện:** `weather_condition`, `lighting_condition`, `roadway_surface_cond`, `road_defect`, `traffic_control_device`, `trafficway_type`, `alignment`
- **Vụ tai nạn:** `first_crash_type`, `crash_type`, `intersection_related_i`, `damage`, `prim_contributory_cause`, `num_units`
- **Thương vong:** `most_severe_injury`, `injuries_total`, `injuries_fatal`, `injuries_incapacitating`, `injuries_non_incapacitating`, `injuries_reported_not_evident`, `injuries_no_indication`

## Cách đọc dữ liệu

File CSV gốc nặng 51 MB, vượt giới hạn 25 MB khi tải lên GitHub qua web, nên được nén thành `.zip`. Pandas đọc thẳng file zip, không cần giải nén:

```python
import pandas as pd

df = pd.read_csv('data/traffic_accidents.zip')
```
