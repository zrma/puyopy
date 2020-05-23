import os

from field import RenderField
from timer import Timer

# Windows
if os.name == 'nt':
    def clear():
        os.system('cls')

# Posix (Linux, OS X)
else:
    def clear():
        os.system('clear')


class Renderer:
    @staticmethod
    def init():
        __class__.__fps_count = 0
        __class__.__fps = 0
        __class__.__accumulated_elapsed_render_time = Timer.get_elapsed()
        __class__.__prev_tick = 0.0

    @staticmethod
    def render_begin(field: RenderField) -> bool:
        elapsed_time = Timer.get_elapsed()
        __class__.__accumulated_elapsed_render_time += elapsed_time
        __class__.__prev_tick += elapsed_time

        # 5FPS(1초에 5번) 화면에 그리기 위해서
        if __class__.__accumulated_elapsed_render_time < 0.2:
            return False

        __class__.__field = field
        __class__.__accumulated_elapsed_render_time = 0.0
        __class__.__fps_count += 1

        if __class__.__prev_tick > 1.0:
            __class__.__fps, __class__.__fps_count = __class__.__fps_count, 0
            __class__.__prev_tick -= 1.0

        clear()

        return True

    @staticmethod
    def render_end():
        __class__.__field.render()
        print(f"FPS : {__class__.__fps}")

    @staticmethod
    def render(data, position: tuple):
        assert isinstance(position, tuple)
        __class__.__field.set_render_data(data, position)

    @staticmethod
    def set_color(color):
        pass

    @staticmethod
    def set_bg_color(color):
        pass

    __field = None
    __screen = None
    __color = None
    __bg_color = None
    __fps_count = 0
    __fps = 0
    __accumulated_elapsed_render_time = 0.0
    __prev_tick = 0.0
