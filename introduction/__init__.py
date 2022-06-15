
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # InformationForm
    name = models.StringField(label="Nama Anda:")
    email = models.StringField(label="Email:")
    accept = models.StringField(label= "Jika anda telah membaca dan memahami informasi yang disampaikan dan BERSEDIA menjadi responden dalam survey ini, silakan pilih 'Ya, Bersedia' . Jika sebaliknya, silakan pilih 'Tidak' *",
                                choices=['Ya, Bersedia', 'Tidak'], 
                                widget=widgets.RadioSelect)

    # EksperimenInfo
    country = models.StringField(label="Apakah nama \"negara\" dalam peneletian ini?")
    tax = models.IntegerField(label="Berapa persenkah tarif pajak yang berlaku di \"negara\" ini? (Tulis angka saja)")
    job = models.IntegerField(label="Dari tiga pilihan ini, apakah pekerjaan Anda di \"negara\" itu? 1) Menteri Keuangan; 2) Auditor/pemeriksa pajak; 3) Pengusaha. (Tulis angka saja)",
                                min=1, max=2)
    method = models.IntegerField(label="Dari dua cara ini, bagaimanakah cara Anda bekerja? 1) Dalam tim; 2) Bekerja sendiri. (Tulis angka saja)",
                                min=1, max=3)
    problem= models.IntegerField(label="Apakah permasalahan utama dalam penelitian ini? 1) Bribery dan Whistleblowing; 2) Ekspor dan Impor; 3) Pariwisata. (Tulis angka saja)",
                                min=1, max=2)
                                

class InformationForm(Page):
    form_model = 'player'
    form_fields = ['name', 'email', 'accept']


class EksperimentInfo(Page):
    form_model = 'player'
    form_fields = ['country', 'tax', 'job', 'method', 'problem']


page_sequence = [InformationForm, EksperimentInfo]