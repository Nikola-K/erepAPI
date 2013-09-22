# Copyright (c) 2013 Nikola Kovacevic   <nikolak@outlook.com>,
#                                       <nikola.kovacevic91@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# SOFTWARE
import api

class invalidID(Exception):
     def __init__(self, id_value):
         self.id_value = id_value

     def __str__(self):
         return repr(self.id_value)

class Country_regions(object):

    """Contains regions of country as dictionary.
      Requires country ID as initial argument

    self.regions={ "region_name":{
                                    "id":integer
                                    "owner_id":integer
                                    "original_owner_id":integer
                                    "url":string
                                }

                }
    """
    def __init__(self, countryID):
        super(Country_regions, self).__init__()
        self.id = str(countryID)
        self.__resource = "country"
        self.__action = "regions"
        self.__params = "countryId=" + self.id

        if not self.id.isdigit():
            raise invalidID
        else:
            self.__url = api._construct_url(self.__resource, self.__action, self.__params)
            self.__headers = api._construct_headers(self.__url)
        self.data = api._load(self.url, self.__headers)
        self.__base_url = "http://www.erepublik.com/en/main/region/"
        self.regions = {}
        for item in self.data["regions"]["region"]:
            region = self.data["regions"]["region"][item]
            self.regions[region["name"]] = {
                "id": int(region["id"]),
                "owner_id": int(region["current_owner_country_id"]),
                "original_owner_id": int(region["original_owner_country_id"]),
                "url": self.__base_url + region["permalink"]}

