testcase1=["address.city", "IN", "Kolkata,Mumbai"]
testcase2=["username", "EQUALS", "Mumbai"]

def parse_json(inputList, size):
    url="https://raw.githubusercontent.com/arcjsonapi/ApiSampleData/master/api/users"
    import requests
    out=requests.get(url)
    data=out.json()
    all_field=inputList[0].split('.')
    all_val=inputList[-1].split(',')
    match=[]
    temp_out=''
    for person in data:
        for val in all_val:
            for field in all_field:
                if isinstance(temp_out, dict):
                    temp_out=person[field]
                else:
                    if temp_out[field] == val:
                        match.append(person['id'])
    # print(data)
    return match

parse_json(testcase1,3)
parse_json(testcase2,3)