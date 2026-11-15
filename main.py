from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.camera import Camera
from kivy.clock import Clock
import requests
import io

class LibraryScanner(App):
    def build(self):
        self.title = "Сканер библиотеки"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Поле для ввода IP
        layout.add_widget(Label(text="IP компьютера (например 192.168.1.10:8000):", size_hint=(1, 0.1)))
        self.ip_input = TextInput(
            text="192.168.1.10:8000", 
            multiline=False,
            size_hint=(1, 0.1),
            font_size=20
        )
        layout.add_widget(self.ip_input)
        
        # Камера
        self.camera = Camera(play=False, resolution=(1280, 720))
        layout.add_widget(self.camera)
        
        # Кнопка отправки
        self.btn_capture = Button(
            text="📸 Сфотографировать и отправить",
            size_hint=(1, 0.2),
            font_size=24,
            background_color=(0.2, 0.6, 1, 1)
        )
        self.btn_capture.bind(on_press=self.capture_and_send)
        layout.add_widget(self.btn_capture)
        
        # Статус
        self.status_label = Label(text="Готов к работе", size_hint=(1, 0.1), font_size=18)
        layout.add_widget(self.status_label)
        
        return layout

    def capture_and_send(self, instance):
        self.btn_capture.text = "⏳ Отправка..."
        self.btn_capture.disabled = True
        self.status_label.text = "Делаем снимок..."
        Clock.schedule_once(self._do_capture, 1)

    def _do_capture(self, dt):
        if self.camera.texture:
            data = io.BytesIO()
            self.camera.export_to_png(data)
            data.seek(0)
            
            ip = self.ip_input.text.strip()
            if not ip.startswith("http"):
                ip = f"http://{ip}"
            url = f"{ip}/upload"
            
            try:
                files = {'file': ('photo.jpg', data, 'image/jpeg')}
                response = requests.post(url, files=files, timeout=10)
                if response.status_code == 200:
                    self.status_label.text = "✅ Успешно отправлено!"
                    self.status_label.color = (0, 1, 0, 1)
                else:
                    self.status_label.text = f"❌ Ошибка сервера: {response.status_code}"
                    self.status_label.color = (1, 0, 0, 1)
            except Exception as e:
                self.status_label.text = f"❌ Нет связи с ПК"
                self.status_label.color = (1, 0, 0, 1)
        else:
            self.status_label.text = "❌ Камера не готова"
            
        self.btn_capture.text = "📸 Сфотографировать и отправить"
        self.btn_capture.disabled = False

if __name__ == '__main__':
    LibraryScanner().run()