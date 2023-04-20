class InfoDataSet():
    def __init__(self) -> None:
        self.context = [{'title':'О нас', 'url_name':'about_info', 'order': '0'},
                        {'title':'Оплата', 'url_name':'payment_info', 'order': '0'},
                        {'title':'Гарантии', 'url_name':'guarantees_info', 'order': '0'},
                        {'title':'Возврат', 'url_name':'return_info', 'order': '0'},
                        {'title':'Контакты', 'url_name':'contacts_info', 'order': '1'},
                        {'title':'Помощь', 'url_name':'help_info', 'order': '1'}]
    
    def getContext(self):
        return self.context