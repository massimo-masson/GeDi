#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('rc__id')
        r.fieldcell('riga_numero')
        r.fieldcell('desc')
        r.fieldcell('dare_udc')
        r.fieldcell('avere_udc')

    def th_order(self):
        return 'rc__id'

    def th_query(self):
        return dict(column='rc__id', op='contains', val='')


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('rc__id')
        fb.field('riga_numero')
        fb.field('desc')
        fb.field('dare_udc')
        fb.field('avere_udc')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
