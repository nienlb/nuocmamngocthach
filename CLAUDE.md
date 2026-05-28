# CLAUDE.md — Nước Mắm Landing Page

## Tổng quan
Landing page giới thiệu và bán nước mắm truyền thống.
Tech stack: HTML/CSS/JS thuần, không có build tool.

## Cấu trúc quan trọng
- `index.html` — file duy nhất, 6 section chính
- `design-tokens.json` — **nguồn duy nhất** cho màu, font, spacing — chỉ edit tại đây
- `css/base.css` — auto-generated từ design-tokens.json, không edit tay
- `css/sections/*.css` — style từng section, dùng variables từ base.css
- `docs/brand.md` — tone of voice, hình ảnh (không chứa giá trị màu)
- `docs/content.md` — nội dung text cho từng section
- `docs/sections.md` — mô tả layout từng section
- `scripts/generate-tokens.py` — script sync token → CSS

## Slash commands
- `/applycss` — chạy `python3 scripts/generate-tokens.py`, sync design-tokens.json vào css/base.css

## Quy tắc khi code
- **Đổi màu/font/spacing:** edit `design-tokens.json` rồi chạy `/applycss`
- Không hardcode màu trong CSS — dùng variables từ `base.css`
- Class đặt theo BEM: `.section-hero__title`, `.card-product__price`
- Không dùng framework CSS (no Bootstrap, no Tailwind)
- Ảnh đặt đúng thư mục trong `assets/images/`

## Thứ tự section trong index.html
1. `#hero`
2. `#story`
3. `#process`
4. `#products`
5. `#testimonials`
6. `#contact`
