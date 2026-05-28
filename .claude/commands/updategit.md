# Update Git — Add, Commit & Push

Commit toàn bộ thay đổi hiện tại và push lên remote.

## Các bước thực hiện

1. **Kiểm tra trạng thái:**
   ```bash
   git status
   git diff --stat
   ```
   Nếu không có thay đổi gì → báo và dừng lại, không tạo commit rỗng.

2. **Xem nội dung thay đổi để soạn commit message:**
   ```bash
   git diff HEAD
   ```

3. **Stage toàn bộ thay đổi:**
   ```bash
   git add -A
   ```

4. **Soạn commit message** dựa trên diff thực tế:
   - Ngắn gọn, tiếng Việt hoặc tiếng Anh tùy nội dung
   - Dùng prefix: `feat:`, `fix:`, `style:`, `refactor:`, `docs:` cho phù hợp
   - Ví dụ: `style: tôn màu tươi sáng hơn cho toàn bộ sections`

5. **Commit:**
   ```bash
   git commit -m "<message vừa soạn>"
   ```

6. **Kiểm tra branch hiện tại và push:**
   ```bash
   git branch --show-current
   git push
   ```
   Nếu branch chưa có upstream: `git push -u origin <branch>`

7. **Báo cáo kết quả** — hash commit, branch, số file thay đổi.

## Lưu ý an toàn
- Không dùng `--force` hay `--no-verify` trừ khi user yêu cầu rõ ràng.
- Nếu push bị reject do remote có commit mới hơn → báo cho user, không tự pull.
- Không commit file `.env` hoặc file chứa thông tin nhạy cảm.
