"""
OpenCVが正しくインストールされているか確認するプログラム
rectangle.png が表示されれば良い
"""
import cv2

img = cv2.imread("rectangle.png")

cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
