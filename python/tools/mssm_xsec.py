#!/usr/bin/env python
import re
import ROOT
import pprint
ROOT.gROOT.SetBatch(True)

# Version copied from /afs/cern.ch/user/t/tvickey/public/out.mhmax.root on Nov16
_FILE_NAME = '/afs/cern.ch/user/f/friis/public/out.mhmax.Nov16.root'

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

def santander_matching(mass, xsec_4f, xsec_5f):
    t = ROOT.TMath.Log(mass/4.75) - 2.0
    return (1.0/(1.0 + t))*(xsec_4f + t*xsec_5f)

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
        for prod_type, unit in [('ggF', picobarns), ('bbH', femtobarns),
                                ('bbH4f', femtobarns)]:
            type_info['xsec'][prod_type] = unit*lookup(
                "h_%s_xsec_%s" % (prod_type, type))

    def add_santander(input):
        # Type gives Higgs type
        type, type_info = input
        mass_of_this_type = type_info['mass']
        xsec_4f = type_info['xsec']['bbH4f']
        xsec_5f = type_info['xsec']['bbH']
        type_info['xsec']['santander'] = santander_matching(
            mass_of_this_type, xsec_4f, xsec_5f)

    map(add_br, output['higgses'].iteritems())
    map(add_mass, output['higgses'].iteritems())
    map(add_xsec, output['higgses'].iteritems())
    map(add_santander, output['higgses'].iteritems())
    return output

# Functions that determine whether or not a Higgs (h, H, A) is non-negligble
_inclusion_ranges = {
    'A' : lambda massA: True,
    'H' : lambda massA: massA > 120,
    'h' : lambda massA: massA < 140,
}
def get_cross_section(sample_name, tan_beta, verbose=False):
    " Get a cross section for a given sample and tan_beta "
    matcher = re.compile(r"(?P<isBB>bb)*A(?P<massA>\d*)")
    " Get the cross section given the sample name"
    match = matcher.match(sample_name)
    if not match:
        return None
    mass = int(match.group('massA'))
    if verbose:
        print "Updating cross section for sample %s - mA: %i" % (
            sample_name, mass)
    mssm_info = query(mass, tan_beta)
    production_mechanism = (match.group('isBB') and 'bbH' or 'ggF')
    # Compute the total cross section, using multiple higgs if necessary
    total_eff_xsec = 0.0
    for higgs_type in ['H', 'A', 'h']:
        # Determine if we care about this higgs for this mA
        if _inclusion_ranges[higgs_type](mass):
            higgs_dict = mssm_info['higgses'][higgs_type]
            br = higgs_dict['BR']
            # Get the cross section in picobarns
            xsec = (higgs_dict['xsec'][production_mechanism]/picobarns)
            if verbose:
                print "--- %s contributes (BR*xsec) %0.2f * %0.2fpb = %0.2f" % (
                    higgs_type, br, xsec, br*xsec)
            total_eff_xsec += xsec*br
    if verbose:
        print "--- Total effective xsec: %0.2f pb" % total_eff_xsec
    return total_eff_xsec

if __name__ == "__main__":
    # Parse arguments
    #mA = sys.argv[1]
    #tanB = sys.argv[2]
    result = query(130, 30)
    pprint.pprint(result)



