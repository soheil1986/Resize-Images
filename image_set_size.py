# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:21:55 2019

@author: sohei
"""

from PIL import Image
#import cv2
import glob
count=0
for filename in glob.glob('C:/Afrozan/script_python/SS 2016/*.jpg'):
    print(count)
    im = Image.open(filename)
    #im = cv2.imread('C:/Afrozan/script_python/SS 2016/*.jpg',1)
    w, h = im.size
    #w, h = cv2.GetSize(im)
    # w is the real width of the original image (x)
    # h is the real height of the original image(y)
    print('width: ', w)
    print('height:', h)
    # x is the proportion of width regard to 1000/1600 with respect to orig. image
    # y is the proportion of the height to 1000/1600 with respect to orig. image
    x= (h*1000.0)/1600.0
    print("in order to reach to right proportion width shall be = ", x)
    y=(w*1600.0)/1000.0
    print("in order to reach to right proportion height shall be = ",y)
    
    if x<w:
        print("we should chnage the width in crop function")
        cropped = im.crop( ( 0.0, 0.0, x ,h ) )
        #cropped = im[0:h, 0:x]
    elif y<h :
        print("we should change the height in crop function")
        cropped = im.crop( ( 0.0, 0.0, w ,y ) )
        #cropped = im[0:y, 0:w]
    else :
        print("we should not change anything and we are in the right proportion")
        cropped = im.crop( ( 0.0, 0.0, w ,h ) )
        #cropped = im[0:h, 0:w]
    
    
    ##cropped.show()
    newsize = (1000, 1600) 
    im1 = cropped.resize(newsize)
    #im1=cv2.resize(cropped, newsize)
    im1 = im1.save('C:/Afrozan/script_python/SS 2016/1000_1600/'+str(count)+'.jpg') 
    #cv2.imwrite('C:/Afrozan/script_python/SS 2016/1000_1600/'+str(count)+'.jpg', im1) 
    count=count+1