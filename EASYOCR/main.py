import streamlit as st
import home , about
from streamlit_option_menu import option_menu


class MultiApp:
    def __init__(self):
        self.apps = []
    
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })

    def run ():
        #create top navigation bar
        app = option_menu(
            menu_title = None,
            options = ["Home","About"],
            icons=["house-door-fill","code-slash"],
            orientation="horizontal",
            default_index = 0
            ) 
        #run this page if selected
        if app == "Home":
            home.app()
        if app == "About":
            about.app()
    
    run()