import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/Astrology"

def generate_wiki_data(url):
    text = requests.get(url).text
    soup_object = BeautifulSoup(text)
    allp = soup_object.findAll("p")
    allp_text = [allp[i].text for i in range(len(allp))]
    wiki_text = " ".join(allp_text)
    return wiki_text

chem = ["compounds", "atoms", "molecules", "ions", "reaction", 
			 "chemist", "substances", "laboratory", "particles",
			 "energy", "radioactive", "matter", "photon", "mass",
			 "atomic_nucleus", "ionization", "metallic", "covalent",
			 "periodic", "isotopes", "solids", "silica", "sulfur", 
			 "sodium", "carbon", "alloy", "avogadro", "liquid", "oxidation",
			 "chloride", "plasma", "hydronium", "quanta", "phonons", "hydrogen",
			 "sulfied", "kinetics", "hydroxide", "phosphate", "redox", "molar",
			 "molarity", "helium", "krypton"]

phys = ["energy", "force", "astronomy", "sun", "moon", "stars",
		   "planets", "optic", "gravitation", "gravity", "thermodynamics", 
		   "electromagnetics", "theory_of_relativity", "photoelectric_effect",
		   "speed_of_light", "motion", "superconductivity", "higgs_boson",
		   "quantum", "quantum_mechanics", "supersymmetry", "neutrinos", "meissner_effect",
		   "magnetic_field", "fluxons", "electric_current", "geomagnetism", "inertia",
		   "newton's_laws_of_motion", "classical_mechanics", "kepler's_law","planet",
		   "thermonuclear", "fusion", "orbit", "ellipse"]


chem_short = ["compounds", "atoms", "molecules", "ions"]
phys_short = ["energy", "force", "astronomy", "sun", "moon"]


wiki_initial = "https://en.wikipedia.org/wiki/"

def make_ml_classification_data(label1, label2,topic1_list,topic2_list):
    
    topic1_data = []
    topic2_data = []
    for topic1 in topic1_list:
        curr_url = wiki_initial + topic1
        topic1_data.append(generate_wiki_data(curr_url))
    for topic2 in topic2_list:
        curr_url = wiki_initial + topic2
        topic2_data.append(generate_wiki_data(curr_url))

    topic1_labels = [label1 for i in range(len(topic1_data))]
    topic2_labels = [label2 for i in range(len(topic2_data))]

    data1 = pd.DataFrame({"Text":topic1_data, "Label":topic1_labels})
    data2 = pd.DataFrame({"Text":topic2_data, "Label":topic2_labels})

    combined_data = pd.concat([data1, data2])

    return combined_data
    
    
    







    






