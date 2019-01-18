import chart

#example demo
#chart.demo_ex().show()

#An example to test the chart builder
x_data = ['journal','book','proceedings','dataset','other']
data_sample = {
     'Open in COCI': {'x': x_data, 'y': [10,20,30,40,50] },
     'Close in Crossref': {'x': x_data, 'y': [15,25,35,45,55] }
}
chart.plotBars(data_sample).show()




#https://api.crossref.org/v1/types
#all the possible types
all_types = [
      "book-section": {
        "label": "Book Section",
        "macro_type": "book"
      },
      "monograph": {
        "label": "Monograph"
      },
      "report": {
        "label": "Report"
      },
      "peer-review":{
        "label": "Peer Review"
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
        "label": "Reference Entry"
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
        "label": "Report Series"
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
        "label": "Posted Content"
      },
      "journal-issue": {
        "label": "Journal Issue",
        "macro_type": "journal"
      },
      "dissertation": {
        "label": "Dissertation"
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
]

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

#Load the COCI data
