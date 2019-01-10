import chart

#example demo
#chart.demo_ex().show()

#data sample
x_data = ['journal','book','proceedings','dataset','others']
data_sample = {
     'Open in COCI': {'x': x_data, 'y': [10,20,30,40,50] },
     'Close in Crossref': {'x': x_data, 'y': [15,25,35,45,55] }
}
chart.plotBars(data_sample).show()
