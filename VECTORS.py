#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Michael
#
# Created:     07/05/2013
# Copyright:   (c) Michael 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import RADIANSDEGREES

class Vecs:

    def __init__(self, listVecs):

        """
        (List of tuples)
        listVecs = [(12.52, 46.4), (18.93, 312), (16.3, 240)]
        """

        self.listVecs = listVecs
        self.numVecs = len(self.listVecs)
        #self.reference = 0
        self.vectorsMagDeg()
        self.reference = RADIANSDEGREES.rad2degrees(math.atan(abs(self.y)/abs(self.x)))

    def vectorsMagDeg(self):
        Xs = []
        Ys = []
        for i in range(self.numVecs):
            Xs.append(math.cos(RADIANSDEGREES.degrees2rad(self.listVecs[i][1]))*self.listVecs[i][0])
            #print(str(i+1) + ". cosine of " + str(self.listVecs[i][1]) + " times " + str(self.listVecs[i][0]) + " = " + str(round(math.cos(RADIANSDEGREES.degrees2rad(self.listVecs[i][1]))*self.listVecs[i][0], 2)))
            #self.stringer = "cos(" + str(self.listVecs[i][1]) + ") * " + str(self.listVecs[i][0])
            Ys.append(math.sin(RADIANSDEGREES.degrees2rad(self.listVecs[i][1]))*self.listVecs[i][0])
            #print(str(i+1) + ". sine of " + str(self.listVecs[i][1]) + " times " + str(self.listVecs[i][0]) + " = " + str(round(math.sin(RADIANSDEGREES.degrees2rad(self.listVecs[i][1]))*self.listVecs[i][0], 2)))
        self.x = sum(Xs)
        #print("Sum of " + str(Xs) + " X's is "  + str(round(self.x, 2)))
        self.y = sum(Ys)
        #print("Sum of " + str(Ys) + " Y's is "  + str(round(self.y, 2)))


    def pt(self):
        #print("Pythagorean Theorum - square root of " + str(round(self.x,2)) + " squared plus " + str(round(self.y,2))  + " squared equals " + str(round(RADIANSDEGREES.pyth(self.x,self.y),2)))
        return RADIANSDEGREES.pyth(self.x,self.y)

    def refAng(self):
        #print("Reference angle is the inverse tangent of " + str(round(abs(self.y),2)) + " divided by " + str(round(abs(self.x),2)) + " equals "+ str(round(RADIANSDEGREES.rad2degrees(math.atan(abs(self.y)/abs(self.x))),2)))

        return RADIANSDEGREES.rad2degrees(math.atan(abs(self.y)/abs(self.x)))

    def rotAng(self):

        if self.x >= 0 and self.y >= 0:
            #rot = self.reference
            #print("Positve X and Y, so Angle in Quadrant I")
            return self.refAng()
        elif self.x < 0 and self.y >= 0:
            #180-self.reference
            #print("Negatve X positive Y, so Rotate reference angle to Quadrant II, 180 degrees minus " + str(round(self.reference,2)) + " is " + str(round(180-self.reference,2)) + " degrees")
            return 180-self.refAng()
        elif self.x < 0 and self.y < 0:
            #rot = 180+self.reference
            #print("Negative X and Y, so Rotate reference angle to Quadrant III, 180 degrees plus " + str(round(self.reference,2)) + " is " + str(round(180+self.reference,2)) + " degrees")
            return 180+self.refAng()
        else:
            #rot = 360-self.reference
            #print("Rotate reference angle to Quadrant IV, 360 degrees minus " + str(round(self.reference,2)) + " is " + str(round(360-self.reference,2)) + " degrees")
            return 360-self.refAng()

    def __str__(self):

        return "X = " + str(round(self.x, 2)) + " and Y = " + str(round(self.y, 2)) +  "\tVector = (" + str(round(self.pt(), 2)) + ", " + str(round(self.rotAng(), 2)) + ")"


if __name__ == '__main__':

    s1 = Vecs([(12, 220), (34.3, 190)])
    #s2 = Vecs([(45.52, 123.4), (18.1, 359), (21.3, 12)])

    print(s1)
    #print(s2)

##        MAG = RADIANSDEGREES.pyth(X,Y)
##        #refAng = math.degrees(math.atan(abs(Y)/abs(X)))
##        refAng = RADIANSDEGREES.rad2degrees(math.atan(abs(Y)/abs(X)))
##
##        if X >= 0 and Y >= 0:
##            return "(" + str(round(MAG, 2)) + ", " + str(round(refAng, 2)) + ")"
##        elif X < 0 and Y >= 0:
##            return "(" + str(round(MAG, 2)) + ", " + str(round(180-refAng, 2)) + ")"
##        elif X < 0 and Y < 0:
##            return "(" + str(round(MAG, 2)) + ", " + str(round(180+refAng, 2)) + ")"
##        else:
##            return "(" + str(round(MAG, 2)) + ", " + str(round(360-refAng, 2)) + ")"

##    def threeVectorsDeg(self):
##
##        X = (math.cos(RADIANSDEGREES.degrees2rad(angleA))*magA) + (math.cos(RADIANSDEGREES.degrees2rad(angleB))*magB) + (math.cos(RADIANSDEGREES.degrees2rad(angleC))*magC)
##
##        Y = (math.sin(RADIANSDEGREES.degrees2rad(angleA))*magA) + (math.sin(RADIANSDEGREES.degrees2rad(angleB))*magB) + (math.cos(RADIANSDEGREES.degrees2rad(angleC))*magC)
##
##        MAG = RADIANSDEGREES.pyth(X,Y)
##        #refAng = math.degrees(math.atan(abs(Y)/abs(X)))
##        refAng = RADIANSDEGREES.rad2degrees(math.atan(abs(Y)/abs(X)))
##
##        if X >= 0 and Y >= 0:
##            return "(" + str(round(MAG, 2)) + ", " + str(round(refAng, 2)) + ")"
##        elif X < 0 and Y >= 0:
##            return "(" + str(round(MAG, 2)) + ", " + str(round(180-refAng, 2)) + ")"
##        elif X < 0 and Y < 0:
##            return "(" + str(round(MAG, 2)) + ", " + str(round(180+refAng, 2)) + ")"
##        else:
##            return "(" + str(round(MAG, 2)) + ", " + str(round(360-refAng, 2)) + ")"


#print(twoVectorsDeg(12.52, 46.4, 18.93, 312))

#RADIANSDEGREES.degrees2rad(90)
##>>> math.degrees(math.cos(120))
##-28.647889756541147
##
##>>> math.degrees(math.cos(2.0943951023931953))
##-28.647889756541147
