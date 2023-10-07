
#How to import your module from the modules folder
from modules import test 

#Used to inport env API token
from dotenv import load_dotenv
load_dotenv('.env')

#Call module using modulename.modulefunction()
test.initial_test()