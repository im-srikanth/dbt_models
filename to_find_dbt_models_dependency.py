from sys import argv
from pathlib import Path
from xlsxwriter import Workbook
from re import search , findall
var1 = sys.argv[1]      #give the path address of your dbt models directory   ../dbt_enviroment/models
var2 = var1.replace('\\' , '/')
temp = var2.replace('/' , '\\')
txt_folder = Path(var2).rglob('*.sql')
files = [x for x in txt_folder]
count = len(files)
dfs = []
file = Workbook(var2 + '/dbt_models_dependency_list.xlsx')
worksheet = file.add_worksheet()
worksheet.write(0 , 0 ,"DIRECTORY_NAME")
worksheet.write(0 , 1 ,"MODEL_NAME")
worksheet.write(0 , 2 ,"REFERENCE_TABLE(S)_OF_THE_MODEL")
worksheet.write(0 , 3 ,"SOURCE_TABLE(S)_OF_THE_MODEL")
excel_count = 1
for f in range(0 , count):
    ref_arr = []
    src_arr = []
    dir_name_arr = []
    model_name_arr = []
    read_file = open(files[f] , 'r')
    for line in read_file:
        if "--" not in line:
            if(search('ref\(([^)]+)' , line.lower().replace(" ",""))):
                final_line = line.lower().replace(" ","")
                arr = findall('ref\(([^)]+)', final_line)
                length = len(arr)
                for i in range(0 , length):
                    ref_arr.append(arr[i].lower().replace("'",""))
            
            if(search('source\(([^)]+)' , line.lower().replace(" " , ""))):
                final_line = line.lower().replace(" ","")
                arr = findall('source\(([^)]+)', final_line)
                new_arr = str(arr)
                arr = new_arr.replace("[","").replace("]","").replace(" ","").replace("'","").replace('"' , "").split(",")
                length = len(arr)
                for i in range(1, length , 2):
                    src_arr.append(arr[i].lower())
                    
    ref_arr = list(set(ref_arr))    
    src_arr = list(set(src_arr))
    ref_arr.sort()
    src_arr.sort()
    full_path_name = str(files[f]).replace((temp + '\\') , "")
    arr = full_path_name.split('\\')
    count = len(arr)
    if count == 3:
        dir_name = arr[0]
        model_name = arr[1] + "/" + arr[2]
    elif count == 2:
        dir_name = arr[0]
        model_name = arr[1]
    else:
        dir_name = arr[count-2]
        model_name = arr[count-1]
    max_length = max(len(ref_arr) , len(src_arr) , len(dir_name_arr) , len(model_name_arr))
    ref_arr += [' ']*(max_length - len(ref_arr))
    src_arr += [' ']*(max_length - len(src_arr))
    dir_name_arr += [dir_name]*(max_length - len(dir_name_arr))
    model_name_arr += [model_name]*(max_length - len(model_name_arr))
    for i in range(0 , max_length):
        worksheet.write(excel_count , 0 ,dir_name_arr[i])
        worksheet.write(excel_count , 1 ,model_name_arr[i])
        worksheet.write(excel_count , 2 ,ref_arr[i])
        worksheet.write(excel_count , 3 ,src_arr[i])
        excel_count = excel_count + 1
file.close()
