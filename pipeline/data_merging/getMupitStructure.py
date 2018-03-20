import requests
import json
import sys
import argparse
import csv
import time


def parse_args():
    parser = argparse.ArgumentParser(description='Determine correct BRCA structure from MuPIT.')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                        help='Input variants.')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        help='Output variants.')
    options = parser.parse_args()
    return options


def isMissenseSubstitution(ref, alt):
    bases = ['a', 'c', 't', 'g']
    ref = ref.lower()
    alt = alt.lower()
    if ref in bases and alt in bases and len(ref) == 1 and len(alt) == 1:
        return True
    return False


def main(args):
    options = parse_args()
    inputFile = options.input
    outputFile = options.output

    input_file = csv.reader(inputFile, delimiter='\t')
    output_file = csv.writer(outputFile, delimiter='\t')
    input_header_row = input_file.next()

    # The following new columns will contain data generated by this file
    new_columns_to_append = ["mupit_structure"]

    output_header_row = input_header_row + new_columns_to_append

    output_file.writerow(output_header_row)

    chromIndex = input_header_row.index("Chr")
    posIndex = input_header_row.index("Pos")
    refIndex = input_header_row.index("Ref")
    altIndex = input_header_row.index("Alt")

    for variant in input_file:
        chrom = "chr" + variant[chromIndex]
        pos = int(variant[posIndex])
        ref = variant[refIndex]
        alt = variant[altIndex]

        # only concerned with missense substitutions
        if isMissenseSubstitution(ref, alt):
            # Add empty data for each new column to prepare for data insertion by index
            for i in range(len(new_columns_to_append)):
                variant.append('-')

            retries = 5
            if (pos >= 32356427 and pos <= 32396972) or (pos >= 43045692 and pos <= 43125184):
                mupit_structure = get_brca_struct(chrom, pos)
                if mupit_structure == "retry":
                    if retries > 0:
                        print "retrying chrom: %s, pos: %s" % (chrom, pos)
                        retries -= 1
                        time.sleep(10)
                        mupit_structure = get_brca_struct(chrom, pos)
                    else:
                        print "Request for position %s failed 5 times, exiting." % (pos)
                        sys.exit(1)

                variant[output_header_row.index("mupit_structure")] = mupit_structure

                if mupit_structure is not '-':
                    print variant

                output_file.writerow(variant)

                time.sleep(0.1)


def get_brca_struct(chrom, pos):
    main_url = 'http://staging.cravat.us/MuPIT_Interactive'
    brca_structures = ['1t15','1jm7','4igk','fENSP00000380152_7']
    query_url = main_url+'/rest/showstructure/query'
    params = {
             'search_textarea':'%s %s'%(chrom, pos),
             'search_gene':'',
             'search_structure':'',
             'search_protein':'',
             'search_upload_file':'',
             }
    try:
        r = requests.post(query_url, data=params)
    except requests.exceptions.RequestException as e:
        print e
        return "retry"
    d = json.loads(r.text)
    structures = d['structures']
    main_struct = None;
    min_pref_level = sys.maxsize # max size integer
    max_no_query_pos = -1
    max_no_res = -1
    pref_level_hit = False
    for structure_id in structures:
        structure = structures[structure_id]
        no_query_pos = len(structure['gmtoseqres'])
        no_res = structure['nores']
        pref_level = structure['prefLevel']
        if (pref_level >= 1) and (pref_level < min_pref_level):
            pref_level_hit = True
            min_pref_level = pref_level
            max_no_query_pos = no_query_pos
            max_no_res = no_res
            main_struct = structure_id
        elif (pref_level == min_pref_level) or (pref_level == 0 and not(pref_level_hit)):
            if no_query_pos > max_no_query_pos:
                max_no_query_pos = no_query_pos
                max_no_res = no_res
                main_struct = structure_id
            elif no_query_pos == max_no_query_pos:
                if no_res > max_no_res:
                    max_no_res = no_res
                    main_struct = structure_id
    if main_struct in brca_structures:
        return main_struct
    else:
        return '-'


if __name__ == "__main__":
    sys.exit(main(sys.argv))
