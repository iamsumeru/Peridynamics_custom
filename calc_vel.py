#! /usr/bin/env python

from math import sqrt

if __name__ == "__main__":

    message =  "\nThis script determines the initial velocities required to break\n"
    message += "a bond between two peridynamic cells.  The configuration considered\n"
    message += "is a two-cell system with the cells moving away from each other\n"
    message += "with equal and opposite prescribed initial velocities."
    #print message

    # material properties
    k = 6.667e9            # bulk modulus
    mu = 5.0e9            # shear modulus
    density = 800.0
    criticalStretch = 0.0028955

    omega = 1.0   # influence function    

    # initial configuration
    cellVolume = 1.05
    mass = cellVolume*density
    initialDistance = 1.0
    weightedVolume = omega*initialDistance*initialDistance*cellVolume

    criticalExtension = initialDistance*criticalStretch
    criticalDistance = criticalExtension + initialDistance

    # the expression for the pairwise force in terms of the extension
    # t = C e

    C = (9.0*k - 15.0*mu)*omega*omega*initialDistance*initialDistance*cellVolume/(weightedVolume*weightedVolume) + \
        15.0*mu*omega/weightedVolume

    # the work done in getting to criticalDistance is the integral of the total force (which is
    # two times the pairwise force) times one half delta extension (because the particles are
    # moving away from each other, the distance traveled for one cell is half the extension).
    # Both cells must be considered.

    # the cellVolumes are required to convert the force density per unit volume to a force

    work = 2.0*cellVolume*cellVolume*C*criticalExtension*criticalExtension/2.0

    # the critical initial velocity for bond breaking is determined by
    # setting the initial kinetic energy equal to the work required to
    # reach the critical stretch

    criticalVelocity = sqrt( work/mass )

    #print "\nMaterial properties:"
    #print "  bulk modulus =                  ", k
    #print "  shear modulus =                 ", mu
    #print "  density =                       ", density
    #print "  critical stretch =              ", criticalStretch

    #print "\nInitial configuration:"
    #print "  cell volume =                   ", cellVolume
    #print "  initial distance =              ", initialDistance

    #print "\nMiscellaneous stuff:"
   # print "  mass =                          ", mass
    #print "  weighted volume =               ", weightedVolume
    #print "  extension at critical stretch = ", criticalExtension
    #print "  distance at critical stretch =  ", criticalDistance
    #print "  work =                          ", work

    print (criticalVelocity)
                                                                                                                                                                                                                   
