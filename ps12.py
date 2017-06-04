# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab
import matplotlib.pyplot as plt


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    
    def __init__(self):
        pass

    def isVirus(self):
        return "is not Virus"
#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        # TODO
        #prob of reproducing if you're  alive and the only one alive
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        #prob of dying each time step ^
        
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        # TODO
        #probability of dying
        floatRandNum = random.random()  
        if floatRandNum < self.clearProb:
            return True
        else:
            return False
            #lives

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. 
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        # TODO
        probOfRepro = self.maxBirthProb * (1 - popDensity)
        floatRandNum = random.random()  

        if floatRandNum < probOfRepro:
            childVirus = SimpleVirus(self.maxBirthProb, self.clearProb)
            return childVirus
        else:
            return NoChildException()

    def isVirus(self):
        return "is Virus"

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        # TODO 
        return len(self.viruses)       

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update() 

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        listVir = self.viruses
        newlistVir = []
        for virus in listVir:
            if virus.doesClear() == False:
                newlistVir.append(virus)


        currentPop = len(newlistVir)
        popDensity = float(currentPop) / self.maxPop


        reproList = []
        for virus in newlistVir:
                childVirus = virus.reproduce(popDensity)

                if childVirus.isVirus() == 'is Virus':
                    reproList.append(childVirus)

        newVirus =  newlistVir + reproList
        self.viruses = newVirus
        return self.viruses


#
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    # TODO
    """
    simVir = SimpleVirus(.3,.5)   
    print simVir.doesClear()
    newVir =  simVir.reproduce(.5)
    print newVir
    newPat = SimplePatient(newVir, .3)
    print newPat.getTotalPop()
    print newPat.update()
    """
    clearProb = 0.05
    maxProb = 0.1
    simVir = SimpleVirus(maxProb,clearProb)
    virList = 100 * [simVir]
    newPat = SimplePatient(virList, 1000)

    newPopListList = []
    for x in range(300):     
        newPopList = newPat.update()
        newPopListList.append(len(newPopList))

    plt.plot(newPopListList, 'ro')
    plt.ylabel('viruspop')
    plt.xlabel('time')
    plt.show()
        
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex. not resistence to 

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        # TODO
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        # TODO
        resDict = self.resistances 
        return resDict[drug]

        
    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # TODO
        willReproduce = True
        for drug in activeDrugs:
            if not self.getResistance(drug): 
                willReproduce = False
                return NoChildException()

        if willReproduce:  
            probOfRepro = self.maxBirthProb * (1 - popDensity)
            floatRandNum = random.random()  

            newResis = {}
            if floatRandNum < probOfRepro:
                for drug, resist in self.resistances.items():

                    willMutate = random.random() 
                    if willMutate < self.mutProb:
                        #probSwitch = self.mutProb
                        newResis[drug] = not resist
                    else:
                        newResis[drug] = resist

                childVirus = ResistantVirus(self.maxBirthProb, self.clearProb, newResis, self.mutProb)
                return childVirus
            else:
                return NoChildException()
            
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugsList = []
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        if newDrug not in self.drugsList:
            self.drugsList.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # TODO
        return self.drugsList
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        virusResistList = []
        virusList = self.viruses
        for drug in drugsList:
            for virus in virusList:
                if virus.getResistance(drug):
                    virusResistList.append(virus)

        return len(virusResistList)



    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly
          
        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        listVir = self.viruses
        newlistVir = []
        for virus in listVir:
            if virus.doesClear() == False:
                newlistVir.append(virus)


        currentPop = len(newlistVir)
        popDensity = float(currentPop) / self.maxPop

        reproList = []
        for virus in newlistVir:
                childVirus = virus.reproduce(popDensity, self.drugsList)
                if childVirus.isVirus() == 'is Virus':
                    reproList.append(childVirus)

        newVirus =  newlistVir + reproList
        self.viruses = newVirus
        return len(self.viruses)

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    clearProb = 0.05
    maxProb = 0.1
    #resist =  {'guttagonol':False} 
    resist = {'guttagonal': False}
    mutProb = .005
    resVir = ResistantVirus(maxProb,clearProb,resist, mutProb)
    virList = 100 * [resVir]
    newPat = Patient(virList, 1000)



    newPopListList = []
    for t in range(300): 
        if t == 150:
            newPat.drugsList.append('guttagonal')
        newPop = newPat.update()
        newPopListList.append(newPop)


    #print newPopListList
    plt.plot(newPopListList, 'ro')
    plt.ylabel('viruspop')
    plt.xlabel('time')
    plt.show()
#print problem4()
#
# PROBLEM 5
#
        
def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    # TODO
    
#
# PROBLEM 6
#

def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # TODO
    maxProb = 0.1
    clearProb = 0.05
    resist = {'guttagonol':False, 'grimpex':False} 
    mutProb = .005

    resVir = ResistantVirus(maxProb,clearProb,resist, mutProb)
    virList = 100 * [resVir]
    newPat = Patient(virList, 1000)

    basePopList =[]
    #timeSteps = 150+300+150
    #timeSteps = 150+150+150
    timeSteps = 150+75+150
    for t in range(timeSteps):
        if t == 150:
            newPat.drugsList.append('guttagonol')
        #if t == 150:
            newPat.drugsList.append('grimpex')

        basePop = newPat.update()
        basePopList.append(basePop)

            

    graphPop = basePopList
    plt.plot(graphPop, 'ro')
    plt.ylabel('viruspop')
    plt.xlabel('time')
    plt.show()
print problem6()



#
# PROBLEM 7
#
     
def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    # TODO



