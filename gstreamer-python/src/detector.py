#!/usr/bin/env python3

# Filename: detector.py
# Author: Nagel Mejía Segura
# Description: This script is the box detector implementation with opencv 

import cv2

class Detector:
    # Constructor
    def __init__(self):
        self.frame_count = 0
    
    # sobel_edge_detection: It receives a frame and applies the sobel edge detection to the frame
    # Returns a new edged frame
    def sobel_edge_detection(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)
        sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = cv2.sqrt(sobelx**2 + sobely**2)
        edged = cv2.convertScaleAbs(sobel_combined)
        _, edged = cv2.threshold(edged, 80, 255, cv2.THRESH_BINARY)
        return edged

    # draw_boxes: Draws rectangles around the detected boxes
    # frame: Original frame
    # edged: Edged frame after sobel method
    # Returns a new frame with the result and the quantity of boxes drawn
    def draw_boxes(self, frame, edged):
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw boxes for significant contours
        boxes_drawn = 0
        color = (0, 255, 0)  # Green for all boxes
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < 1500:
                continue

            hull = cv2.convexHull(contour)
            x, y, w, h = cv2.boundingRect(hull)
            
            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            boxes_drawn += 1

        # Add frame info with boxes count only
        info_text = f' Boxes in view: {boxes_drawn}'
        cv2.putText(frame, info_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, 'Press Q to quit', (10, frame.shape[0] - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        return frame, boxes_drawn

    # process_frame: Method to simplify all the opencv processing
    # frame: Original 
    def process_frame(self, frame):
        edges = self.sobel_edge_detection(frame)
        result_frame, boxes_count = self.draw_boxes(frame.copy(), edges)
        self.frame_count += 1
        return result_frame, edges, boxes_count