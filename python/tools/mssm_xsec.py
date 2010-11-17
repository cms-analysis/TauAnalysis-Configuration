#!/usr/bin/env python
import os
#import sys
#arguments = sys.argv[:]
#sys.argv = []
import ROOT
import pprint
ROOT.gROOT.SetBatch(True)

# Version copied from /afs/cern.ch/user/t/tvickey/public/out.mhmax.root on Nov16
_FILE_NAME = '/afs/cern.ch/user/f/friis/public/out.mhmax.Nov16.root'
#_FILE_NAME = '/afs/cern.ch/user/t/tvickey/public/out.mhmax.root'

picobarns = 1.0
femtobarns = 1e-3*picobarns

def lookup_value_impl(ma, tanb, histo):
    bin = histo.FindBin(ma, tanb)
    return histo.GetBinContent(bin)

_FILE = []
def _get_file():
    " Load file "
    if not _FILE:
        _FILE.append(ROOT.TFile(_FILE_NAME))
    return _FILE[0]

def lookup_value(ma, tanb, histo):
    return lookup_value_impl(ma, tanb, _get_file().Get(histo))

def query(mA, tan_beta):
    higgs_types = [ 'h', 'A', 'H' ]
    # Curry lookup
    lookup = lambda histo : lookup_value(mA, tan_beta, histo)
    # Build emtpy dictionaries for each
    output = {
        'mA' : mA,
        'tan_beta' : tan_beta,
        'higgses' : {
            'h' : {},
            'A' : {},
            'H' : {}
        }
    }
    def add_br(input):
        " Lookup the branching ratio for a given higgs type "
        # Unpack
        type, type_info = input
        type_info['BR'] = lookup("h_brtautau_%s" % type)

    def add_mass(input):
        " Lookup the mass for a given higgs type "
        type, type_info = input
        if type == 'A':
            type_info['mass'] = mA
            return
        type_info['mass'] = lookup("h_m%s" % type)

    def add_xsec(input):
        type, type_info = input
        type_info.setdefault('xsec', {})
        for prod_type, unit in [('ggF', picobarns), ('bbH', femtobarns)]:
            type_info['xsec'][prod_type] = unit*lookup(
                "h_%s_xsec_%s" % (prod_type, type))

    map(add_br, output['higgses'].iteritems())
    map(add_mass, output['higgses'].iteritems())
    map(add_xsec, output['higgses'].iteritems())
    return output

if __name__ == "__main__":
    # Parse arguments
    #mA = sys.argv[1]
    #tanB = sys.argv[2]
    result = query(130, 30)
    pprint.pprint(result)



