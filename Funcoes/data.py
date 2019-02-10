# -*- coding: utf-8 -*-
from datetime import date
import calendar


class DataAtual(object):

    def __init__(self, diames="", diasemana="", ultimodia="", primeiroDia="", dataAtual=""):
        self.dataAtual = dataAtual
        self.diames = diames
        self.diasemana = diasemana
        self.ultimodia = ultimodia
        self.primeiroDia = primeiroDia

    def diaAtual(self):
        self.diames = date.today()

        self.diames = self.diames.strftime('%d/%m')
        self.diasemana = ["SEGUNDA", "TERÇA", "QUARTA",
                          "QUINTA", "SEXTA", "SABÁDO", "DOMINGO"]
        self.diasemana = self.diasemana[date.today().weekday()]

    def ultimoDiaMes(self):
        self.diames = date.today()
        self.ultimodia = calendar.monthrange(
            self.diames.year, self.diames.month)[1]

        self.ultimodia = self.diames.replace(day=calendar.monthrange(
            self.diames.year, self.diames.month)[1])

        return self.ultimodia

    def primeiroDiaMes(self):
        self.diames = date.today()
        self.primeiroDia = self.diames.replace(day=1)
        return self.primeiroDia
