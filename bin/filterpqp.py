#!/usr/bin/env python3

import os
import argparse
import pandas as pd


def get_arguments(parser):
  """Set up command line parameters
  """
  parser.add_argument("-s", "--psmfile",
                      help="""The .psmpkl input file.""",
                      metavar="FILE",
                      required=True)
  parser.add_argument("-k", "--peakfile",
                      help="""The .peakpkl input file.""",
                      metavar="FILE",
                      required=True)
  parser.add_argument("-l", "--proteinfile",
                      help="""The protein list input file.""",
                      metavar="FILE",
                      required=True)
  parser.add_argument("-p", "--prob_cutoff",
                      help="""The peptide probability cutoff.""",
                      type=float,
                      metavar=("prob_cutoff"),
                      default=0.01)
  return parser.parse_args()


def main():
  """Main
  """
  parser = argparse.ArgumentParser(description="""Filter .psmpkl and .peakpkl files based on PeptideProphet and ProteinProphet FDRs.""")
  args = get_arguments(parser)

  psmfile = args.psmfile
  peakfile = args.peakfile
  proteinfile = args.proteinfile
  prob_cutoff = 1 - args.prob_cutoff

  psmfilteredfile = os.path.splitext(psmfile)[0] + "_filtered.psmpkl"
  peakfilteredfile = os.path.splitext(peakfile)[0] + "_filtered.peakpkl"

  psms = pd.read_pickle(psmfile)
  peaks = pd.read_pickle(peakfile)
  protein_list = pd.read_csv(proteinfile)

  # Filter psmpkl
  psms_filtered1 = psms[ psms['pep'] <= prob_cutoff ]
  psms_filtered2 = psms_filtered1[ psms_filtered1['protein_id'].str.contains('|'.join(protein_list['protein_id']))]
  psms_filtered2.to_pickle(psmfilteredfile, protocol=4)
  
  # Filter peakpkl
  peaks_filtered = peaks[ peaks['scan_id'].isin(psms_filtered2['scan_id'])]
  peaks_filtered.to_pickle(peakfilteredfile, protocol=4)

  
if __name__ == "__main__":
  main()
