from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'post_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Closing
    gender = models.StringField(choices=["Laki-laki", "Perempuan"], label="Jenis kelamin Anda", widget=widgets.RadioSelect)
    age = models.StringField(choices=["di bawah 18", "18-21", "22-25", "26-29", "30-35", "35 ke atas"], label="Usia Anda", widget=widgets.RadioSelect)
    reason1 = models.StringField(label='Jika Anda dalam penelitian memilih "MENERIMA HADIAH" dari Wajib Pajak, apa alasan Anda memilih opsi tersebut?')
    reason2 = models.StringField(label='Jika Anda dalam penelitian memilih "TIDAK MENERIMA HADIAH" dari Wajib Pajak, apa alasan Anda memilih opsi tersebut?')
    reason3 = models.StringField(label='Jika Anda dalam penelitian mengetahui ada tindakan penerimaan hadiah,lalu Anda memilih "MELAPORKAN" tindakan itu ke Negara, apa alasan Anda memilih opsi tersebut?')
    reason4 = models.StringField(label='Jika Anda dalam penelitian mengetahui ada tindakan penerimaan hadiah lalu Anda memilih "TIDAK MELAPORKAN" tindakan itu ke Negara, apa alasan Anda memilih opsi tersebut?')
    
    # Payment
    payment_method = models.StringField(choices=["DANA", "Go-Pay", "OVO"], label="Dengan metode apa Anda bersedia menerima pembayaran?")
    account_no = models.IntegerField(label="Silakan isi nomor rekening untuk pembayaran")
    account_name = models.StringField(label="Silakan isi nama pemilik nomor rekening pembayaran")
    account_contact = models.IntegerField(label="Silakan isi nomor kontak untuk konfirmasi pengiriman bukti pembayaran")


class Closing(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'reason1', 'reason2', 'reason3', 'reason4']


class Payment(Page):
    form_model = 'player'
    form_fields = ['payment_method', 'account_no', 'account_name', 'account_contact']


class Thanks(Page):
    pass

page_sequence = [Closing, Payment, Thanks]