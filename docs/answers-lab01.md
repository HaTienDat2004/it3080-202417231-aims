# Câu hỏi thảo luận Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- Cấu hình `--global` được lưu tại `~/.gitconfig` trong thư mục người dùng, áp dụng cho mọi repo trên máy.
- Cấu hình `--local` được lưu tại `.git/config` của riêng từng repo, chỉ có tác dụng trong repo đó và được ưu tiên hơn `--global`.

## 2. Vì sao dùng `git mv`?
- `git mv` vừa di chuyển tệp trong thư mục làm việc vừa tự động ghi nhận thao tác đổi đường dẫn vào vùng Staging Area, giúp giữ nguyên và dễ dàng truy vết lịch sử thay đổi của tệp với `git log --follow`.

## 3. `release/lab01` có phải là baseline không?
- Có. Đây là phiên bản ổn định đã hoàn thành các yêu cầu của Lab 01, được đóng băng để nộp bài và chỉ thay đổi qua quy trình kiểm soát (hotfix).

## 4. Vì sao không commit thẳng lên `master` dù làm một mình?
- Giúp nhánh `master` luôn ở trạng thái ổn định, tách biệt các thay đổi đang phát triển sang nhánh riêng và kiểm soát chất lượng thay đổi qua Pull Request trước khi gộp.
