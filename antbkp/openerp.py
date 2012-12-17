#This file is part of Ant Backup. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.


class Openerp():

    @staticmethod
    def run(vals, options):
        print "Aqui fem _copia de bd OpenERP"
        for server in vals.get('servers').split(','):
            
            s = server.split(':')
            server = s[0]
            bd = s[1]
            print server
            print bd
        print "===="
