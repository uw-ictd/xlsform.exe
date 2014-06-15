"""
Drag and drop a file onto this exe in order to convert it.
The xform will appear in an output folder in the same directory as this exe.
"""
import os, sys
import pyxform
from pyxform.utils import sheet_to_csv

def has_external_choices(json_struct):
    """
    Returns true if a select one external prompt is used in the survey.
    """
    if isinstance(json_struct, dict):
        for k,v in json_struct.items():
            if k == u"type" and v.startswith(u"select one external"):
                return True
            elif has_external_choices(v):
                return True
    elif isinstance(json_struct, list):
        for v in json_struct:
            if has_external_choices(v):
                return True
    return False

if __name__ == '__main__':
    try:
        argv = sys.argv
        if len(argv) < 2:
            print __doc__
            print 'Usage:'
            print argv[0] + ' path_to_XLSForm'
        else:
            warnings = []
            name, ext = os.path.splitext(os.path.basename(argv[1]))
            output_dir = os.path.join(os.path.split(argv[0])[0], 'output')
            out_file = os.path.join(output_dir, name + '.xml')
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            json_survey = pyxform.xls2json.parse_file_to_json(argv[1], warnings=warnings)
            survey = pyxform.builder.create_survey_element_from_dict(json_survey)
            survey.print_xform_to_file(out_file, validate=False)
            if has_external_choices(json_survey):
                itemsets_csv = os.path.join(output_dir, "itemsets.csv")
                choices_exported = sheet_to_csv(argv[1], itemsets_csv, "external_choices")
                if not choices_exported:
                    print "Could not export itemsets.csv, perhaps the external choices sheet is missing."
                else:
                    print 'external choices csv is located at:', itemsets_csv
            if len(warnings) > 0:
                print "Warnings:"
            for w in warnings:
                print w
            print 'xform is located at:', out_file
            print 'Conversion complete!'
    except Exception as e:
        print e
    raw_input("Press Enter to continue...")
