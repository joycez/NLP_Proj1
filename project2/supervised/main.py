from sup_preprocessing import *
from sup_model import *

def main():
##        fM1 = featureModel('training_data.data',3)
        fM1 = featureModel('sample.data',3)
        print fM1.probSense('allow.v','1')
        print fM1.probFeature('area.n','2','superiority')
               
if __name__ == "__main__":
  main()
