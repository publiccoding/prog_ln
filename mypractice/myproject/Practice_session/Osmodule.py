import os 

#.pyc_dis_failed
print("{}".format('Thimma'))
path ='C:\\Users\\kristhim\\Desktop\\hana project'
cpath ='C:\\Users\\kristhim\\Desktop\\hana project\\2018.02\\csur1.4-1.sles11'
hpath='C:\\Users\\kristhim\\Desktop\\hana project\\healthcheck\\health1.0-0.sles11'

for root, dirs, files in os.walk(path):
    for file in files:
        # if str(file).endswith(".pyc_dis"):
        #     os.rename(root+"\\"+file, "{}.py".format(str(root+"\\"+file).split(".pyc_dis")[0]))
        if str(file).endswith(".pyc_dis_failed") or str(file).endswith(".pyc"):
            os.remove(root+"\\"+file)
