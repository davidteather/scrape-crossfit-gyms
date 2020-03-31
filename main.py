import requests

with open("output.csv", "w+") as data:
    data.write("")

with open("output.csv", "a", encoding="utf-8") as output:
    output.write("website,photo,ready_to_link,ordernum,latlon,city,name_search,photo_version,zip,country_short_code,bad_standing,effective_date,status,address,active,state_code,show_on_map,kids,name,country,org_type,aid,full_state\n")
    
    morePages = True
    itx = 1
    while morePages:
        r = requests.get("https://www.crossfit.com/cf/find-a-box.php?page={}&country=&state=&city=&type=Commercial".format(str(itx))).json()

        if len(r['affiliates']) == 0:
            morePages = False
        else:

            for gym in r['affiliates']:
                try:
                    state = gym['state_code']
                    full_state = gym['full_state']
                except:
                    state = ""
                    full_state = ""

                try:
                    latlon = gym['latlon'].replace(",","\t")
                except:
                    latlon = ""

                try:
                    zipcode = gym['zip']
                except:
                    zipcode = ""

                try:
                    city = gym['city']
                except:
                    city = ""

                try:
                    address = gym['address']
                except:
                    address = ""

                print(gym)
                output.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                    gym['website'], gym['photo'], str(gym['ready_to_link']), str(gym['ordernum']), latlon, city,
                    gym['name_search'], str(gym['photo_version']), zipcode, gym['country_short_code'], str(gym['bad_standing']),
                    str(gym['effective_date']), str(gym['status']), address, str(gym['active']), state, str(gym['show_on_map']),
                    str(gym['kids']), gym['name'], gym['country'], gym['org_type'], str(gym['aid']), full_state
                ))
        itx += 1
    
print("Final Page with data: " + str(itx-2))