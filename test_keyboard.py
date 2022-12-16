# from PIL import Image, ImageColor, ImageFont
# from PIL import ImageDraw
# angel = 72
#
#
# image = Image.new("RGB", (600, 400))
# draw = ImageDraw.Draw(image)
#
# for ang in range(1, 6):
#     if ang == 2:
#         color = 'red'
#     else:
#         color = 'white'
#     start = (angel * ang) - 122
#     end = 72 + (angel * ang) - 122
#     print(f"ang {ang} start={start} end={end}")
#     draw.pieslice(
#         xy=(150, 50, 450, 350),
#         start=start, end=end, fill=color,
#         outline=(0, 0, 0)
#     )
# image.show()
