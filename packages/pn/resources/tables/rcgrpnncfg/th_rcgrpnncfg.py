#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('rcgrp__id', hasDownArrow=True,
                    columns='$cod,$desc',
                    condition='$sog__cod = :SOG',
                    condition_SOG='=.sog__cod',
                    )

        r.fieldcell('rcgrpcfg__id')
        r.fieldcell('__ins_sog__cod')

    def th_order(self):
        return 'rcgrp__id'

    def th_query(self):
        return dict(column='rcgrp__id', op='contains', val='',
                    runOnStart=True,
                    )



class ViewFromGRPCFG(View):
    pass



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=1, border_spacing='4px')

        fb.field('__ins_sog__cod', readOnly=True)

        fb.field('rcgrp__id', hasDownArrow=True,
                 columns='$cod,$desc,$sog__cod',
                 auxColumns='$cod,$desc',
                 condition='$sog__cod=:sog',
                 condition_sog='=.__ins_sog__cod',
                 #condition_sog='XS', # for testing purposes...
                 )

        fb.field('rcgrpcfg__id')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
