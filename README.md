## Nhóm 14 lớp 48K22.3

## Thành viên
  `Cao Tiến Hải`

  `Phạm Hưng`

  `Văn Thị Kim Anh`

  `Phạm Thị Minh Tâm` 

  `Huỳnh Thị Thúy Vy`

## Giới thiệu
  **Đây là dự án cuối kỳ trong khuôn khổ môn học `Lập Trình Web` do `Tiến sĩ Đặng Trung Thành` giảng dạy ở kỳ 1 năm học 2024-2025.**
  **Trong dự án này, nhóm xây dựng một Website mô phỏng quy trình CMS của trang báo điện tử lớn nhất Việt Nam `VNExpress`**. 
  **Dự án sử dụng thư viện Django của Python để triển khai và sử dụng phương pháp triển khai Server-Side Rendering bám sát với kiến thức học tập ở lớp cũng như giáo trình.**

## Mục tiêu
  **Hiểu rõ cách thức hoạt động của một Website, nắm chắc kiến thức cơ bản của ngôn ngữ `Python`, `JavaScript`, `HTML` và `CSS`**
  **Tạo tiền đề cho việc phát triển của những bạn học trái ngành, học ngách,...**

## Triển khai cấu trúc thư mục
  - Folder `cms` là app gốc của dự án
  - Folder `myapp` là app chứa các file liên quan tới đối tượng `Client` của Website
  - Folder `processing` là app chứa các file liên quan tới việc xử lý bài viết, trung tâm CMS, danh cho đối tượng `Contributor`, `Editor`, `Approver`
  - Folder `manager` là app chứa các file liên quan tới thống kê Website dành cho đối tượng `Approver`
  - Folder `static` là folder chứa các file tĩnh bao gồm hình ảnh, audio, JavaScript, CSS sử dụng cho các template
  - Folder `templates` là folder chứa các file HTML render ra Website
  - Folder `media` là folder chứa các file hình ảnh, nội dung,... khi người dùng upload lên Website
  - File `.gitignore` là file chứa tên các file, folde để khi khởi tạo Git sẻ bỏ qua
  - File `.env` chứa các biến có độ bảo mật cao, không muốn cho người xem GitHub thấy và sử dụng
  - File `requirements.txt` là file chứa tên và phiên bản của thư viện cần cài đặt để khởi chạy dự án