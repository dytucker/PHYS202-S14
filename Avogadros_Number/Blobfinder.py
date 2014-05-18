
#usual opening stuff
%pylab inline
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from StringIO import StringIO

#Defining class Blob
class Blob():
    def __init__(self):
        self.blobPoints = []
        self.mass = 0
    def add(self,i,j):
        self.blobPoints.append((i,j));
    def getmass(self):
        self.mass = len(self.blobPoints)
    def distanceTo(self,other_blob):
        xdistance = self.centerOfMass[0] - other_blob.centerOfMass[0]
        ydistance = self.centerOfMass[1] - other_blob.centerOfMass[1]

        self.distance = (xdistance**2 + ydistance**2)**0.5
        
    def getcenterOfMass(self):
        total = []
        xtot = 0
        ytot = 0
        for point in self.blobPoints:
            xtot += point[0]
            ytot += point[1]
        xave =  float(xtot) / len(self.blobPoints)
        yave =  float(ytot) / len(self.blobPoints)   
        self.centerOfMass = [xave,yave]

#the monochrome function
def monochrome(picture, threshold):
    """loops over the pixels in the loaded image, 
    replacing the RGB values of each with either 
    black or white depending on whether its total 
    luminance is above or below some threshold 
    passed in by the user"""
    black = (0, 0, 0)
    white = (255, 255, 255)
    xsize, ysize = picture.size
    temp = picture.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b >= threshold: 
                temp[x,y] = black
            else:
                temp[x,y] = white

#The count function
def count(picture, counter, blob_list):
    """scan the image top to bottom and left to right using a nested loop.
    when black pixel is found, increment the count, create a new blob, then call the fill
    function to fill in all the pixels connected to that one. Put the pixels into the blob in the fill function."""
    BLACK = (0,0,0)
    RED = (255,0,0)
    xsize, ysize = picture.size
    temp = picture.load()
    result = 0
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == BLACK:
                result += 1
                """create a new blob"""
                blobbert = Blob()
                fill(temp,xsize,ysize,x,y,blobbert)
                blobbert.getmass()
                blobbert.getcenterOfMass()
                blob_list.append(blobbert)
    return blob_list

#The fill function
def fill(picture, xsize, ysize, xstart, ystart,current_blob):
    """keep a list of pixels that need to be looked at, 
    but haven't yet been filled in - a list of the (x,y) 
    coordinates of pixels that are neighbors of ones we have 
    already examined.  Keep looping until there's nothing 
    left in this list. When a pixel is filled in, put it into the blob"""
    queue = [(xstart,ystart)]
    while queue:
        x,y,queue = queue[0][0], queue[0][1], queue[1:]
        if picture[x,y] == BLACK:
            picture[x,y] = RED
            """if a point is red, add that point to the current blob we're working with"""
            blobbert.add(x,y)
            if x > 0:
                queue.append((x-1,y))
            if x < (xsize-1):
                queue.append((x+1,y))
            if y > 0:
                queue.append((x, y-1))
            if y < (ysize-1):
                queue.append((x, y+1))
                
#The BlobFinder function
def BlobFinder(picture, tau):
    float(tau)
    blob_list = []
    monochrome(picture, tau)
    slide = picture.load()
    all_blobs = count(slide,fill,blob_list)
    
    return all_blobs

#The count beads function
def countBeads(P,blob_list):
    """return the number of beads with >= P pixels"""
    counter = 0
    for b in blob_list:
        if b.mass >= P:
            counter += 1
    return counter
            
#The Get beads function
def getBeads(P,blob_list):
    """return all beads with >= P pixels"""
    bigBlob_list = []
    for b in blob_list:
        if b.mass >= 25:
            bigBlob_list.append(b)
    return bigBlob_list