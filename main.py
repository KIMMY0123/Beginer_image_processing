import cv2

img = cv2.imread("cat.webp") # อ่านภาพจากโฟดเดอร์เดียวกัน

resize = cv2.resize(img, (300, 300)) # ลด-ขยายภาพ

crop = img[7:265, 65:300] # ตัดแต่งภาพ !! img[y1:y2, x1:x2] !!

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # เปลี่ยนสีภาพ

blur = cv2.GaussianBlur(gray, (15,15), 0) # เบลอภาพ

edges = cv2.Canny(blur, 100, 200) # ทำเส้นขอบของรูปตามความเข้มของภาพ(ขึ้นอยู่กับการเบลอ)

#============================= show image ===================================#
cv2.imshow("Original Image", img)
cv2.imshow("Resize Image", resize)
cv2.imshow("Crop Image", crop)
cv2.imshow("Gray Image", gray)
cv2.imshow("Blur Image", blur)
cv2.imshow("Edges Image", edges)
#===========================================================================#


cv2.waitKey(0)
cv2.destroyAllWindows()