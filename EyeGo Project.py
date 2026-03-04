#EyeGo Project
import cv2
#first we create object to use our webcam for tracking
cap = cv2.VideoCapture(0) # zero because we are using our internal camera (laptop camera)

tracker = cv2.legacy.TrackerCSRT_create() # create a tracker object
# i used CSRT tracker because it is more accurate than other trackers but it is slower than other trackers like KCF and MOSSE

success,img = cap.read() # read the video frame by frame
boundingBox = cv2.selectROI("Tracking",img,False) # select the object to track and false to not show the lines inside the bounding box of the corsshiar
tracker.init(img,boundingBox) # initialize the tracker with the first frame and the bounding box

def drawBox(img,boundingBox):
    x,y,w,h = int(boundingBox[0]), int(boundingBox[1]), int(boundingBox[2]), int(boundingBox[3]) # get the coordinates of the bounding box and convert them to integers
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3,1) # draw a rectangle on the image with the coordinates of the bounding box and with blue color and thickness of 3 and line type of 1
    cv2.putText(img,"Now Tracking", (5,55),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2) # put text on the image to show that we are tracking the object and with green color and thickness of 2

while True:
    # check frames per second
    timer = cv2.getTickCount()
    success , img = cap.read() # read the video frame by frame

    success, boundingBox = tracker.update(img) # update the tracker and get the new bounding box
    print(boundingBox) # to show us the coordinates of the bounding box in the terminal like x,y width and height
    if success:
       drawBox(img,boundingBox) # draw the bounding box on the image
    else:
        cv2.putText(img,"Lost tracking the object", (5,55),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer) # calculate fps
    cv2.putText(img,str(int(fps)), (5,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("Tracking",img) # show the video feed
    if cv2.waitKey(1) & 0xFF == ord('q'): # here we choose to press q to quit
        break # so if user clicks q it quits
