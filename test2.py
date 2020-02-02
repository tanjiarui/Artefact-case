import pandas as pd

# change the separation ',' as '\t' in product.csv and drop duplicate id, facilitating the later hive import
# product=pd.read_csv('/home/ubuntu/Artefact_written_test/test2_data/product.csv',sep='\t',header=None).astype(str)
# product.drop_duplicates(0,inplace=True)
# product.to_csv('/home/ubuntu/Artefact_written_test/test2_data/tmp',sep='\t',header=False,index=False)

order=pd.read_csv('/home/ubuntu/Artefact_written_test/test2_data/order.csv',sep=',',header=None)
order.insert(4,value=None,column=4,allow_duplicates=True)
for index in order.index:
	date=order.loc[index,3]
	year=date.split('-')[2]
	order.loc[index,4]=int(year)
	print('handling line '+str(index))
order.to_csv('/home/ubuntu/Artefact_written_test/test2_data/tmp',sep=',',header=False,index=False)