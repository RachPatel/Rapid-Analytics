__author__ = "Rachana Patel"
__version__ = "Rapid_Analytics_2.1"
__email__ = "rrp3@hw.ac.uk"
__status__ = "Prototype"
__ide__ = "PyCharm Community 2020.2"
__language__ = "Python 3.8"

""" Packages"""

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import Counter
from graphviz import Digraph
from Information import Information
from optparse import OptionParser

""" Set the GUI size """
root = Tk()
root.title('Rapid Analytics')
root.geometry("1000x400")

""" Variable to be used """
user_doc_input = StringVar(root)

"""Create an Information object to access the methods"""
I = Information()
doc_id = ""
visitor_id = ""
d = StringVar()
data_file = d.set('issuu_cw2.json')

""" Clear button to clear text inputs"""


def clear():
    e.delete(0, END)
    e2.delete(0, END)


"""Task 2a: The method produces a graph of countries that have accessed the input document ID"""


def viewByCountry(doc_id, data_file):
    try:
        countries = I.infoCountry(doc_id, data_file)
        if countries != []:
            # use counter to count the number of occurrences
            c = Counter(countries)
            # using matplotlib plot the graph using elements as keys and
            # counts as values with associated aesthetics
            plt.bar(c.keys(), c.values(), color=(0.4, 0.7, 0.8, 0.75))
            # provide appropriate labels and title
            plt.ylabel('Counts')
            plt.xlabel('Countries')
            plt.title('Viewer counts for doc: \n' + str(doc_id))
            # show the plot
            plt.show()
        else:
            messagebox._show('', "Please Provide a Valid Document ID or select the correct datafile")
    except:
        print("Please Provide a Valid Document ID or select the correct datafile")


""" Task 2a: Method enables GUI usage to produce a graph of countries that have accessed the input document ID """


def graphByCountry():
    # get the doc_id from the input textbox
    doc_id = e.get()
    try:
        # if the document ID is not empty run the code block
        if doc_id != '':
            # get the user selected datafile
            data_file = (selectRadioButton(d.get()))
            # create a list of countries by calling the infoCountry
            # method that uses doc_id as one of the parameters
            viewByCountry(doc_id, data_file)
        # in case the document id is not provided, prompt the use to provide a valid one
        else:
            # pop-up message box
            messagebox._show('', "Please Provide a Valid Document ID")
    except:
        messagebox._show('', "Please Provide a Valid Document ID or select the correct datafile")


""" Task 2b: The method produces a graph of continents that have accessed the input document ID """


def viewByContinent(doc_id, data_file):
    try:
        continents = I.infoContinents(doc_id, data_file)
        if continents != []:
            # use counter to count the number of occurrences
            c = Counter(continents)
            # using matplotlib plot the graph using elements as keys and
            # counts as values with associated aesthetics
            plt.bar(c.keys(), c.values(), color=(0.5, 0.0, 0.5, 0.5))
            # appropriate labels and title
            plt.ylabel('Counts')
            plt.xlabel('Continents')
            plt.title('Viewer counts for doc: \n' + str(doc_id))
            # show the plot
            plt.show()
        else:
            messagebox._show('', "Please Provide a Valid Document ID or select the correct datafile")
    except:
        print("Please Provide a Valid Document ID or select the correct datafile")


"""Task 2b: The method enables GUI usage to produce a graph of continents that have accessed the input document ID"""


def graphByContinent():
    # get the doc_id from the input textbox
    doc_id = e.get()
    try:
        # if the document ID is not empty run the code block
        if doc_id != '':
            # get the user selected datafile
            data_file = (selectRadioButton(d.get()))
            # create a list of continents by calling the infoContinents
            # method that uses doc_id as one of the parameters
            viewByContinent(doc_id, data_file)
        else:
            # pop-up message box
            messagebox._show('', "Please Provide a Valid Document ID")
    except:
        messagebox._show('', "Please Provide a Valid Document ID or select the correct datafile")


""" Task 3a: The method produces a graph of all browsers in the specified dataset"""


def viewsByBrowser(data_file):
    try:
        # obtain a list of browsers from user selected datafile
        browsers = I.infoBrowser(data_file)
        # using Counter count the frequency of each browser
        c = Counter(browsers)
        # using matplotlib plot the graph using elements as keys and
        # counts as values with associated aesthetics
        plt.bar(c.keys(), c.values(), color=(0.5, 0.0, 0.8, 0.5))
        # appropriate labels and title
        plt.ylabel('Counts')
        plt.xlabel('Visitor Useragents')
        # show the plot
        plt.show()
    except:
        print("OOps! something is not right! Please select another datafile")


""" Task 3a: The method enables GUI usage to produce a graph of all browsers in the specified dataset"""


def graphByBrowser():
    try:
        # get the user selected datafile
        data_file = (selectRadioButton(d.get()))
        viewsByBrowser(data_file)
    except:
        messagebox._show('', "OOps! something is not right! Please select another datafile")


""" Task 3b: The method produces graph of popular browsers based on first and last matches for visitor user agent """


def popularBrowsers(data_file):
    try:
        # obtain a list of matched browsers from user selected datafile
        browsers = I.infoBrowserMatch(data_file)
        # use counter to count the frequency
        c = Counter(browsers)
        # using matplotlib plot the graph using elements as keys and
        # counts as values with associated aesthetics
        plt.bar(c.keys(), c.values(), color=(0.5, 0.0, 0.8, 0.5))
        # labels
        plt.ylabel('Counts')
        plt.xlabel('Popular Browsers')
        # adjust the graph vs label area
        plt.subplots_adjust(bottom=0.2, top=0.9)
        # show the plot
        plt.show()
    except:
        print("OOps! something is not right! Please select another datafile")


""" Task 3b: The method enables GUI usage t0 produce graph of popular browsers based on first 
and last matches for visitor user agent """


def graphByBrowserSubset():
    try:
        # get the user selected datafile
        data_file = (selectRadioButton(d.get()))
        popularBrowsers(data_file)
    except:
        messagebox._show('', "OOps! something is not right! Please select another datafile")


""" Task 4: The method prints top 10 readers in the data file"""


def avidReaders(data_file):
    try:
        # create a data frame with top 10 readers and their reading time in the data file selected
        r = I.readtimes(data_file)
        print(r)
    except:
        print("OOps! something is not right! Please select another datafile")


""" Task 4: The method enables GUI usage to pop up a message box showing top 10 readers in the data file """


def popUpAvidReaders():
    try:
        # get the user selected datafile
        data_file = (selectRadioButton(d.get()))
        # create a data frame with top 10 readers and their reading time in the data file selected
        df = I.readtimes(data_file)
        # get the information to be printed
        first_column = df.iloc[:, 0]
        r = str(first_column)
        # open a pop up message box displaying top 10 readers
        messagebox._show('', r)
    except:
        messagebox._show('', "OOps! something is not right! Please select another datafile")


""" Task 5a: Get all readers for the specified document in the specified dataset"""


def docReaders(doc_id, data_file):
    try:
        print(str(I.getAllReaders(doc_id, data_file)))
    except:
        print("Please Provide a Valid Document ID or select the correct datafile")


""" Task 5a: The method pops up a message box showing the readers based on their visitor id who have
read the specified document from the selected datafile """


def getDocReaders():
    # get the doc_id from the input textbox
    doc_id = e.get()
    try:
        # if the document ID is not empty run the code block
        if doc_id != '':
            # get the user selected datafile
            data_file = (selectRadioButton(d.get()))
            # get all the readers that have read the document in the data file
            readers = I.getAllReaders(doc_id, data_file)
            if readers != []:
                # format the list to be printed on GUI message box
                r = str('\n'.join('{}: {}'.format(*k) for k in enumerate(readers)))
                # message box pop up to display the readers using their visitor ids
                messagebox._show('', r)
            else:
                messagebox._show('', "No matches found. \n "
                                     "Please Provide a Valid Document ID or select the correct datafile")
        else:
            # pop-up message box
            messagebox._show('', "Please Provide a Valid Document ID")
    except:
        messagebox._show('', "Please Provide a Valid Document ID or select the correct datafile")


""" Task 5b: The method prints all the documents read by the specified reader in specified dataset"""


def docsByReaders(visitor_id, data_file):
    try:
        # get all the documents for the specified visitor
        print(str(I.getAllDocs(visitor_id, data_file)))
    except:
        print("Please Provide a Valid Visitor ID or select the correct datafile")


""" Task 5b: The method pops up a message box showing the documents based for the specified visitor id
in the selected datafile """


def getDocs():
    # get the visitor_id from the input textbox
    visitor_id = e2.get()
    try:
        # execute only if the visitor id is provided
        if visitor_id != '':
            # get the user selected datafile
            data_file = (selectRadioButton(d.get()))
            # get all the documents for the specified visitor
            docs = I.getAllDocs(visitor_id, data_file)
            # execute the code only if the doc is not empty
            if docs != []:
                # convert the list to string format for display
                r = str('\n'.join('{}: {}'.format(*k) for k in enumerate(docs)))
                # pop up message box with the list of documents
                messagebox._show('', r)
            else:
                messagebox._show('', "No matches found. \n"
                                     "Please Provide a Valid Visitor ID or select the correct datafile")
        # if the visitor id is not provided, prompt the user to provide one
        else:
            # pop-up message box
            messagebox._show('', "Please Provide a Valid Visitor ID")
    except:
        messagebox._show('', "Please Provide a Valid Visitor ID or select the correct datafile")


""" Task 5c&d: The method pops up a message box showing the top 10 commonly liked documents
based on doc_id or visitor_id specified """


def Top10DocOrVisitor():
    try:
        # get the doc_id from the input textbox
        doc_id = e.get()
        # get the visitor_id from the input textbox
        visitor_id = e2.get()
        # if only doc id is provided
        if doc_id != '' and visitor_id == '':
            # get the user selected datafile
            data_file = (selectRadioButton(d.get()))
            # get op 10 commonly liked documents based on the doc_id provided
            docs = I.alsoLikesDocs(doc_id, data_file)
            # execute the code only in docs is not empty
            if docs.empty:
                messagebox._show('', "No matches found. \n"
                                     "Please Provide a Valid Document ID or select the correct datafile")
            else:
                # get the information to be printed
                r = str(docs[['Count', 'Doc']].to_string(header=False, index=False))
                messagebox._show('', r)

                # if only visitor id is provided
        elif doc_id == '' and visitor_id != '':
            # get the user selected datafile
            data_file = (selectRadioButton(d.get()))
            # get op 10 commonly liked documents based on the doc_id provided
            docs = I.alsoLikesVisitor(visitor_id, data_file)
            if docs is None:
                messagebox._show('', "No matches found. \n"
                                     "Please Provide a Valid Visitor ID or select the correct datafile")
            else:
                # get the information to be printed
                r = str(docs[['Count', 'Doc']].to_string(header=False, index=False))
                messagebox._show('Count & Doc ID', r)

        # if both doc and visitor ids are provided
        elif doc_id != '' and visitor_id != '':
            # get the user selected datafile
            data_file = (selectRadioButton(d.get()))
            # get op 10 commonly liked documents based on the doc_id provided
            docs = I.alsoLikesDocs_Visitor(doc_id, visitor_id, data_file)
            if docs is None:
                messagebox._show('', "No matches found. \n"
                                     "Please Provide a Valid Document ID or visitor ID or select the correct datafile")
            else:
                # get the information to be printed
                r = str(docs[['Count', 'Doc']].to_string(header=False, index=False))
                messagebox._show('Count & Doc ID', r)
    except:
        messagebox._show('', "Oops! No matches found. \n"
                             "Please Provide a Valid Document ID or visitor ID or select the correct datafile")


"""Task 5d: Method is used for commandline usage to give a list of top 10 commonly liked documents based on the 
inputs provided """


def commonlyLikedDocs(doc_id, visitor_id, data_file):
    try:
        # if only doc id is provided
        if doc_id != '' and visitor_id == '':
            # get the user selected datafile
            data_file = (selectRadioButton(d.get()))
            # get op 10 commonly liked documents based on the doc_id provided
            docs = I.alsoLikesDocs(doc_id, data_file)
            # execute the code only in docs is not empty
            if docs.empty:
                print("No matches found. \n"
                      "Please Provide a Valid Document ID or select the correct datafile")
            else:
                # get the information to be printed
                r = str(docs[['Count', 'Doc']].to_string(header=False, index=False))
                print(r)
        elif doc_id == '' and visitor_id != '':
            # get op 10 commonly liked documents based on the doc_id provided
            docs = I.alsoLikesVisitor(visitor_id, data_file)
            if docs is None:
                print("No matches found. \n"
                      "Please Provide a Valid Visitor ID or select the correct datafile")
            else:
                # get the information to be printed
                r = str(docs[['Count', 'Doc']].to_string(header=False, index=False))
                print(r)
        elif doc_id != '' and visitor_id != '':
            # get op 10 commonly liked documents based on the doc_id provided
            docs = I.alsoLikesDocs_Visitor(doc_id, visitor_id, data_file)
            if docs is None:
                print("No matches found. \n"
                      "Please Provide a Valid Document ID or visitor ID or select the correct datafile")
            else:
                # get the information to be printed
                r = str(docs[['Count', 'Doc']].to_string(header=False, index=False))
                print(r)
    except:
        print("Oops! No matches found. \n"
              "Please Provide a Valid Document ID or visitor ID or select the correct datafile")


""" Task 6: Method is used for command line usage to render the 'also likes' graph"""


def alsoLikesGraph(doc_id, visitor_id, data_file):
    try:
        if doc_id != '':
            I.alsoLikesGraph1(doc_id, visitor_id, data_file)
    except:
        print("please provide a Valid Document ID or Visitor ID or select the correct datafile")


""" Task 6: Render the also likes function as a dot graph """

dot = Digraph(comment='Also likes graph')


def getAlsoLikesGraph():
    try:
        # get the doc_id from the input textbox
        doc_id = e.get()
        # get the visitor_id from the input textbox
        visitor_id = e2.get()
        # get the user selected datafile
        data_file = (selectRadioButton(d.get()))
        # if the document id is provided
        if doc_id != '':
            # inform the user that the graph will appear in some time and possibility of an incorrect file being chosen
            messagebox._show('', " Please wait the graph will appear soon. If it does not appear, \n"
                                 "please provide a Valid Document ID or Visitor ID or select the correct datafile")
            # render the also likes graph based on the information provided
            I.alsoLikesGraph1(doc_id, visitor_id, data_file)

        # if the doc id is not provided, prompt the user to provide one
        else:
            messagebox._show('', "Please Provide a Valid Document ID ")
    except:
        messagebox._show('', " Please wait the graph will appear soon. If it does not appear, \n"
                             "please provide a Valid Document ID or Visitor ID or select the correct datafile")


def getInfo():
    info = [" 2a: Countries that viewed the documents", " 2b: Continent that viewed the document",
            " 3a: All browsers used", "3b: Popular Browsers", " 4: Top 10 avid readers",
            " 5a: All readers for the document ", " 5b: All documents by the reader ",
            " 5d: Most liked documents based on the input document ",
            " 6: Graph for readers and commonly liked documents "]
    messagebox._show("Information", str(info))

""" GUI design components """

""" Input labels and textboxes """

entry = Entry(root, textvariable=user_doc_input)

blankLabel1 = Label(root, text=' Please ensure no blank spaces are left before the document and visitor ID')
blankLabel1.grid(row=0, column=0, columnspan=10)

blankLabel2 = Label(root, text='')
blankLabel2.grid(row=6, column=0, columnspan=5)

docLabel = Label(root, text='Doc ID')
docLabel.grid(row=1, column=0)
e = Entry(root, width=70)
e.grid(row=1, column=1)

visitorLabel = Label(root, text='Visitor ID')
visitorLabel.grid(row=8, column=0)
e2 = Entry(root, width=70)
e2.grid(row=8, column=1)

""" Task buttons """

button1 = Button(root, text='Task2a', command=graphByCountry)
button1.grid(row=1, column=2)

button1a = Button(root, text='Task2b', command=graphByContinent)
button1a.grid(row=1, column=3)

button3 = Button(root, text='Clear', command=clear)
button3.grid(row=9, column=1)

button4 = Button(root, text='Task3a', command=graphByBrowser)
button4.grid(row=10, column=0)

button5 = Button(root, text='Task3b', command=graphByBrowserSubset)
button5.grid(row=11, column=0)

button6 = Button(root, text=' Task4 ', command=popUpAvidReaders)
button6.grid(row=12, column=0)

buttoninfo = Button(root, text = '   Info  ', command = getInfo)
buttoninfo.grid(row=13, column =0)


button7 = Button(root, text='Task5a', command=getDocReaders)
button7.grid(row=1, column=4)

button8 = Button(root, text='Task5b', command=getDocs)
button8.grid(row=8, column=2)

button10 = Button(root, text='Task5d', command=Top10DocOrVisitor)
button10.grid(row=8, column=3)

button11 = Button(root, text=' Task6 ', command=getAlsoLikesGraph)
button11.grid(row=8, column=4)

""" For dataset selection """

def selectRadioButton(value):
    return str(value)

dataLabel = Label(root, text='Please select a dataset')
dataLabel.grid(row=10, column=1)

radiobutton1 = Radiobutton(root, text='issuu_cw2 dataset', variable=d, value="issuu_cw2.json",
                           command=lambda: selectRadioButton(d.get()))
radiobutton1.grid(row=11, column=1)

radiobutton2 = Radiobutton(root, text='sample_100k_lines dataset', variable=d, value="sample_100k_lines.json",
                           command=lambda: selectRadioButton(d.get()))
radiobutton2.grid(row=12, column=1)

radiobutton3 = Radiobutton(root, text='sample_400k_lines dataset', variable=d, value="sample_400k_lines.json",
                           command=lambda: selectRadioButton(d.get()))
radiobutton3.grid(row=13, column=1)

radiobutton4 = Radiobutton(root, text='sample_600k_lines dataset', variable=d, value="sample_600k_lines.json",
                           command=lambda: selectRadioButton(d.get()))
radiobutton4.grid(row=14, column=1)

radiobutton5 = Radiobutton(root, text='sample_3m_lines dataset', variable=d, value="sample_3m_lines.json",
                           command=lambda: selectRadioButton(d.get()))
radiobutton5.grid(row=15, column=1)


""" Method for parsing arguments for command line usage """

def main():
    parser = OptionParser()
    parser.add_option('-u')
    parser.add_option('-d')
    parser.add_option('-t')
    parser.add_option('-f')
    parser.set_defaults(u='')
    (options, args) = parser.parse_args()
    visitor_id = str(options.u)
    doc_id = str(options.d)
    task_id = str(options.t)
    data_file = str(options.f)
    if task_id == '2a':
        viewByCountry(doc_id, data_file)
    elif task_id == '2b':
        viewByContinent(doc_id, data_file)
    elif task_id == '3a':
        viewsByBrowser(data_file)
    elif task_id == '3b':
        popularBrowsers(data_file)
    elif task_id == '4':
        avidReaders(data_file)
    elif task_id == '5a':
        docReaders(doc_id, data_file)
    elif task_id == '5b':
        docsByReaders(visitor_id, data_file)
    elif task_id == '5d':
        commonlyLikedDocs(doc_id, visitor_id, data_file)
    elif task_id == '6':
        alsoLikesGraph(doc_id, visitor_id, data_file)
    elif task_id == '7':
        alsoLikesGraph(doc_id, visitor_id, data_file)
        root.mainloop()

#root.mainloop()
""" Main method for programme execution """

if __name__ == '__main__':

    main()

    print()
