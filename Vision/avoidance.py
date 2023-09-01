import cv2 as cv
import pyrealsense2 as rs
import numpy as np

# Initialize global variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)




class RealSense:
    def __init__(self, width:int, height:int, fps:int):
        self.pipeline = rs.pipeline()
        
        config = rs.config()
        config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
        config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
        self.pipeline.start(config)
        
        self.width = width
        self.height = height
        self.fps = fps
        self.midwidth = width // 2
        self.midheight = height // 2
    
    
    
    def getFrames(self):
        frames = self.pipeline.wait_for_frames()
        
        self.depth_frame = frames.get_depth_frame()
        self.color_frame = frames.get_color_frame()
        
        self.depth_color_frame = rs.colorizer().colorize(self.depth_frame)
        
        
        if not self.depth_frame or not self.color_frame:
            return False
        
        self.depth_color_image = np.asanyarray(self.depth_color_frame.get_data())
        self.color_image = np.asanyarray(self.color_frame.get_data())
    

    def showImages(self):
        cv.imshow('Color', self.color_image)
        cv.imshow('Depth', self.depth_color_image)


    def getDistance(self, x:int, y:int):
        return self.depth_frame.get_distance(x, y)
    
    
    def drawPoint(self, x:int, y:int, image:str, color:tuple):
        if image == 'color':
            cv.circle(self.color_image, (x, y), 1, color, 5)
        elif image == 'depth':
            cv.circle(self.depth_color_image, (x, y), 1, color, 5)
        else:
            print("RealSense.drawPoint() ERROR: Not a valid image.")    
    
def main():
    
    realsense = RealSense(1280, 720, 6)
    
    while True:
        realsense.getFrames()

        
        print(realsense.getDistance(realsense.midwidth, realsense.midheight))
        
        realsense.drawPoint(realsense.midwidth, realsense.midheight, 'depth', GREEN)
        
        
        
        
        
        realsense.showImages()
        
        
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            print("Quitting...")
            break
        
    realsense.pipeline.stop()
    
if __name__ == '__main__':
    main()