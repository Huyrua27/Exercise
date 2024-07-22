import cv2
import numpy as np

def canny_edge_detector(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image):
    height, width = image.shape[:2]
    mask = np.zeros_like(image)

    # Define the region of interest
    polygon = np.array([[
        (0, height),
        (width, height),
        (width, int(height / 1.5)),
        (0, int(height / 1.5)),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)
    return line_image

def filter_lines(lines, min_angle=30, max_angle=60):
    filtered_lines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            angle = np.abs(np.arctan2(y2 - y1, x2 - x1) * 180.0 / np.pi)
            if min_angle < angle < max_angle:
                filtered_lines.append(line)
    return filtered_lines

def process_image(image):
    # Convert to HSV and filter for gray color
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_gray = np.array([0, 0, 50])
    upper_gray = np.array([180, 50, 200])
    mask = cv2.inRange(hsv_image, lower_gray, upper_gray)
    gray_filtered_image = cv2.bitwise_and(image, image, mask=mask)

    canny_image = canny_edge_detector(gray_filtered_image)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    
    # Filter lines based on angle
    filtered_lines = filter_lines(lines)
    
    line_image = display_lines(image, filtered_lines)
    combo_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)
    return combo_image

# Read image from file
input_image = cv2.imread('test.png')

# Process image
output_image = process_image(input_image)

# Display image
cv2.imshow('Lane Detection', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()