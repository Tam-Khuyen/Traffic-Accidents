# Traffic Accidents in Chicago

Đồ án cuối kỳ CSC17104 — Programming for Data Science, Khoa Công nghệ Thông tin, Trường ĐH Khoa học Tự nhiên, ĐHQG-HCM.

Nhóm khảo sát dữ liệu tai nạn ghi nhận ở Chicago và phân tích sáu câu hỏi về thời gian, thời tiết, thương tích và giao lộ. Giai đoạn so sánh chính là **2018–2024**.

## Nhóm Tam Khuyển (Nhóm 14)

| Thành viên | MSSV | Câu hỏi phụ trách | Phần việc chung |
|---|---|---|---|
| Nguyễn Tiến Hưng | 24127391 | Q1, Q2 | Thu thập, khảo sát và chuẩn bị dữ liệu |
| Lê Việt Hải | 24127029 | Q3, Q4 | Dữ liệu thời tiết NOAA và quy trình Machine Learning |
| Nguyễn Gia Kiệt | 24127195 | Q5, Q6 | Đóng gói đồ án, tổng kết và trình chiếu |

## Dữ liệu

- **Nguồn chính** — [Traffic Accidents trên Kaggle](https://www.kaggle.com/datasets/oktayrdeki/traffic-accidents), Oktay Ördekçi, bản 1 ngày 20/01/2025. File gốc có **209.306 bản ghi × 24 cột**, từ **03/03/2013 đến 18/01/2025**. Mỗi dòng mô tả một vụ được ghi nhận. [City of Chicago Traffic Crashes](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data) cung cấp bối cảnh về biên bản E-Crash của Chicago Police Department. Bản Kaggle chưa mô tả đầy đủ cách chọn bản ghi từ dữ liệu gốc.
- **Giấy phép bản Kaggle** — Metadata ghi `Other (specified in description)`. Mô tả chưa nêu điều khoản cụ thể, nên quyền sử dụng cho mục đích giáo dục và quyền phân phối lại bản CSV chưa được xác nhận từ thông tin công bố. Nhóm ghi nguồn cho người đăng và City of Chicago. Tham khảo [điều khoản dữ liệu của City of Chicago](https://www.chicago.gov/city/en/narr/foia/data_disclaimer.html) cho nguồn chính thức.
- **Q2** — Bảng ngày kết thúc giờ mùa hè (DST) được tạo theo [quy tắc của NIST](https://www.nist.gov/pml/time-and-frequency-division/popular-links/daylight-saving-time-dst) và ghép theo năm.
- **Q3** — [NOAA NCEI GHCN-Daily v3](https://doi.org/10.7289/V5D21VHZ), trạm [Chicago O’Hare USW00094846](https://www.ncei.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND%3AUSW00094846/detail). [Bản trích 2.557 ngày](data/reference/ohare_ghcn_daily_2018_2024.csv) giữ lượng giáng thủy, tuyết và các cờ đo lường để ghép theo ngày. Trích dẫn theo [metadata của NOAA](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc%3AC00861/html).

[Notebook 01](notebooks/01_collection_exploration.ipynb) giữ riêng các nhãn như `UNKNOWN`, bỏ 31 dòng trùng hoàn toàn và xuất **209.275 dòng × 29 cột**. Có **181.051 bản ghi** trong giai đoạn 2018–2024. Xem thêm [tài liệu dữ liệu](data/README.md).

## Các câu hỏi

| Câu | Câu hỏi phân tích | Notebook |
|---|---|---|
| Q1 | Số vụ mỗi tháng và tỷ lệ có thương tích thay đổi thế nào giữa 2018–2019, 2020–2021 và 2022–2024? Kết quả có vững khi đổi mốc thời gian hoặc giữ dòng trùng? | [Q1–Q2](notebooks/02_analysis_q1_q2.ipynb) |
| Q2 | Trong khung 16:00–18:59, số vụ trong bóng tối và tỷ lệ có thương tích thay đổi thế nào giữa 14 ngày trước và sau khi kết thúc DST? | [Q1–Q2](notebooks/02_analysis_q1_q2.ipynb) |
| Q3 | Mưa và tuyết gắn với tỷ lệ thương tích thế nào trong các nhóm mặt đường và ánh sáng tương đương? Nhãn trong biên bản khớp với số đo O’Hare đến mức nào? | [Q3](notebooks/02_analysis_q3.ipynb) |
| Q4 | Giờ, thứ và tháng có đủ để dự đoán vụ có thương tích trong một kịch bản giả định lúc nhận tin? | [Q4 — Machine Learning](notebooks/03_ml_question.ipynb) |
| Q5 | Các nhóm nguyên nhân được ghi nhận nào có tỷ lệ thương tích nặng cao? Thứ hạng thay đổi thế nào theo loại va chạm và tiêu chí lọc? | [Q5–Q6](notebooks/02_analysis_q5_q6.ipynb) |
| Q6 | Tỷ lệ thương tích nặng ở giao lộ khác nhau thế nào theo thiết bị điều khiển, ngày/đêm và loại va chạm? | [Q5–Q6](notebooks/02_analysis_q5_q6.ipynb) |

## Công trình công khai liên quan

- [Elisehk — Prediction of Traffic Accident](https://github.com/Elisehk/Machine-Learning---Prediction-of-Traffic-Accident/blob/main/Machine%20Learning%20-%20Prediction%20of%20Traffic%20Accident.ipynb) dùng cùng nguồn Kaggle để thực hành mô hình dự đoán. Q4 của nhóm giới hạn thông tin đầu vào ở lịch và giờ, chia tập theo thời gian, và đánh giá số cảnh báo tại ngưỡng chọn trước trên tập validation.
- [mariam2004 — Traffic Crash Analysis](https://github.com/mariam2004/traffic-crash-analysis) dùng cùng snapshot cho quy trình SQL và dashboard, có tổng hợp xu hướng tháng, nguyên nhân và mức độ thương tích. Nhóm bổ sung so sánh ghép cặp quanh ngày đổi giờ (Q2), ghép quan trắc NOAA (Q3) và so sánh thiết bị trên cùng phân bố loại va chạm và ánh sáng (Q6).
- [Danh sách notebook cộng đồng trên Kaggle](https://www.kaggle.com/datasets/oktayrdeki/traffic-accidents/code).

## Kết quả chính

1. **Q1 — Số vụ ghi nhận và tỷ lệ thương tích biến động khác nhau.** Bình quân từ 2.308 xuống 2.019 vụ/tháng giai đoạn 2020–2021, rồi lên 2.144 vụ/tháng giai đoạn 2022–2024. Tỷ lệ có thương tích tăng từ 25,50% lên 28,19% giữa giai đoạn đầu và cuối.
2. **Q2 — Phát hiện bất ngờ nhất.** Số vụ trong bóng tối tăng từ 451 lên 1.036 sau đổi giờ, cao hơn ở cả bảy năm. Số vụ giờ cao điểm tính trên mọi điều kiện ánh sáng chỉ tăng từ 1.517 lên 1.631. Chênh lệch tỷ lệ có thương tích là −2,17 điểm phần trăm (KTC 95% −7,19 đến +2,64).
3. **Q3 — Kết quả về mưa nhạy với trọng số.** Ghép đủ 181.051 bản ghi theo ngày. Chênh lệch tỷ lệ có thương tích giữa mưa và quang đãng là +1,38 điểm phần trăm khi ưu tiên các nhóm có dữ liệu ở cả hai điều kiện. Ước lượng đổi thành −3,94 điểm phần trăm với trọng số theo tổng số bản ghi của mỗi nhóm.
4. **Q4 — Mô hình theo giờ và lịch cải thiện ít so với baseline.** Logistic Regression đạt AP 0,322 so với 0,286 của baseline trên tập kiểm tra 2023–2024. Ở ngưỡng chọn từ validation, mô hình phát hiện 86,94% ca có thương tích và gắn cờ gần 85 trên 100 vụ, chưa đủ cơ sở cho ứng dụng điều phối.
5. **Q5–Q6 — Thứ hạng phụ thuộc nhóm so sánh.** Trong các nhãn có ít nhất 500 bản ghi, tình trạng thể chất của tài xế có tỷ lệ thương tích nặng cao nhất (11,85%). Thứ hạng thay đổi theo loại va chạm. Tại giao lộ, tỷ lệ chuẩn hóa là 3,83% với đèn tín hiệu, 2,80% với biển stop/đèn nháy và 3,45% khi không có thiết bị. Thứ tự giữa các thiết bị thay đổi trong từng nhóm va chạm.

### Hạn chế và hướng phát triển

Các tỷ lệ tính trên những vụ có trong bản Kaggle. Dữ liệu thiếu lưu lượng giao thông, vị trí chi tiết, thông tin điều phối và mã duy nhất để xác nhận vụ trùng. Biên bản và quan trắc NOAA tại một trạm mô tả thời tiết ở hai thang khác nhau. So sánh theo thời gian hoặc theo nhóm còn chịu ảnh hưởng của cách báo cáo và các yếu tố chưa quan sát như tốc độ hay thiết kế giao lộ.

Bước tiếp theo là ghép lưu lượng theo giờ, quan trắc thời tiết theo giờ ở nhiều trạm và dữ liệu hình học giao lộ. Với Q4, cần thử trên dữ liệu có thời điểm nhận tin và kết quả điều phối thực tế.

## Cách chạy

Nếu chưa có bản local, tải repo trước.

```bash
git clone https://github.com/Tam-Khuyen/Traffic-Accidents.git
cd Traffic-Accidents
```

Từ terminal có Conda, chạy các lệnh sau trong thư mục repo.

```bash
conda env create -f environment.yml
conda activate p4ds
jupyter lab
```

Repo dùng bản ZIP `data/traffic_accidents.zip`. Nếu ZIP thiếu, lấy bản 1 từ trang Kaggle đã dẫn và đặt đúng tên, hoặc đặt CSV gốc tại `data/raw/traffic_accidents.csv`. File NOAA nhỏ nằm trong `data/reference/` để Q3 có thể chạy với dữ liệu địa phương.

Trong Jupyter, chọn kernel của môi trường `p4ds` và chạy **Run All** theo thứ tự:

1. [01_collection_exploration.ipynb](notebooks/01_collection_exploration.ipynb) — tạo `data/raw/` từ ZIP khi cần và ghi `data/processed/traffic_accidents_clean.csv`.
2. [02_analysis_q1_q2.ipynb](notebooks/02_analysis_q1_q2.ipynb).
3. [02_analysis_q3.ipynb](notebooks/02_analysis_q3.ipynb).
4. [02_analysis_q5_q6.ipynb](notebooks/02_analysis_q5_q6.ipynb).
5. [03_ml_question.ipynb](notebooks/03_ml_question.ipynb).

Các CSV gốc và đã xử lý được tạo khi chạy và nằm trong `.gitignore`. Các hàm dùng chung ở [`src/`](src/). Nếu đã có môi trường `p4ds`, cập nhật bằng `conda env update -n p4ds -f environment.yml`.

## Thuyết trình

[Slide trình bày](slides.pdf) theo nhịp 15 phút. Hỏi đáp khoảng 10 phút.

| Slide | Người trình bày | Thời lượng |
|---|---|---:|
| 1 | Kiệt — mở đầu | 0:35 |
| 2–4 | Hưng — dữ liệu, Q1 và Q2 | 5:20 |
| 5–7 | Hải — Q3 và Q4 | 4:55 |
| 8–11 | Kiệt — Q5, Q6, tổng kết và chuyển sang hỏi đáp | 4:10 |

Xem [nhật ký hỗ trợ LLM](LLM_USAGE.md) để biết công cụ đã hỗ trợ ở những phần nào.
