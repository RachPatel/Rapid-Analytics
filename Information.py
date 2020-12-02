

""" Packages """
import collections
import json
import pandas as pd
from collections import Counter
import re
from functools import reduce
from graphviz import Digraph

""" Information Class which holds attributes and methods to create and use the Information object"""


class Information:
    """ Class constructor with attributes of information object"""

    def __int__(self, ts, visitor, environment, event, subject):

        # each attribute can by defined its own class
        # for any further analytics
        self.ts = ts
        self.visitor = visitor
        self.environment = environment
        self.event = event
        self.subject = subject

    """ the get methods for all the attributes of Information Object"""

    def getts(self):
        return self.ts

    def getVisitor(self):
        return self.visitor

    def getEnvironment(self):
        return self.environment

    def getEvent(self):
        return self.event

    def getSubject(self):
        return self.subject

    """ Dictionary that maps countries to continents - created by Hans-Wolfgang Loidl"""

    cntry_to_cont = {'AF': 'AS', 'AX': 'EU', 'AL': 'EU', 'DZ': 'AF', 'AS': 'OC', 'AD': 'EU', 'AO': 'AF',
                     'AI': 'NA', 'AQ': 'AN', 'AG': 'NA', 'AR': 'SA', 'AM': 'AS', 'AW': 'NA', 'AU': 'OC',
                     'AT': 'EU', 'AZ': 'AS', 'BS': 'NA', 'BH': 'AS', 'BD': 'AS', 'BB': 'NA', 'BY': 'EU',
                     'BE': 'EU', 'BZ': 'NA', 'BJ': 'AF', 'BM': 'NA', 'BT': 'AS', 'BO': 'SA', 'BQ': 'NA',
                     'BA': 'EU', 'BW': 'AF', 'BV': 'AN', 'BR': 'SA', 'IO': 'AS', 'VG': 'NA', 'BN': 'AS',
                     'BG': 'EU', 'BF': 'AF', 'BI': 'AF', 'KH': 'AS', 'CM': 'AF', 'CA': 'NA', 'CV': 'AF',
                     'KY': 'NA', 'CF': 'AF', 'TD': 'AF', 'CL': 'SA', 'CN': 'AS', 'CX': 'AS', 'CC': 'AS',
                     'CO': 'SA', 'KM': 'AF', 'CD': 'AF', 'CG': 'AF', 'CK': 'OC', 'CR': 'NA', 'CI': 'AF',
                     'HR': 'EU', 'CU': 'NA', 'CW': 'NA', 'CY': 'AS', 'CZ': 'EU', 'DK': 'EU', 'DJ': 'AF',
                     'DM': 'NA', 'DO': 'NA', 'EC': 'SA', 'EG': 'AF', 'SV': 'NA', 'GQ': 'AF', 'ER': 'AF',
                     'EE': 'EU', 'ET': 'AF', 'FO': 'EU', 'FK': 'SA', 'FJ': 'OC', 'FI': 'EU', 'FR': 'EU',
                     'GF': 'SA', 'PF': 'OC', 'TF': 'AN', 'GA': 'AF', 'GM': 'AF', 'GE': 'AS', 'DE': 'EU',
                     'GH': 'AF', 'GI': 'EU', 'GR': 'EU', 'GL': 'NA', 'GD': 'NA', 'GP': 'NA', 'GU': 'OC',
                     'GT': 'NA', 'GG': 'EU', 'GN': 'AF', 'GW': 'AF', 'GY': 'SA', 'HT': 'NA', 'HM': 'AN',
                     'VA': 'EU', 'HN': 'NA', 'HK': 'AS', 'HU': 'EU', 'IS': 'EU', 'IN': 'AS', 'ID': 'AS',
                     'IR': 'AS', 'IQ': 'AS', 'IE': 'EU', 'IM': 'EU', 'IL': 'AS', 'IT': 'EU', 'JM': 'NA',
                     'JP': 'AS', 'JE': 'EU', 'JO': 'AS', 'KZ': 'AS', 'KE': 'AF', 'KI': 'OC', 'KP': 'AS',
                     'KR': 'AS', 'KW': 'AS', 'KG': 'AS', 'LA': 'AS', 'LV': 'EU', 'LB': 'AS', 'LS': 'AF',
                     'LR': 'AF', 'LY': 'AF', 'LI': 'EU', 'LT': 'EU', 'LU': 'EU', 'MO': 'AS', 'MK': 'EU',
                     'MG': 'AF', 'MW': 'AF', 'MY': 'AS', 'MV': 'AS', 'ML': 'AF', 'MT': 'EU', 'MH': 'OC',
                     'MQ': 'NA', 'MR': 'AF', 'MU': 'AF', 'YT': 'AF', 'MX': 'NA', 'FM': 'OC', 'MD': 'EU',
                     'MC': 'EU', 'MN': 'AS', 'ME': 'EU', 'MS': 'NA', 'MA': 'AF', 'MZ': 'AF', 'MM': 'AS',
                     'NA': 'AF', 'NR': 'OC', 'NP': 'AS', 'NL': 'EU', 'NC': 'OC', 'NZ': 'OC', 'NI': 'NA',
                     'NE': 'AF', 'NG': 'AF', 'NU': 'OC', 'NF': 'OC', 'MP': 'OC', 'NO': 'EU', 'OM': 'AS',
                     'PK': 'AS', 'PW': 'OC', 'PS': 'AS', 'PA': 'NA', 'PG': 'OC', 'PY': 'SA', 'PE': 'SA',
                     'PH': 'AS', 'PN': 'OC', 'PL': 'EU', 'PT': 'EU', 'PR': 'NA', 'QA': 'AS', 'RE': 'AF',
                     'RO': 'EU', 'RU': 'EU', 'RW': 'AF', 'BL': 'NA', 'SH': 'AF', 'KN': 'NA', 'LC': 'NA',
                     'MF': 'NA', 'PM': 'NA', 'VC': 'NA', 'WS': 'OC', 'SM': 'EU', 'ST': 'AF', 'SA': 'AS',
                     'SN': 'AF', 'RS': 'EU', 'SC': 'AF', 'SL': 'AF', 'SG': 'AS', 'SX': 'NA', 'SK': 'EU',
                     'SI': 'EU', 'SB': 'OC', 'SO': 'AF', 'ZA': 'AF', 'GS': 'AN', 'SS': 'AF', 'ES': 'EU',
                     'LK': 'AS', 'SD': 'AF', 'SR': 'SA', 'SJ': 'EU', 'SZ': 'AF', 'SE': 'EU', 'CH': 'EU',
                     'SY': 'AS', 'TW': 'AS', 'TJ': 'AS', 'TZ': 'AF', 'TH': 'AS', 'TL': 'AS', 'TG': 'AF',
                     'TK': 'OC', 'TO': 'OC', 'TT': 'NA', 'TN': 'AF', 'TR': 'AS', 'TM': 'AS', 'TC': 'NA',
                     'TV': 'OC', 'UG': 'AF', 'UA': 'EU', 'AE': 'AS', 'GB': 'EU', 'US': 'NA', 'UM': 'OC',
                     'VI': 'NA', 'UY': 'SA', 'UZ': 'AS', 'VU': 'OC', 'VE': 'SA', 'VN': 'AS', 'WF': 'OC',
                     'EH': 'AF', 'YE': 'AS', 'ZM': 'AF', 'ZW': 'AF'}

    """ Datafile to explore """

    @staticmethod
    def readData(data_file):
        data = open(data_file).readlines()
        return data

    """ Task 2b: Method to identify the countries that access the input document"""

    def infoCountry(self, doc_id, data_file):
        # try block
        try:
            # proceed only if doc_id is not an empty string
            if doc_id != "":
                # create an empty list
                countries = []
                # read the user selected data file as data
                data = self.readData(data_file)
                # for each data segment
                for d in data:
                    # if the env_doc_if exists as the key value
                    if 'subject_doc_id' in d:
                        # and if the the key value matches the doc_id provided
                        if json.loads(d)['event_type'] == "read" and json.loads(d)['subject_doc_id'] == doc_id:
                            # select the associated visitor country information and add in to
                            # the countries list
                            countries.append(json.loads(d)['visitor_country'])
                # return this list
                return countries
            # if the document id is blank prompt the user to provide one
            else:
                print("Please provide a valid Document ID")
        # to avoid exceptions during program execution place a except block
        except Exception as e:
            print("Please provide a valid Document ID")

    """ Task 2d: Method to identify the continents that access the input document """

    def infoContinents(self, doc_id, data_file):
        # try block
        try:
            # get all the countries that access the document
            countries = self.infoCountry(doc_id, data_file)
            # map the countries to the continents using the dictionary cntry_to_cont
            a = [self.cntry_to_cont[k] for k in countries]
            # return a list of continents based on the countries
            return a
        # to avoid exceptions during program execution place a except block
        except Exception as e:
            print("Please provide a valid Document ID")

    """ Task 3a: Browser information from the dataset """

    def infoBrowser(self, data_file):
        try:
            # create an empty list
            browser = []
            # read the user selected data file as data
            data = self.readData(data_file)
            # for every segment of data
            for d in data:
                # for data segments with event type as reader
                if json.loads(d)['event_type'] == "read":
                    # find the visitor user agent and add it to the list of browser
                    browser.append(json.loads(d)['visitor_useragent'])
            # return the browser list
            return browser
        # get the exception message if any
        except Exception as e:
            print(e)

    def infoBrowserSubset(self):
        bsubset = []
        b = self.infoBrowser()
        for i in b:
            sub = i.split('/')
            x = sub[0]
            if len(sub) > 2:
                y = sub[-2]
                info = list([val for val in y if val.isalpha()])
                z = "".join(info)
            bsubset.append(x + ' \n' + z)
        return bsubset

    """ Task 3b: Method takes the list of all user agents to collect information on popular browsers """

    def infoBrowserMatch(self, data_file):
        try:
            # create an empty list of browser subset
            bsubset = []
            # get the list of all user agents from the selected file
            b = self.infoBrowser(data_file)
            # for each user agent in the list
            for i in b:
                # split the user agent string into substrings when encountered with /
                sub = i.split('/')
                # let x be the first sub string
                x = sub[0]
                # if the substring has more than two units
                if len(sub) > 2:
                    # let y be the second last substring
                    y = sub[-2]
                    # for every second last substring use regex to find matches for popular browsers
                    for f in re.finditer(r'(?i)(firefox|msie|fbob|safari|trident)', y):
                        # append the bsubset list with first part which is x and matches in last part
                        bsubset.append(x + '\n' + f.group(0))
            # return the bsubset list
            return bsubset
        # get the exception message if any
        except Exception as e:
            print(e)

    """ Task 4: The method produces the final list of top 10 avid readers for the selected dataset"""

    def readtimes(self, data_file):
        # create an empty list of readers
        readers = []
        t = []
        # read the user selected data file as data
        data = self.readData(data_file)
        # for every data segment in user selected datafile
        for d in data:
            # if the data segment has a event_readtime as the key feature
            if 'event_readtime' in d:
                t.append(json.loads(d)['event_readtime'])
                readers.append(json.loads(d)['visitor_uuid'])
        # merge the two lists
        data_tuples = list(zip(readers, t))
        # create a dataframe for the readers and their associated read times
        d = pd.DataFrame(data_tuples, columns=['Top readers', 'time'])
        # group the the readers and sum the read time
        d = d.groupby(['Top readers']).sum()
        # sort the dataframe by time and get the top 10
        top_10 = d.sort_values(by=['time'], ascending=False).head(10)
        # print the list of top 10 readers
        first_column = top_10.iloc[:, 0]
        # return the top_10 acid readers
        return top_10

    """ Task 5a: The method returns all readers for the specified document in the selected datafile"""

    def getAllReaders(self, doc_id, data_file):
        try:
            # execute the code block if doc_id is provided by the user
            if doc_id != '':
                # crete an empty list of readers
                readers = []
                # read the user selected data file as data
                data = self.readData(data_file)
                # for all data segments in the selected data file
                for d in data:
                    # if the env_doc_id key exists
                    if 'subject_doc_id' in d and json.loads(d)['event_type'] == "read":
                        # and if the existing env_doc_id matches the doc_id provided
                        if json.loads(d)['subject_doc_id'] == doc_id:
                            # add all the associated readers using visitor_uuid as key to readers list
                            readers.append(json.loads(d)['visitor_uuid'])
                    # remove duplicates
                    readers = list(dict.fromkeys(readers))
                # return the list of readers
                return readers
            # if doc_id is not provided, prompt the user to provide one
            else:
                print('Please provide a valid document id to search')
        # provide an exception message
        except Exception as e:
            print('Please provide a valid document id to search')

    """ Task 5b: The method returns all the documents read by the reader specified using visitor id"""

    def getAllDocs(self, visitor_id, data_file):
        try:
            # execute the code block if a visitor_id is provided by the user
            if visitor_id != '':
                # create an empty list of documents
                docs = []
                # read the user selected data file as data
                data = self.readData(data_file)
                # for all data segments in the selected data file
                for d in data:
                    # if the visitor uuid exits
                    if 'visitor_uuid' in d and json.loads(d)['event_type'] == "read":
                        # and if the visitor uuid matched with the visitor id provided
                        if json.loads(d)['visitor_uuid'] == visitor_id:
                            # if the env doc if exists
                            if 'subject_doc_id' in d:
                                # add the visitor associated doc ids to the docs list
                                docs.append(json.loads(d)['subject_doc_id'])
                # remove duplicates
                docs = list(dict.fromkeys(docs))
                # return the docs list
                return docs
            # if the visitor id is not provided, prompt the user to provide one
            else:
                print('Please provide a valid visitor id to search')
        # provide an exception message
        except Exception as e:
            print('Please provide a valid visitor id to search')

    """ Task 5cd: The method provided a list of top 10 documents that are also liked by other readers
    of the specified document"""

    def alsoLikes(self, doc_id, data_file):
        try:
            # execute the code block if doc_id is provided by the user
            if doc_id != '':
                # create empty containers to collected docs and visitors
                e = [[]]
                r = []
                # get all the readers based on the specified doc_id
                v = self.getAllReaders(doc_id, data_file)
                # for all visitors in the list
                for i in v:
                    # get all the documents
                    d = self.getAllDocs(i, data_file)
                    # remove the input doc_id
                    d.remove(doc_id)
                    # add these to the nested list
                    e.append(d)
                # convert this to a dataframe
                e = pd.DataFrame(e)
                # remove the redundant top row
                e = e.drop([0], axis=0)
                # convert the dataframe to a list
                f = e.values.tolist()
                # merge the list
                f = reduce(lambda x, y: x + y, f)
                # remove all none
                f = list(filter(None, f))
                # count the frequency
                a = (Counter(f))
                # provide a list of 10 most common based on the frequency count
                b = a.most_common(10)
                # create a data frame
                doc = pd.DataFrame(b, columns=['Doc', 'Count'])
                # return the list of to 10 commonly liked documents
                return doc
            # if the document id is not provided, prompt the user to provide one
            else:
                print('Please provide a valid Document ID')
        # provide with exception message
        except Exception as e:
            print('Please provide a valid document id to search')

    """ Task 5cd: The method provides top 10 commonly liked documents based on the specified document"""

    def alsoLikesDocs(self, doc_id, data_file):
        try:
            # execute the code block if the document id is provided
            if doc_id != '':
                # get commonly liked documents based on the document id provided
                d = self.alsoLikes(doc_id, data_file)
                # create a dataframe of the information obtained
                doc = pd.DataFrame(d, columns=['Doc', 'Count'])
                # return the dataframe
                return doc
            else:
                print('Please provide a valid Document ID')
        except Exception as e:
            print('Please provide a valid document id to search')

    """ Task 5cd: The method provides top 10 commonly liked documents based on the specified visitor"""

    def alsoLikesVisitor(self, visitor_uuid, data_file):
        try:
            # execute code block only if visitor id is provided
            if visitor_uuid != '':
                # get a list of documents read by the specified visitor
                doc = self.getAllDocs(visitor_uuid, data_file)
                # for each document in the doc list get the readers and their respective documents
                # find the top 10 common docs in those
                for i in doc:
                    v = self.alsoLikes(i, data_file)
                    # create a data frame
                    docs = pd.DataFrame(v, columns=['Doc', 'Count'])
                # return the list of top 10 documents
                return docs
            # if the visitor id is not provided, prompt the user to provide one
            else:
                print('Please provide a valid Visitor ID')
        # provide with exception message
        except Exception as e:
            print('Please provide a valid Visitor id to search')

    """ Task 5d: The method provides top 10 commonly liked documents based on the specified visitor and 
    document id """

    def alsoLikesDocs_Visitor(self, doc_id, visitor_id, data_file):
        try:
            # execute if both document and visitor id are provided
            if doc_id != '' and visitor_id != '':
                # read the user selected data file as data
                data = self.readData(data_file)
                # for all data segments in the selected data file
                for d in data:
                    # if the env_doc_id exists as a key value
                    if 'subject_doc_id' in d and json.loads(d)['event_type'] == "read":
                        # if the input visitor id and doc id match
                        if json.loads(d)['visitor_uuid'] == visitor_id and json.loads(d)['subject_doc_id'] == doc_id:
                            # get the top 10 commonly liked documents
                            doc = self.alsoLikes(doc_id, data_file)
                            # create a data frame
                            doc = pd.DataFrame(doc, columns=['Doc', 'Count'])
                # return the data frame
                return doc
            else:
                print('Please provide valid Document and Visitor IDs')
        except Exception as e:
            print('Please provide valid Document and Visitor IDs')

    """ Task 6: The method produces visitors from graphical representation of task 5d"""

    def getVisitorsForGraph(self, doc_id, visitor_id, data_file):
        # create an empty nested list
        e = [[]]

        # collect the readers for the document id provided from the selected data file
        v = self.getAllReaders(doc_id, data_file)
        if visitor_id != '':
            v.remove(visitor_id)

        # for all visitors in the list v
        for i in v:
            # get the documents read by them
            d = self.getAllDocs(i, data_file)
            # remove the document id which was used to search
            d.remove(doc_id)
            # add these documents to the nested list e
            e.append(d)
        # convert the nested list to a dataframe
        reader_docs = pd.DataFrame(e)

        # remove redundant row
        reader_docs = reader_docs.drop([0], axis=0)

        # add the visitors as a column to the dataframe e
        reader_docs['visitor'] = v


        # return the dataframe
        return reader_docs

    """ Task 6: The method generates dataframe of readers and documents read by them based on either document
     id or both document and visitor ids"""

    def alsoLikesForGraph(self, doc_id, visitor_id, data_file):
        # create empty lists
        e = [[]]
        # r = []
        # if both document and visitor ids are provided
        if doc_id != '' and visitor_id != '':
            # read the user selected data file as data
            data = self.readData(data_file)
            # for all data segments in datafile
            for d in data:
                # for readers when subject doc id exists
                if 'subject_doc_id' in d and json.loads(d)['event_type'] == "read":
                    # and if the visitor and document ids match
                    if json.loads(d)['visitor_uuid'] == visitor_id and json.loads(d)['subject_doc_id'] == doc_id:
                        # get the dataframe of visitors and documents
                        e = self.getVisitorsForGraph(doc_id, visitor_id, data_file)
                        # return the dataframe
                        return e

        else:
            # read the user selected data file as data
            data = self.readData(data_file)
            # for all data segments in datafile
            for d in data:
                # for readers when subject doc id exists
                if 'subject_doc_id' in d and json.loads(d)['event_type'] == "read":
                    # if the document matches any in the data
                    if json.loads(d)['subject_doc_id'] == doc_id:
                        # get all visitors and the documents read by them
                        e = self.getVisitorsForGraph(doc_id, visitor_id, data_file)
                        # return the data frame
                        return e

        return e

    """ Task 6: Produces the dot graph for also likes function"""

    def alsoLikesGraph1(self, doc_id, visitor_id, data_file):
        try:
            # create a dot object
            dot = Digraph()
            # get the dataframe of visitors and the documents they like to read
            liked_Docs = self.alsoLikesForGraph(doc_id, visitor_id, data_file)
            # check if the dataframe is not  empty before proceeding
            if liked_Docs.empty:
                print('No matches found! Please use the correct data file or provide correct IDs')
            # proceed with the dataframe is not empty
            else:
                # get the last four alphabets of the doc if
                doc_id = doc_id[-4:]
                # define the attributes of the graph
                dot.node(doc_id, style='filled', fillcolor='green')
                # define how the edge will look
                dot.edge_attr.update(arrowhead='vee', arrowsize='2')
                # if the visitor id is provided then define its node and edge
                if visitor_id != '':
                    dot.node(visitor_id[-4:], style='filled', fillcolor='green')
                    dot.edge(visitor_id[-4:], doc_id)
                # convert the dataframe to dictionary
                d = liked_Docs.set_index('visitor').T.to_dict('list')
                # define the keys and values and check them
                visitor = d.keys()
                # for each visitor
                for i in visitor:
                    # create nodes and edges
                    dot.node(i[-4:], shape='box', style='filled', fillcolor='pink')
                    dot.edge(i[-4:], doc_id)

                documents = d.values()
                # merge the list
                documents = reduce(lambda x, y: x + y, documents)
                # remove all none
                documents = list(filter(None, documents))
                # count the frequency
                topdoc = (Counter(documents))
                # provide a list of 10 most common based on the frequency count
                finalist = topdoc.most_common(10)
                # create a data frame
                docs = pd.DataFrame(finalist, columns=['TopDoc', 'Count'])
                updatedList = docs['TopDoc'].values
                for ud in updatedList:
                    dot.node(ud[-4:], style='filled', fillcolor='pink')
                    for docu in d.values():
                        for f in docu:
                            if f == ud:
                                key = d.keys()

                for k in key:
                    # get values from each key
                    for l in d.get(k):
                        # if the values are not none
                        if l is not None:
                            for di in updatedList:
                                if l == di:
                                    # define the edge
                                    dot.edge(k[-4:], l[-4:])

            # render the graph
            return dot.render('A', view=True)
        except Exception as e:
            print('Please provide valid Document or Visitor IDs or select the correct dataset')



