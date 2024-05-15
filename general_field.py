from PIL import Image, ImageDraw

# Создаем новое изображение размером 400x400 пикселей
image = Image.new("RGB", (300, 380), "white")
draw = ImageDraw.Draw(image)

# Определяем координаты прямоугольника и его размеры
x1, y1 = 0, 0
x2, y2 = 300, 380

# Рисуем горизонтальные линии сетки
for y in range(y1, y2+1, 55):
    draw.line([(x1, y), (x2, y)], fill="black")

# Рисуем вертикальные линии сетки
for x in range(x1, x2+1, 60):
    draw.line([(x, y1), (x, y2)], fill="black")

# Рисуем прямоугольник
draw.rectangle([(x1, y1), (x2, y2)], outline="black")

# Сохраняем изображение
image.save("grid_rectangle.png")