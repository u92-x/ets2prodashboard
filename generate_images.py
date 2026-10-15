import os
import math
from PIL import Image, ImageDraw, ImageFont

os.makedirs('static/img', exist_ok=True)

def create_real_gauge(filename, title, unit, ticks, is_rpm=False):
    size = 500
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center = size // 2
    radius = 200
    
    draw.ellipse([20, 20, size-20, size-20], fill="#141414", outline="#444444", width=8)
    draw.ellipse([35, 35, size-35, size-35], fill="#0a0a0a", outline="#222222", width=3)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        font_title = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        font_title = font

    num_ticks = len(ticks)
    start_angle = 140
    end_angle = 400  
    
    for i, label in enumerate(ticks):
        current_angle = start_angle + (i / (num_ticks - 1)) * (end_angle - start_angle)
        angle_rad = math.radians(current_angle)
        
        x1 = center + (radius - 25) * math.cos(angle_rad)
        y1 = center + (radius - 25) * math.sin(angle_rad)
        x2 = center + (radius - 12) * math.cos(angle_rad)
        y2 = center + (radius - 12) * math.sin(angle_rad)
        
        # Czerwone kreski od wartości 24 (indeks 4 z 6)
        color = "#cc0000" if is_rpm and i >= 4 else "#aaaaaa"
        draw.line([x1, y1, x2, y2], fill=color, width=3)
        
        tx = center + (radius - 60) * math.cos(angle_rad)
        ty = center + (radius - 60) * math.sin(angle_rad)
        
        bbox = draw.textbbox((0, 0), str(label), font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((tx - tw/2, ty - th/2), str(label), fill="#ffffff", font=font)

    if is_rpm:
        red_start_angle = start_angle + (4 / (num_ticks - 1)) * (end_angle - start_angle)
        for a in range(int(red_start_angle), int(end_angle)):
            ra = math.radians(a)
            ax1 = center + (radius - 30) * math.cos(ra)
            ay1 = center + (radius - 30) * math.sin(ra)
            ax2 = center + (radius - 22) * math.cos(ra)
            ay2 = center + (radius - 22) * math.sin(ra)
            draw.line([ax1, ay1, ax2, ay2], fill="#cc0000", width=4)

    draw.text((center - 25, center - 35), title, fill="#888888", font=font_title)
    draw.text((center - 45, center + 35), unit, fill="#666666", font=font_title)

    img.save(f'static/img/{filename}', 'PNG')
    print(f"Generated: static/img/{filename}")

create_real_gauge('speed.png', 'SPEED', 'km/h', [0, 20, 40, 60, 80, 100, 120, 140])
create_real_gauge('rpm.png', 'RPM', 'x100 r/min', [0, 6, 12, 18, 24, 30], is_rpm=True)
create_real_gauge('fuel.png', 'FUEL', '1/1', ['0', '1/4', '1/2', '3/4', '1/1'])
create_real_gauge('temp.png', 'TEMP', '°C', [40, 60, 80, 100, 120])
