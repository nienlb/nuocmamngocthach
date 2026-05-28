# Apply CSS từ Design Tokens

Đồng bộ `design-tokens.json` → `css/base.css` cho project Nước Mắm Ngọc Thạch.

## Các bước thực hiện

1. **Đọc `design-tokens.json`** — hiểu các token hiện tại (màu, font, spacing).

2. **Chạy script generate:**
   ```bash
   python3 scripts/generate-tokens.py
   ```

3. **Xác nhận output** — đọc phần `:root {}` trong `css/base.css` vừa được sinh ra, kiểm tra các biến CSS đã đúng chưa.

4. **Báo cáo kết quả** theo định dạng:
   - Liệt kê các màu chính đã được apply (primary, secondary, accent)
   - Ghi chú nếu có token nào trông bất thường
   - Nhắc lại lệnh chạy nếu cần chỉnh thêm: `python3 scripts/generate-tokens.py`

## Lưu ý
- Không tự ý sửa `css/base.css` — file này là auto-generated.
- Nếu muốn thay đổi màu, hướng dẫn user edit `design-tokens.json` trước, rồi mới chạy lệnh.
- Các file CSS section (`css/sections/*.css`) dùng variables từ `base.css`, không cần động vào khi đổi màu.
