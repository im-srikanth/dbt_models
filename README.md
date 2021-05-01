# dbt
Intro to What is dbt?
dbt (data build tool) enables analytics engineers to transform data in their warehouses by simply writing select statements. dbt handles turning these select statements into tables and views. DBT does the T in ELT (Extract, Load, Transform) processes – it doesn’t extract or load data, but it’s extremely good at transforming data that’s already loaded into your warehouse.
More details browse here https://docs.getdbt.com/docs

Now coming to the above python code,,,,
Run this python script from command line and give the path address of your dbt models as argument , and the python script gives the details of model(table) dependencies i.e its source and reference tables. All this details are captured in excel file and that excel file will be in the model directory itself...

cmd inuput argument: ../dbt_enviroment/models             
output file: ../dbt_environment/models/dbt_models_dependency_list.xlsx

This code will be usefull for those who run all the models at once in a production deployment and also want track the source and reference tables of the model
