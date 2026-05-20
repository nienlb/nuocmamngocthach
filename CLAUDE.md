# CLAUDE.md — Nước Mắm Landing Page

## Tổng quan
Landing page giới thiệu và bán nước mắm truyền thống.
Tech stack: HTML/CSS/JS thuần, không có build tool.

## Cấu trúc quan trọng
- `index.html` — file duy nhất, 6 section chính
- `css/base.css` — CSS variables (màu, font, spacing) định nghĩa tại đây
- `docs/brand.md` — màu sắc, font, tone of voice
- `docs/content.md` — nội dung text cho từng section
- `docs/sections.md` — mô tả layout từng section

## Quy tắc khi code
- Dùng CSS variables từ `base.css`, không hardcode màu
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
