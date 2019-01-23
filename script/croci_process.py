#https://api.crossref.org/v1/types
#all the possible types
#https://api.crossref.org/v1/types
#all the possible types
all_types = {
      "book-section": {
        "label": "Book Section",
        "macro_type": "book"
      },
      "monograph": {
        "label": "Monograph",
        "macro_type": "book"
      },
      "report": {
        "label": "Report",
        "macro_type": "other"
      },
      "peer-review":{
        "label": "Peer Review",
        "macro_type": "other"
      },
      "book-track":{
        "label": "Book Track",
        "macro_type": "book"
      },
      "journal-article":{
        "label": "Journal Article",
        "macro_type": "journal"
      },
      "book-part":{
        "label": "Part",
        "macro_type": "book"
      },
      "other":{
        "label": "Other",
        "macro_type": "other"
      },
      "book":{
        "label": "Book",
        "macro_type": "book"
      },
      "journal-volume":{
        "label": "Journal Volume",
        "macro_type": "journal"
      },
      "book-set":{
        "label": "Book Set",
        "macro_type": "book"
      },
      "reference-entry": {
        "label": "Reference Entry",
        "macro_type": "other"
      },
      "proceedings-article": {
        "label": "Proceedings Article",
        "macro_type": "proceedings"
      },
      "journal": {
        "label": "Journal",
        "macro_type": "journal"
      },
      "component":{
        "label": "Component",
        "macro_type": "other"
      },
      "book-chapter": {
        "label": "Book Chapter",
        "macro_type": "book"
      },
      "proceedings-series": {
        "label": "Proceedings Series",
        "macro_type": "proceedings"
      },
      "report-series": {
        "label": "Report Series",
        "macro_type": "other"
      },
      "proceedings": {
        "label": "Proceedings",
        "macro_type": "proceedings"
      },
      "standard":{
        "label": "Standard",
        "macro_type": "other"
      },
      "reference-book": {
        "label": "Reference Book",
        "macro_type": "book"
      },
      "posted-content": {
        "label": "Posted Content",
        "macro_type": "other"
      },
      "journal-issue": {
        "label": "Journal Issue",
        "macro_type": "journal"
      },
      "dissertation": {
        "label": "Dissertation",
        "macro_type": "book"
      },
      "dataset": {
        "label": "Dataset",
        "macro_type": "dataset"
      },
      "book-series": {
        "label": "Book Series",
        "macro_type": "book"
      },
      "edited-book": {
        "label": "Edited Book",
        "macro_type": "book"
      },
      "standard-series": {
        "label": "Standard Series",
        "macro_type": "other"
      }
}


macro_type = {
        'journal': {
            'label': 'Journal',
            'value':{'coci_open': 0,'crossref_close':0}
        },

        'book': {
            'label': 'Book',
            'value':{'coci_open': 0,'crossref_close':0}
        },

        'proceedings': {
            'label': 'Proceedings',
            'value':{'coci_open': 0,'crossref_close':0}
        },

        'dataset': {
            'label': 'Dataset',
            'value':{'coci_open': 0,'crossref_close':0}
        },

        'other': {
            'label': 'Other',
            'value':{'coci_open': 0,'crossref_close':0}
        }
}


#PROCESSING THE DATA

import csv

#Load the COCI data
COCI_CSV_PATH = "../data/non_open_sample.csv"
COCI_CSV_PATH = "/Users/ivan.heibi/project.loc/croci/data/non_open.csv"
STREAM_BUFFER = 1000

other_list = {}

with open(COCI_CSV_PATH,'r') as cocicsv:
    cocicsv_reader = csv.DictReader(cocicsv)
    for row in cocicsv_reader:
        #"doi","type","cited_by","non_open"

        if row['type'] not in all_types:
            all_types[row['type']] = {'label': row['type'],"macro_type": "other"}

        r_m_type = all_types[row['type']]['macro_type']

        #check the others
        if r_m_type == 'other':
            if row['type'] not in other_list:
                other_list[row['type']] = {'value':{'coci_open':0,'crossref_close':0}}
            other_list[row['type']]['value']['coci_open'] += int(row['cited_by'])
            other_list[row['type']]['value']['crossref_close'] += int(row['non_open'])

        #in case is not int
        try:
            macro_type[r_m_type]['value']['coci_open'] += int(row['cited_by'])
        except Exception as e:
            macro_type[r_m_type]['value']['coci_open'] += 0

        #in case is not int
        try:
            macro_type[r_m_type]['value']['crossref_close'] += int(row['non_open'])
        except Exception as e:
            macro_type[r_m_type]['value']['crossref_close'] += 0


#Write the results on a new .csv file
#Load the COCI data
CROCI_RES = "../data/croci_res.csv"

str_csv = "type,coci_open,crossref_close\n"
for r_m_type in macro_type:
    str_csv = str_csv + r_m_type + "," + str(macro_type[r_m_type]['value']['coci_open']) + "," + str(macro_type[r_m_type]['value']['crossref_close']) +"\n"

file_res = open(CROCI_RES,'w')
file_res.write(str_csv)
file_res.close()
