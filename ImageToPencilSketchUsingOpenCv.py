#!/usr/bin/env python
# coding: utf-8

# In[2]:


#OpenCV is a huge open-source library for computer vision, machine learning, and image processing. 
#OpenCV supports a wide variety of programming languages like Python, C++, Java, etc.
#It can process images and videos to identify objects, faces, or even the handwriting of a human
pip install opencv-python


# In[4]:


#command to import openCV library class so that inbuilt fxn can be exposed
import cv2


# In[8]:


#Checking the current working directoy so that a sample pic can be placed there for operations
pwd


# In[10]:


#imread is to read the image
img=cv2.imread("SumitChandPic_JPEG.JPG")


# In[13]:


cv2.imshow('Original Pic',img) #imshow is to show the image

#The waitkey() is a keyword binding function and it only accepts time in milliseconds as an argument. 
#When you add any time as an argument , then it waits for the specified time and then the program continues.
#If o is passed , it waits indefinitely until a key is pressed. 
#It can also be useful in determining the keyboard alphabet you have type.
#In the next section, we will know the steps to implement it on an image.
cv2.waitKey(5000) 

#cv2.destroyAllWindows() simply destroys all the windows we created. To
#destroy any specific window, use the function cv2.destroyWindow() where you pass the exact window name.
cv2.destroyAllWindows()


# In[18]:


gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Pic',gray_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()


# In[21]:


inverted_image=255-gray_image
cv2.imshow('Inverted Pic',inverted_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()


# In[22]:


blurred = cv2.GaussianBlur(inverted_image,(21,21),0)


# In[24]:


inverted_blurred=255-blurred
pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=256.0)
cv2.imshow("Sketch",pencil_sketch)
cv2.waitKey(5000)
cv2.destroyAllWindows()


# In[26]:


cv2.imshow("Original Pic",img)
cv2.imshow("Pencil Sketch",pencil_sketch)
cv2.waitKey(5000)


# In[27]:


cv2.destroyAllWindows()

