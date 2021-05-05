import requests
from urllib.request import urlopen

def dispatch_request(addr,image_path):
        test_url = addr + '/predict'
        my_img = {'image': urlopen(image_path).read()}
        recv_response = requests.post(test_url, files=my_img)
        print(recv_response.text)
        print(recv_response.json())
        jsonResponse = recv_response.json()
        recv_dict = {}
        for key, value in jsonResponse.items():
                print(key, ":", value)
                recv_dict[key] = value

        coordinates = recv_dict['size'][1:len(recv_dict['size']) - 1].split(",")
        list_of_coordinates = []
        for i in coordinates:
                list_of_coordinates.append(float(i))

        return tuple(list_of_coordinates)

