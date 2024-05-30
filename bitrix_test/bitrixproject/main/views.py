from django.shortcuts import render
from .models import StoredRequests
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip

def generate_running_line(request, text):
    StoredRequests.objects.create(request=request, text=text)

    # Параметры итогового видео
    width = 100
    height = 100
    screensize = (width, height)
    duration = 3

    # Чёрный фон для видео
    bg_clip = ColorClip(size=screensize, color=(0, 0, 0)).set_duration(duration)

    # Жёлтый текст для видео
    txt_clip = TextClip(text, fontsize=30, color='yellow').set_duration(duration)

    # Размеры текста
    textclip_width, textclip_height = txt_clip.size

    # Функция изменения позиции текста
    def translate(t):
        # Задаём стартовую и конечную позицию текста
        start_pos = (0, height/2-textclip_height/2)
        end_pos = (width/2 -textclip_width, height/2-textclip_height/2)

        # Вычисляем положение x и y на основе прошедшего времени и общей продолжительности
        x = int(start_pos[0] + t/duration * (end_pos[0] - start_pos[0]))
        y = int(start_pos[1] + t/duration * (end_pos[1] - start_pos[1]))

        return (x, y)

    # Устанавливаем позицию текста с пощью ранее созданной функции
    txt_moving = txt_clip.set_position(translate)

    # Собираем итоговое видео из фона и бегущего текста
    video = CompositeVideoClip([bg_clip, txt_moving])

    video_file_path = "/content/bitrix_test_view/bitrix_test/bitrixproject/video/scrolling_text.mp4"
    video.write_videofile(video_file_path, fps=60)

    return render(request, 'main/index.html')
