import nltk
nltk.download('all')
parser = nltk.parse.malt.MaltParser(working_dir="/home/rostunov/workspace/malt_wrapper",
                                     mco="test123",
                                     additional_java_args=['-Xmx512m'])
txt = "This is a test sentence"
graph = parser.raw_parse(txt)
graph.tree().pprint()