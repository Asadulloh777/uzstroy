from  aiogram.dispatcher.filters.state import State,StatesGroup

class Murojaat(StatesGroup):
    ism_qabuli= State()
    fam_qabuli = State()
    mail_qabuli = State()
    text_qabuli = State()
