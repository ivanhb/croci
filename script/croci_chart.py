import csv
import chart

#Write the results on a new .csv file
#Load the COCI data
CROCI_RES = "../data/croci_res.csv"
macro_type = {}

#type,label,coci_open,crossref_close
with open(CROCI_RES,'r') as cocicsv:
    cocicsv_reader = csv.DictReader(cocicsv)
    for row in cocicsv_reader:
        macro_type[row['type']] = {}
        macro_type[row['type']]['label'] = row['label']
        macro_type[row['type']]['value'] = {'coci_open': int(row['coci_open']),'crossref_close': int(row['crossref_close'])}
        #"doi","type","cited_by","non_open"




# journal, book, proceedings, dataset, other
#Plot them
#Data sample
############
x_data = ['journal','book','proceedings','dataset','other']

o_in_coci = []
for k in x_data:
    o_in_coci.append(macro_type[k]['value']['coci_open'])

c_in_crossref = []
for k in x_data:
    c_in_crossref.append(macro_type[k]['value']['crossref_close'])

data_plot = {
     'Open in COCI': {'x': x_data, 'y': o_in_coci },
     'Close in Crossref': {'x': x_data, 'y': c_in_crossref }
}

chart.plotBars(data_plot,opt = {'ylabel': 'Number of Citations', 'bar_val':True,'bar_coi':1000000,'bar_suf':'M','bar_pre':''}, sortit= False, logit= True).show()
