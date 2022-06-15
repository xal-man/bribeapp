from otree.api import *

c = cu

import csv
import os

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 12
    STAF_ROLE = 'Staf'
    KATIM_ROLE = 'Katim'

    GAJI = [c(7500), c(10000)]

    WP_EARNING = []
    TAX_25 = []
    EVASION = []
    TAX_PAYED = []
    BRIBE = []

    path = os.path.join(os.getcwd(), 'game/data.csv')
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                WP_EARNING.append(cu(int(row[1])))
                TAX_25.append(cu(int(row[2])))
                EVASION.append(cu(int(row[3])))
                TAX_PAYED.append(cu(int(row[4])))
                BRIBE.append(cu(int(row[5])))
                line_count += 1
    print(f'Processed {line_count} lines.')

    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    num_messages = models.IntegerField()
    game_finished = models.BooleanField()


class Player(BasePlayer):
    # StaffPage1
    staff1_first_qstn = models.CurrencyField(label="1. Berapakah nilai pajak terutang riil dari perusahaan H? (hanya angka; tanpa tanda pemisah angka)")
    staff1_second_qstn = models.StringField(label="2. Apa yang akan Anda lakukan dengan hadiah tersebut?",
                                            choices=["Menolak hadiah tersebut dan menetapkan pajak sesuai nilai sebenarnya",
                                                    f"Menerima hadiah sebesar 0% untuk Staf dan 100% untuk Kepala Tim",
                                                    f"Menerima hadiah sebesar 25% untuk Staf dan 75% untuk Kepala Tim",
                                                    f"Menerima hadiah sebesar 50% untuk Staf dan 50% untuk Kepala Tim",
                                                    f"Menerima hadiah sebesar 75% untuk Staf dan 25% untuk Kepala Tim",
                                                    f"Menerima hadiah sebesar 100% untuk Staf dan 0% untuk Kepala Tim"],
                                                    widget=widgets.RadioSelect)

    # KepalaTimPage
    katim_first_qstn = models.CurrencyField(label="1. Berapakah nilai pajak terutang riil dari perusahaan H? (hanya angka; tanpa tanda pemisah angka)")
    katim_second_qstn = models.StringField(label="2. Apa yang akan Anda lakukan dengan hadiah tersebut?",
                                            choices=["Menolak hadiah tersebut dan menetapkan pajak sesuai nilai sebenarnya",
                                                    f"Menerima hadiah sebesar 0% untuk Staf dan 100% untuk Kepala Tim",
                                                    f"Menerima hadiah sebesar 25% untuk Staf dan 75% untuk Kepala Tim",
                                                    f"Menerima hadiah sebesar 50% untuk Staf dan 50% untuk Kepala Tim",
                                                    f"Menerima hadiah sebesar 75% untuk Staf dan 25% untuk Kepala Tim",
                                                    f"Menerima hadiah sebesar 100% untuk Staf dan 0% untuk Kepala Tim"],
                                                    widget=widgets.RadioSelect)

    # StaffPage2
    staff2_qstn = models.StringField(choices=["Melaporkan kepada Negara", "Tidak melaporkan kepada Negara"], widget=widgets.RadioSelect
                                     ,label="Apa yang akan Anda lakukan setelah mengetahui informasi tersebut?")

    # GameSummary
    game_summary = models.StringField(choices=["LANJUT", "SELESAI"], widget=widgets.RadioSelect)


class WaitPageGrouping(WaitPage):
    group_by_arrival_time = True
    title_text = 'Please wait...'
    body_text = 'You will be associated with real people in this study. You are now waiting for the other participants to reach this stage. '


class Page1(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        if player.role == C.STAF_ROLE:
            return ['staff1_first_qstn', 'staff1_second_qstn']
        else:
            return []

    @staticmethod
    def error_message(player: Player, values):
        if player.role == C.STAF_ROLE:
            group = player.group
            iter = group.round_number - 1
            if cu(values['staff1_first_qstn']) != C.TAX_25[iter]:
                return 'Masukan nilai tax yang tepat'

    @staticmethod
    def live_method(player, data):
        print(data)
        if data != None:
            if cu(data) == C.TAX_25[0]:
                group = player.group
                group.game_finished = True
                response = dict(type='game_finished')
                return {0: response}
            else:
                response = dict(type='wrong')
                return {0: response}
        else:
            response = dict(type='wait')
            return {0: response}

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        iter = group.round_number - 1
        earning = C.WP_EARNING[iter]
        evasion = C.EVASION[iter]
        tax_25 = C.TAX_25[iter]
        tax_payed = C.TAX_PAYED[iter]
        bribe = C.BRIBE[iter]
        return dict(
            earning = earning,
            evasion = evasion,
            tax_25 = tax_25,
            tax_payed = tax_payed,
            bribe = bribe,
            gaji = C.GAJI[0]
        )


class Page2(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        if player.role == C.KATIM_ROLE:
            return ['katim_first_qstn','katim_second_qstn']
        else:
            return []

    @staticmethod
    def error_message(player: Player, values):
        if player.role == C.KATIM_ROLE:
            group = player.group
            iter = group.round_number - 1
            if cu(values['katim_first_qstn']) != C.TAX_25[iter]:
                return 'Masukan nilai tax yang tepat'

    @staticmethod
    def live_method(player, data):
        print(data)
        if data != None:
            if cu(data) == C.TAX_25[0]:
                group = player.group
                group.game_finished = True
                response = dict(type='game_finished')
                return {0: response}
            else:
                response = dict(type='wrong')
                return {0: response}
        else:
            response = dict(type='wait')
            return {0: response}

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        staff = group.get_player_by_role(C.STAF_ROLE)
        dec1 = staff.staff1_second_qstn
        iter = group.round_number - 1
        earning = C.WP_EARNING[iter]
        evasion = C.EVASION[iter]
        tax_25 = C.TAX_25[iter]
        tax_payed = C.TAX_PAYED[iter]
        bribe = C.BRIBE[iter]
        return dict(
            decision1 = dec1,
            earning = earning,
            evasion = evasion,
            tax_25 = tax_25,
            tax_payed = tax_payed,
            bribe = bribe,
            gaji = C.GAJI[1]
        )


class Page3(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        if player.role == C.STAF_ROLE:
            return ['staff2_qstn']
        else:
            return []

    def live_method(player, data):
        group = player.group
        group.game_finished = True
        response = dict(type='game_finished')
        return {0: response}

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        katim = group.get_player_by_role(C.KATIM_ROLE)
        dec2 = katim.katim_second_qstn
        return dict(decision2=dec2)


class Result(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        staff = group.get_player_by_role(C.STAF_ROLE)
        dec1 = staff.staff1_second_qstn
        dec3 = staff.staff2_qstn
        
        katim = group.get_player_by_role(C.KATIM_ROLE)
        dec2 = katim.katim_second_qstn

        return dict(decision1=dec1,
                    decision2=dec2,
                    decision3=dec3)

page_sequence = [WaitPageGrouping, Page1, Page2, Page3, Result]