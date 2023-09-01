import cv2 as cv
import pyrealsense2 as rs
import numpy as np


class RealSense:
    def __init__(self, width, height, fps):
        self.pipeline = rs.pipeline()
        
        config = rs.config()
        config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
        config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
        self.pipeline.start(config)
        
        self.width = width
        self.height = height
        self.fps = fps
    
    
    
    
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


def main():
    
    realsense = RealSense(1280, 720, 6)
    
    while True:
        realsense.getFrames()

        
        realsense.showImages()
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    realsense.pipeline.stop()
    
if __name__ == '__main__':
    main()