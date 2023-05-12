from otree.api import *
import random



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Thesis'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    payment_per_correct_answer = cu(1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(label='Выберете Ваш пол ', choices=["м", "ж", "другое"],)
    zodiac = models.StringField(label='Какой Ваш знак зодиака?', choices=["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"],)
    city = models.StringField(label='В каком городе Вы родились?',)
    hobby = models.StringField(label='Напишите Ваши хобби (можно несколько, через запятую)', )
    bs = models.IntegerField(label='Сколько братьев и сестер у Вас есть?',min=0)
    color = models.StringField(label='Какой Ваш любимый цвет?', )
    corr = models.StringField(label='Как Вы считаете, коэффециент корреляции 0.4 это', choices=["маленькая корреляция", "средняя корреляция", "высокая корреляция"],)
    email = models.StringField(label='Напишите, пожалуйста, адрес вашей электронной почты (необходимо для выплаты выигрыша)', )
    place = models.IntegerField(label='Как Вы помните/думаете Вы находитесь в первой или во второй половине рейтинга по GPA?', choices=[1,2],)
    question_answer = models.StringField()
    number1 = models.IntegerField(min=0, max=100)
    number2 = models.IntegerField(min=0, max=100)
    number3 = models.IntegerField(min=0, max=100)
    ran=models.IntegerField()
    can_gender=models.StringField()
    can_city = models.StringField()
    can_zodiac = models.StringField()
    can_bs = models.IntegerField()
    can_hobby = models.StringField()
    can_color = models.StringField()
    mid_math = models.FloatField()
    final_math = models.FloatField()
    mid_essay = models.FloatField()
    final_essay = models.FloatField()
    sh = models.IntegerField()
    payoff1 = models.CurrencyField()
    payoff2 = models.CurrencyField()
    payoff3 = models.CurrencyField()
    payoff4 = models.CurrencyField()
    risk = models.IntegerField(label='Ответ:', choices=[1,2,3,4,5,6], )

# PAGES

class FirstPage(Page):
    form_model = "player"

    @staticmethod
    def vars_for_template(player: Player):
        sh = random.randint(0, 1)
        player.sh=sh
        if sh == 0:
            link = 'эссе на тему "Выберите какую-либо реформу или блок реформ 1990-х годов в одной из республик бывшего СССР, кроме России (после 21.08.1991). Какие из связанных с этой реформой проблем могли бы быть интересны для экономического исследования и почему?"'
        elif sh == 1:
            link = '<a href="https://drive.google.com/file/d/1Gj_MJF8RwUuL9_lB8AUUO4Xcbf6nZB9l/view?usp=sharing" target="_task">данное задание </a>'

        return{"sh": sh, "link": link }

class Question(Page):
    form_model = "player"
    
    @staticmethod
    def vars_for_template(player: Player):
        question = random.randint(0, 2)
        if question == 0:
            q = 'Если Вы готовы приступить к эксперименту, нажмите на кнопку ниже'
            form_fields = []
        elif question == 1:
            q = "На какие факторы Вы бы обратили внимание при выборе кандидата для этого теста, если бы у Вас был доступ ко всем данным кандидатов?"
            form_fields = ["question_answer"]
        elif question == 2:
            q = "Kак Вы думаете, влияет ли пол на вероятность успеха при выполнении подобных работ?"
             form_fields = ["question_answer"]
        return {"q":q,
               "form_fields": form_fields}

class Simple_CV(Page):
    form_model = "player"
    form_fields = ["number1"]

    def vars_for_template(player: Player):
        cv = {'gender': ['м', 'м', 'ж', 'ж', 'м', 'м', 'ж', 'ж', 'м', 'ж', 'м', 'ж', 'м', 'ж', 'м', 'ж', 'ж', 'ж', 'м',
                         'ж', 'м', 'м', 'м', 'ж', 'ж', 'м', 'ж', 'ж'],
              'zodiac': ['рыбы', 'водолей', 'водолей', 'лев', 'дева', 'дева', 'рыбы', 'овен', 'весы', 'лев', 'дева',
                         'рак', 'водолей', 'стрелец', 'рак', 'скорпион', 'лев', 'рак', 'телец', 'весы', 'дева',
                         'близнецы', 'близнецы', 'весы', 'рыбы', 'овен', 'лев', 'дева'],
              'city': ['Население не менее 500 тыс.чел. и не более 2 млн.чел.', 'Население более 6 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.', 'Население более 6 млн.чел.',
                       'Население более 6 млн.чел.', 'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.', 'Население более 6 млн.чел.',
                       'Население более 6 млн.чел.', 'Население более 2 млн.чел. и неболее 6 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население более 2 млн.чел. и неболее 6 млн.чел.',
                       'Население более 2 млн.чел. и неболее 6 млн.чел.', 'Население более 6 млн.чел.',
                       'Население более 6 млн.чел.', 'Население более 2 млн.чел. и неболее 6 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.', 'Население более 6 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.', 'Население более 6 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.',
                       'Население не менее 500 тыс.чел. и не более 2 млн.чел.'],
              'hobby': ['зимние виды спорта,настольные игры', 'летние виды спорта',
                        'зимние виды спорта,настольные игры,путешествия',
                        'рисование,спортивный зал,просмотр видеоконтента', 'летние виды спорта,фотография',
                        'спортивный зал,создание видео', 'спортивный зал,путешествия', 'спортивный зал',
                        'дайвинг,рыбалка,видеоигры', 'зимние виды спорта,кулинария', 'энология(изучение вина и виноделия),зимние виды спорта',
                        'дизайн', 'танцы,летние виды спорта', 'спортивный зал,кулинария',
                        'летние виды спорта,кулинария,компьютерные игры', 'летние виды спорта,рисование,чтение',
                        'танцы,кулинария', 'зимние виды спорта,летние виды спорта', 'летние виды спорта',
                        'летние виды спорта,просмотр видеоконтента', 'летние виды спорта,компьютерные игры',
                        'настольные игры,летние виды спорта', 'летние виды спорта',
                        'кулинария,спортивный зал,игра на гитаре', 'просмотр видеоконтента,настольные игры',
                        'игра на гитаре', 'просмотр видеоконтента,рукоделие', 'летние виды спорта,чтение'],
              'bs': [2, 2, 0, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 0, 1, 3, 0, 0],
              'color': ['зеленый', 'синий', 'оранжевый', 'синий', 'оранжевый', 'синий', 'голубой', 'белый', 'красный',
                        'синий', 'красный', 'синий', 'черный', 'розовый', 'голубой', 'черный', 'голубой', 'голубой',
                        'синий', 'зеленый', 'синий', 'синий', 'синий', 'цвет морской волны', 'зеленый', 'черный',
                        'синий', 'синий'],
              'mid_math': [86.5, 36.5, 48.0, 80.7, 7.6, 57.6, 90.3, 17.3, 61.5, 19.2, 3.8, 34.6, 92.3, 18.0, 23.0, 65.3,
                           28.8, 65.3, 44.2, 44.0, 17.3, 48.0, 100.0, 55.7, 90.3, 53.8, 73.0, 28.8],
              'final_math': [87.5, 12.5, 32.1, 50.0, 14.2, 30.3, 39.2, 51.7, 57.1, 69.6, 10.7, 66.0, 80.3, 25.0, 33.9,
                             44.6, 50.0, 55.3, 66.0, 75.0, 35.2, 73.2, 98.0, 26.7, 41.0, 83.9, 83.9, 91.0],
              'mid_essay': [84.6, 84.5, 36.5, 9.6, 23.0, 36.5, 36.5, 63.4, 84.6, 100.0, 23.0, 23.0, 63.4, 37.0, 36.5,
                            63.4, 63.4, 63.4, 9.6, 87.0, 63.4, 23.0, 100.0, 84.6, 100.0, 84.6, 100.0, 100.0],
              'final_essay': [6.2, 14.5, 14.5, 14.5, 29.1, 29.1, 29.1, 29.1, 29.1, 29.1, 41.6, 41.6, 41.6, 42.0, 60.4,
                              60.4, 60.4, 60.4, 72.9, 73.0, 85.4, 85.4, 85.4, 100.0, 100.0, 100.0, 100.0, 100.0]}
        ran = random.randint(0, 27)
        gender = cv['gender'][ran]
        zodiac = cv['zodiac'][ran]
        city = cv['city'][ran]
        hobby = cv['hobby'][ran]
        bs = cv['bs'][ran]
        color = cv['color'][ran]
        mid_math = cv['mid_math'][ran]
        final_math = cv['final_math'][ran]
        mid_essay = cv['mid_essay'][ran]
        final_essay = cv['final_essay'][ran]
        player.ran=ran
        player.can_gender=gender
        player.can_zodiac=zodiac
        player.can_city=city
        player.can_hobby=hobby
        player.can_bs=bs
        player.can_color=color
        player.mid_math=mid_math
        player.final_math=final_math
        player.mid_essay=mid_essay
        player.final_essay=final_essay
        return{'gender': gender, 'zodiac': zodiac, 'city': city, 'hobby': hobby, 'bs': bs, 'color': color,
               'mid_math': mid_math, 'final_math': final_math,
               'mid_essay': mid_essay, 'final_essay': final_essay, 'ran': ran}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        fm = player.final_math
        fe = player.final_essay

        if player.sh==0:
            if fe>50:
                player.payoff1 = C.payment_per_correct_answer*player.number1
            else:
                player.payoff1 = C.payment_per_correct_answer * (100-player.number1)
        elif player.sh == 1:
            if fm>50:
                player.payoff1 = C.payment_per_correct_answer*player.number1
            else:
                player.payoff1 = C.payment_per_correct_answer * (100-player.number1)

class Test_CV(Page):
    form_model = "player"
    form_fields = ["number2"]

    @staticmethod
    def vars_for_template(player: Player):
        if player.sh == 0:
            mid=player.mid_essay
            mid_text='эссе на тему «Можно ли было плавно реформировать советскую экономику?»'
        elif player.sh == 1:
            mid=player.mid_math
            mid_text = '<a href="https://drive.google.com/file/d/1PtRnJ76bmSMrridTYoDBTAb3FIe_gjK5/view?usp=sharing" target="_task_2">Задание</a>'
        return { 'gender': player.can_gender,
                 'zodiac': player.can_zodiac,
                 'city': player.can_city,
                 'bs': player.can_bs,
                 'hobby': player.can_hobby,
                 'color': player.can_color,
                 'mid': mid,
                 'mid_text': mid_text
        }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        fm = player.final_math
        fe = player.final_essay
        if player.sh==0:
            if fe>50:
                player.payoff2 = C.payment_per_correct_answer*player.number2
            else:
                player.payoff2 = C.payment_per_correct_answer * (100-player.number2)
        elif player.sh == 1:
            if fm>50:
                player.payoff2 = C.payment_per_correct_answer*player.number2
            else:
                player.payoff2 = C.payment_per_correct_answer * (100-player.number2)


class Corr_CV(Page):
    form_model = "player"
    form_fields = ["number3"]
    @staticmethod
    def vars_for_template(player: Player):
        if player.sh ==0:
            mid=player.mid_essay
            mid_text='"Эссе на тему «Можно ли было плавно реформировать советскую экономику?»"'

        else:
            mid=player.mid_math
            mid_text ='https://drive.google.com/file/d/1PtRnJ76bmSMrridTYoDBTAb3FIe_gjK5/view?usp=sharing'
        return { 'gender': player.can_gender,
                 'zodiac': player.can_zodiac,
                 'city': player.can_city,
                 'bs': player.can_bs,
                 'hobby': player.can_hobby,
                 'color': player.can_color,
                 'mid': mid,
                 'mid_text': mid_text }
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        fm = player.final_math
        fe = player.final_essay
        if player.sh==0:
            if fe>50:
                player.payoff3 = C.payment_per_correct_answer*player.number3
            else:
                player.payoff3 = C.payment_per_correct_answer * (100-player.number3)
        elif player.sh == 1:
            if fm>50:
                player.payoff3 = C.payment_per_correct_answer*player.number3
            else:
                player.payoff3 = C.payment_per_correct_answer * (100-player.number3)


class Survey(Page):
    form_model = "player"
    form_fields = ["gender", "zodiac", "city", "hobby", "bs", "color", "place", "corr", "email"]

class Risk(Page):
    form_model = "player"
    form_fields = ["risk"]
    @staticmethod
    def  before_next_page(player: Player, timeout_happened):
        lot = random.randint(0, 1)
        if lot == 0:
            if player.risk==1:
                player.payoff4=C.payment_per_correct_answer*70
            elif player.risk==2:
                player.payoff4=C.payment_per_correct_answer*60
            elif player.risk==3:
                player.payoff4=C.payment_per_correct_answer*50
            elif player.risk==4:
                player.payoff4=C.payment_per_correct_answer*40
            elif player.risk==5:
                player.payoff4=C.payment_per_correct_answer*30
            elif player.risk==6:
                player.payoff4=C.payment_per_correct_answer*10   
        elif lot == 1:
            if player.risk==1:
                player.payoff4=C.payment_per_correct_answer*70
            elif player.risk==2:
                player.payoff4=C.payment_per_correct_answer*90
            elif player.risk==3:
                player.payoff4=C.payment_per_correct_answer*110
            elif player.risk==4:
                player.payoff4=C.payment_per_correct_answer*130
            elif player.risk==5:
                player.payoff4=C.payment_per_correct_answer*150
            elif player.risk==6:
                player.payoff4=C.payment_per_correct_answer*170 
        

class Results(Page):
    @staticmethod
    def is_displayed(player:Player):
        return player.round_number == C. NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        combined_payoff=player.payoff1 + player.payoff2 + player.payoff2 + player.payoff4

        return{
            "combined_payoff":combined_payoff
        }
page_sequence = [FirstPage,Question,Simple_CV, Test_CV, Corr_CV , Risk, Survey, Results]
