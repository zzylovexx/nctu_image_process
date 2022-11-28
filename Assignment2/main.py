import sys
sys.path.append('C:/nycu_image_processing/Assignment2')
from utils import utils
import canny_edge_decector as ced
imgs = utils.load_data()
utils.visualize(imgs, 'gray')
detector = ced.cannyEdgeDetector(imgs, sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
imgs_final = detector.detect()
utils.visualize(imgs_final, 'gray')