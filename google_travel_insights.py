cities=['Berlin','Baden-Württemberg','Bavaria','Brandenburg','Bremen','Hamburg','Hessen','Lower Saxony',
        'Mecklenburg-Vorpommern','North Rhine-Westphalia','Rhineland-Palatinate','Saarland','Saxony',
       'Saxony-Anhalt','Schleswig-Holstein','Thuringia']
base_text="""https://destinationinsights.withgoogle.com/data/daily?origin_country=DE&destination_country=DE&travel_type=ACCOMMODATION&trip_type=DOMESTIC&"""
start_date="""date_start=2020-01-01&"""
end_date="""date_end=2022-01-25&"""

import os 
import time
for i in cities:
    print(i)
    dest_city="""&origin_admin_area="""+str(i)
    query=base_text+start_date+end_date+dest_city
    response = requests.get(query).text
    data=json.loads(response)
    df = pd.json_normalize(data['daily_travel_demand'])
    df['origin_country']=data['origin_country']
    df['destination_country']=data['destination_country']
    df['origin_admin_area']=data['origin_admin_area']
    df['destination_admin_area']="ALL"
    df['travel_type']=data['travel_type']
    df['trip_type']=data['trip_type']
    filename=r"results.csv"
    with open(filename, 'a') as f:
           df.to_csv(f, mode='a', header=f.tell()==0)
    time.sleep(10)
    print(query)