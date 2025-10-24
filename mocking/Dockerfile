# Sử dụng image Node.js phiên bản lightweight (Alpine)
FROM node:18-alpine

# Thiết lập thư mục làm việc bên trong container
WORKDIR /usr/src/app

# Cài đặt Mountebank global. Sử dụng phiên bản ổn định mới nhất.
# Ghi chú: Có thể chỉ định phiên bản nếu cần (ví dụ: mountebank@2.0.0)
RUN npm install -g mountebank

# Sao chép file cấu hình imposters vào container
COPY imposters.json .

# Cổng mặc định của Mountebank để quản lý (API và UI)
EXPOSE 2525
# Cổng của imposter (giả lập) chúng ta đã định nghĩa trong imposters.json
EXPOSE 4545

# Khởi động Mountebank với file cấu hình
# --allowInjection: Cho phép injection code nếu bạn có các kịch bản nâng cao.
# --localOnly false: Quan trọng để Mountebank có thể được truy cập từ bên ngoài container.
CMD ["mb", "--config", "imposters.json", "--allowInjection", "--localOnly", "false", "--pidfile", "/dev/null"]
