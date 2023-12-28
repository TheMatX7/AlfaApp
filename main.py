from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import AsyncImage
from bs4 import BeautifulSoup
import requests
from io import BytesIO

class AlfaApp(App):
    def build(self):
        # Tworzenie zarządcy ekranów
        sm = ScreenManager()

        # Ekran Menu
        menu_screen = Screen(name='menu')
        menu_layout = BoxLayout(orientation='vertical', padding=10)

        # Górny pasek z tytułem
        title_label = Label(text='Alfa - New Age', font_size=24)
        menu_layout.add_widget(title_label)

        # Przyciski
        tasks_button = Button(text='Zadania', on_press=self.show_tasks)
        profile_button = Button(text='Profil', on_press=self.show_profile)
        exit_button = Button(text='Wyjście', on_press=self.exit_app)

        menu_layout.add_widget(tasks_button)
        menu_layout.add_widget(profile_button)
        menu_layout.add_widget(exit_button)

        menu_screen.add_widget(menu_layout)
        sm.add_widget(menu_screen)

        # Ekran Zadania
        tasks_screen = Screen(name='tasks')
        tasks_layout = BoxLayout(orientation='vertical', padding=10)

        # Pobierz dane ze strony internetowej
        url = 'https://thematx7.github.io/test-alfa-app/'  # Podmień to na właściwy adres URL
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Pobierz dane z elementów HTML
            image_url = soup.find('img')['src']
            goal = soup.find('div', class_='goal').text
            age = soup.find('div', class_='age').text
            location = soup.find('div', class_='location').text
            intention = soup.find('div', class_='intention').text

            # Wyświetl obraz zamiast linku
            image = AsyncImage(source=image_url, allow_stretch=True, size=(300, 300))
            tasks_layout.add_widget(image)

            # Aktualizuj etykietę z danymi
            data_label = Label(
                text=f'Cel: {goal}\nWiek: {age}\nLokalizacja: {location}\nZamiar: {intention}',
                font_size=16
            )
            tasks_layout.add_widget(data_label)

            # Przycisk "Wróć"
            back_button = Button(text='Wróć', on_press=self.show_menu, background_color=(0.2, 0.7, 0.3, 1),
                                 size_hint=(None, None), size=(100, 50))
            tasks_layout.add_widget(back_button)
        else:
            data_label = Label(text='Błąd pobierania danych')
            tasks_layout.add_widget(data_label)

        tasks_screen.add_widget(tasks_layout)
        sm.add_widget(tasks_screen)

        return sm

    def show_tasks(self, instance):
        # Przełącz na ekran Zadania
        self.root.current = 'tasks'

    def show_menu(self, instance):
        # Przełącz na ekran Menu
        self.root.current = 'menu'

    def show_profile(self, instance):
        # Tutaj możesz dodać kod do przejścia do sekcji Profil
        print('Przejście do sekcji Profil')

    def exit_app(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    AlfaApp().run()
