import wf_dataprocessing
import wf_visualization
import hashlib
import os

def get_file_hash(filepath):
    with open(os.path.join("data_original", filepath), "rb") as file:
        hash_computer = hashlib.md5()
        while data := file.read(8192):
            hash_computer.update(data)
            
    return hash_computer.hexdigest()


if __name__ == "__main__":
    data_original = get_file_hash("data_original.csv")
    inflation_rates = get_file_hash("inflation_rates.csv")
    mortgage_interest = get_file_hash("mortgage_interest.csv")
    print("data_original.cvs = "+data_original+"    inflation_rates.csv = "+ inflation_rates+"     mortgage_interest.csv = "+mortgage_interest)
    wf_dataprocessing.process()
    wf_visualization.visualize()