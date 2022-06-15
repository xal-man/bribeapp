
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'instruction'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # GeneralInstruction
    num_player = models.IntegerField(label="1. Berapakah jumlah pemain dalam tiap kelompok eksperimen?", choices=[2, 4, 3], widget=widgets.RadioSelect)
    num_round = models.IntegerField(label="2. Berapakah jumlah keputusan yang dilakukan oleh Staf dalam tiap ronde?", choices=[1, 2, 3], widget=widgets.RadioSelect)
    authorized = models.StringField(label="3. Siapakah yang berwenang menentukan keputusan penerimaan hadiah?", choices=['Staf', 'Kepala Tim'], widget=widgets.RadioSelect)
    whistleblower = models.StringField(label="Siapakah yang mempunyai hak pelaporan (whistleblowing)?", choices=['Staf', 'Kepala Tim'], widget=widgets.RadioSelect)

    # RewardInfo
    first_qstn = models.IntegerField(label="1. Jika Staf menerima hadiah, Kepala Tim tidak menerima, dan Staf tidak melaporkan tindakan ini, berapakah imbalan yang didapat oleh Kepala Tim? (Tuliskan angka saja)")
    second_qstn = models.IntegerField(label="2. Jika Staf tidak menerima hadiah, Kepala Tim menerima, dan Staf melaporkan tindakan ini, berapakah imbalan yang didapat oleh Kepala Tim? (Tuliskan angka saja)")
    third_qstn = models.IntegerField(label="3. Jika Staf tidak menerima hadiah, Kepala Tim menerima, dan Staf tidak melaporkan tindakan ini, berapakah imbalan yang didapat oleh Staf?  (Tuliskan angka saja)")
    fourth_qstn = models.StringField(label="4. Dengan metode apakah pemain dapat menerima imbalan?", choices=['Akumulasi 12 ronde', 'Diambil SATU secara acak dari 12 ronde'], widget=widgets.RadioSelect)

    # RewardInfo
    si_first_qstn = models.IntegerField(label="1. Jika Staf menerima hadiah, Kepala Tim tidak menerima, dan Staf tidak melaporkan tindakan ini, berapakah imbalan yang didapat oleh Kepala Tim? (Tuliskan angka saja)")
    si_second_qstn = models.IntegerField(label="2. Jika Staf tidak menerima hadiah, Kepala Tim menerima, dan Staf melaporkan tindakan ini, berapakah imbalan yang didapat oleh Kepala Tim? (Tuliskan angka saja)")
    si_third_qstn = models.IntegerField(label="3. Jika Staf tidak menerima hadiah, Kepala Tim menerima, dan Staf tidak melaporkan tindakan ini, berapakah imbalan yang didapat oleh Staf?  (Tuliskan angka saja)")
    si_fourth_qstn = models.StringField(label="4. Dengan metode apakah pemain dapat menerima imbalan?", choices=['Akumulasi 12 ronde', 'Diambil SATU secara acak dari 12 ronde'], widget=widgets.RadioSelect)

    # Consent
    consent = models.BooleanField(choices=[[True, 'SIAP'], [False, 'ULANGI']], initial=True, label='Jika sudah siap, silakan pilih opsi "SIAP". Jika belum, silakan pilih opsi "ULANGI" dan Anda akan menuju sesi 3 (Instruksi Umum).')


class GeneralInstruction(Page):
    form_model = 'player'
    form_fields = ['num_player', 'num_round', 'authorized', 'whistleblower']


class RewardInfo(Page):
    form_model = 'player'
    form_fields = ['first_qstn','second_qstn','third_qstn', 'fourth_qstn']


class SpecialInstruction(Page):
    form_model = 'player'
    form_fields = ['si_first_qstn','si_second_qstn','si_third_qstn', 'si_fourth_qstn']


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.consent=False
    @staticmethod
    def error_message(player: Player, values):
        solution = dict(
          consent=True
                  )
        error_messages = dict()
        for field_name in solution:
                if values [field_name] != solution[field_name]:
                    error_messages[field_name] = 'You cannot proceed to the next page without giving your consent. Please exit this webpage if you do not want to participate.'
        return error_messages


page_sequence = [GeneralInstruction, RewardInfo, Consent]