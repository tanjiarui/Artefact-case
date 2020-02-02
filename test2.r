library(REmap)
library(devtools)

top_sell=read.csv("/home/ubuntu/Artefact_written_test/test2_data/top_sell.csv",sep='\t', header=FALSE, stringsAsFactors=FALSE)
# change the column
names(top_sell)=c('product_id','sell','nation','year','name','rank')
# remove duplicates
top_sell=unique(top_sell)
top_sell[which(top_sell$nation=='EIRE'),'nation']='Ireland'
top_sell[which(top_sell$nation=='RSA'),'nation']='South Africa'
top_sell[which(top_sell$nation=='USA'),'nation']='United States of America'
data_10=top_sell[which(top_sell$year==10),]
data_11=top_sell[which(top_sell$year==11),]

# top10 sell in every country of year 10
data = data.frame(country = data_10$nation,value=data_10$sell)
remapC(data,maptype="world",color='skyblue')

# top10 sell in every country of year 11
data = data.frame(country = data_11$nation,value=data_11$sell)
remapC(data,maptype="world",color='skyblue')