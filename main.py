from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file('design.kv')


class MyLayout(Widget):
    button_1_var = ObjectProperty(None)
    label_var = ObjectProperty(None)


    def on_button_click(self, instance):
        self.label_var.text = "Label of " + instance.text
        # print(f"Button {instance.text} was clicked!")


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
