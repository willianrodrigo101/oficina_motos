from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.login_screen import LoginScreen

class HomeDono(Screen):
    pass

class HomeFuncionario(Screen):
    pass

class OficinaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeDono(name='home_dono'))
        sm.add_widget(HomeFuncionario(name='home_funcionario'))
        return sm

if __name__ == '__main__':
    OficinaApp().run()

