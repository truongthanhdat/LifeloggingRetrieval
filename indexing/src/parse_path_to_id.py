import numpy as np
import xml.etree.ElementTree as ET

tree = ET.parse('NTCIR13-ImageCLEF2018lifelog_deveset_metadata.xml')
root = tree.getroot()

result = []

for images in root.iter("images"):
    for image in images.findall("image"):
        image_id = image.find("image-id").text
        image_path = image.find("image-path").text

        cur = {image_path[3:] : image_id}
        print(cur)
        result.append(cur)

np.save('path_to_id.npy', result)

test = np.load('path_to_id.npy')
print(test)